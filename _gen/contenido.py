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

PLAZOS = [
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

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = [
("es", "CCN y ENS · 23 jul 2026 · vence el 15 de septiembre", True,
 "El CCN obliga a toda entidad en ámbito ENS a autoevaluarse frente a la IA ofensiva",
 "El CCN ha incorporado a <b>INES</b> un cuestionario de madurez sobre <i>IA ofensiva</i>, accesible con Cl@ve PIN o doble factor. Cubre ingeniería social, protección de credenciales, detección y respuesta, y gobierno interno de herramientas de IA, y devuelve una calificación de madurez con recomendaciones priorizadas. El CCN pide a todas las entidades sujetas al ENS completarlo <b>antes del 15 de septiembre de 2026</b>, coordinado por el Responsable de Seguridad, elevando los resultados al Comité de Seguridad de la Información e integrándolos en el análisis de riesgos y el plan de tratamiento.",
 "Es el único plazo español duro del periodo y cae de lleno en agosto. Encargo concreto y facturable para todo cliente del sector público y para sus proveedores en ámbito ENS. Además marca la dirección de la supervisión: el CCN está usando INES para recoger datos temáticos de madurez más allá del catálogo de medidas del ENS, así que conviene anticipar que estas preguntas aparecerán en futuras revisiones de conformidad.",
 '<a href="https://www.ccn.cni.es/es/actualidad-ccn/1374-el-ccn-insta-a-las-entidades-publicas-a-completar-cuanto-antes-el-formulario-de-autoevaluacion-sobre-ia-ofensiva" @L>El aviso del 23 de julio</a> y, debajo, la guía <b>CCN-CERT BP/36</b>, <i>Buenas prácticas frente al modelo de IA ofensiva</i>.',
 None),

("es", "Contencioso · 8 jul 2026", True,
 "La Comisión demanda a España ante el TJUE por NIS2, con petición de sanciones económicas",
 "España, Irlanda, Francia y Países Bajos han sido llevados ante el Tribunal de Justicia por no notificar las medidas de transposición de la Directiva (UE) 2022/2555. La nota es literal: «Las remisiones incluyen una solicitud al Tribunal para que imponga sanciones económicas, consistentes en una suma a tanto alzado y multas coercitivas diarias hasta la notificación de la transposición completa.» La cadena de escalado: plazo el 17 de octubre de 2024, cartas de emplazamiento el 28 de noviembre de 2024, dictámenes motivados el 7 de mayo de 2025 y demanda el 8 de julio de 2026.",
 "Mientras no exista la ley española <b>no hay registro nacional de entidades NIS2, ni plazo de registro en vigor, ni régimen sancionador</b>: siguen rigiendo el RDL 12/2018 y el RD 43/2021. Conviene ser preciso con los clientes, porque abunda el contenido de consultoría que afirma plazos españoles de registro para 2026 que ninguna fuente primaria sostiene. Lo que cambia la demanda es el riesgo de calendario: la adopción será probablemente tardía y además comprimida.",
 '<a href="https://digital-strategy.ec.europa.eu/en/news/commission-refers-ireland-spain-france-and-netherlands-court-justice-failing-transpose-rules" @L>IP/26/1499 completo</a> y el <a href="https://www.interior.gob.es/opencms/pdf/servicios-al-ciudadano/participacion-ciudadana/Participacion-publica-en-proyectos-normativos/Audiencia-e-informacion-publica/01_2025_Anteproyecto_ley_coordinacion_gobernanza_ciberseguridad.pdf" @L>texto del Anteproyecto</a>.',
 "He podido confirmar que la ley no está en el BOE y que no está transpuesta. No he podido confirmar su fase administrativa exacta, dictamen del Consejo de Estado o pendiente de segunda lectura, porque el buscador de iniciativas del Congreso funciona con JavaScript y no devuelve registro legible."),

("es", "Compras y arquitectura · 27 jul 2026", False,
 "Revisión del CPSTIC: reescritas 45 de las 73 familias, y se fusionan ENS Media y Alta",
 "En palabras del propio CCN, la actualización «simplifica la estructura de los Requisitos Fundamentales de Seguridad al integrar en un único documento por familia los requisitos para ENS categoría Media y ENS categoría Alta». Añade matrices de trazabilidad hacia <b>LINCE, CICLON y Common Criteria</b>, requisitos explícitos para productos de seguridad desplegados en la nube, y un esfuerzo máximo de evaluación en jornadas para LINCE en ENS Media. No se ha anunciado periodo transitorio ni fecha de corte para productos ya cualificados.",
 "El artículo 19 del RD 311/2022 exige productos cualificados del CPSTIC en sistemas ENS Media y Alta, así que esto reconfigura directamente el asesoramiento en compras y arquitectura. La fusión Media con Alta y los nuevos requisitos de nube pegan más fuerte en parques híbridos, y la trazabilidad hacia CICLON es la continuación operativa de la metodología de certificación en nube que el CCN presentó en mayo.",
 '<a href="https://www.ccn.cni.es/es/actualidad-ccn/1375-el-ccn-actualiza-45-de-las-73-familias-del-cpstic-para-simplificar-la-cualificacion-de-productos-de-seguridad-tic" @L>El anuncio</a> y después los documentos de requisitos por familia en el catálogo CPSTIC (anexos de la CCN-STIC 140).',
 None),

("es", "Criptografía · 22 jul 2026", False,
 "El CCN fija las primeras fechas nacionales de migración poscuántica: 2030 y 2035",
 "<i>Recomendaciones para una transición PQC segura</i> establece objetivos explícitos: sistemas de riesgo alto completamente migrados a criptografía resistente a lo cuántico <b>antes del 31 de diciembre de 2030</b>, riesgo medio <b>antes del 31 de diciembre de 2035</b>, y riesgo bajo en la medida de lo posible. Incluye un decálogo de buenas prácticas e insta a arrancar ya el descubrimiento y el inventario. Llega después de que el CCN admitiera en junio el primer producto resistente a lo cuántico en el CPSTIC para Difusión Limitada.",
 "Son anclas nacionales defendibles para una hoja de ruta de agilidad criptográfica, y están alineadas con el calendario europeo: mucho más fáciles de vender que una fecha propuesta por un fabricante. Cabe esperar que el inventario criptográfico se convierta en materia de auditoría ENS. Los clientes con horizontes largos de confidencialidad, como sanidad, cadena de suministro de defensa o el ámbito notarial y registral, deberían iniciar el análisis de <i>harvest now, decrypt later</i> en este ciclo presupuestario.",
 'Cítalo como <b>CCN-CERT BP/37 y CCN-TEC 009</b>. <a href="https://www.ccn.cni.es/es/actualidad-ccn/1372-el-centro-criptologico-nacional-advierte-de-los-graves-riesgos-que-supone-la-amenaza-cuantica-para-la-seguridad-de-la-informacion-y-llama-a-prepararse-frente-a-ella" @L>Anuncio aquí</a>.',
 "El documento lleva dos referencias: BP/37 en la serie de buenas prácticas del CCN-CERT y CCN-TEC 009 en la portada del PDF. Usa ambas. El PDF está alojado en ccn-cert.cni.es, que bloquea el acceso automatizado, así que las fechas están confirmadas desde la noticia del CCN y no desde la guía."),

("es", "Líneas base · 1 jul 2026", False,
 "Veinte guías CCN-STIC de la serie 1000 publicadas o actualizadas",
 "<b>14 nuevas</b>, entre ellas la CCN-STIC 1116 (Microsoft Entra ID), 1222 (Cortex XDR Agent), 1225 (Splunk), 1226 (SentinelOne), 1246 (Elastic Platform), 1307 y 1308 (Azure Monitor Log Analytics y Azure Activity Log), 1519 (Azure Confidential Computing), 1521 a 1523 (firma SIAVAL y Cryhod) y 1658 (Red Hat Enterprise Linux). <b>6 actualizadas</b>: 1247 (Symantec Endpoint Security), 1406 (Fortigate), 1413 (Palo Alto NGFW), 1457 (Nokia SR y SAR), 1480 (ArubaOS-Switch 16) y 1481 (conmutadores Huawei CE).",
 "Los <i>Procedimientos de Empleo Seguro</i> son contra lo que el auditor comprueba realmente que un producto cualificado está desplegado de forma conforme. <b>La CCN-STIC 1116 sobre Entra ID es la destacada</b>: la configuración de identidad es el hallazgo ENS más frecuente y ahora existe una línea base española con autoridad contra la que auditar.",
 '<a href="https://www.ccn.cni.es/es/actualidad-ccn/1366-el-ccn-actualiza-y-amplia-sus-guias-ccn-stic-sobre-procedimiento-de-empleo-seguro-de-20-productos-y-servicios" @L>Nota de publicación con el listado completo</a>.',
 None),

("es", "CER y entidades críticas · BOCG 27 mar 2026", False,
 "El proyecto de ley de entidades críticas va más avanzado que el de NIS2",
 "El <i>Proyecto de Ley de protección y resiliencia de las entidades críticas</i> (expediente 121/000088) transpone la Directiva (UE) 2022/2557 y reforma el régimen de la Ley 8/2011 y del CNPIC. Obligaciones confirmadas en el texto: las entidades críticas designadas presentan <b>evaluación de riesgos en 9 meses</b> desde la notificación, <b>plan de resiliencia en 6 meses</b> desde que la completan, notificación de incidentes <b>en 24 horas</b> e informe detallado en un mes. La Comisión de Interior recibió competencia legislativa plena el 24 de marzo de 2026.",
 "CER y NIS2 solapan mucho, en energía, transporte, agua, salud, banca e infraestructura digital, y CER está sistemáticamente infratratada en los programas de cliente. El plazo de 9 meses arranca con la designación, no con la entrada en vigor de la ley, así que los probables designados deberían estar construyendo ya los entregables de evaluación y plan de resiliencia.",
 '<a href="https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-88-1.PDF" @L>Texto del proyecto (BOCG-15-A-88-1)</a> y el <a href="https://www.congreso.es/webpublica/documentacion/docs_trabajo/leg15/121_000088/121_000088_dosier.pdf" @L>dosier legislativo del Congreso</a>.',
 "Que no haya avanzado desde abril es una inferencia por ausencia de documentos BOCG posteriores, no una confirmación positiva."),

("eu", "CRA · en vigor el 11 de septiembre de 2026", True,
 "La notificación del artículo 14 del CRA arranca en cuatro semanas, y ENISA ya ha publicado el material de alta",
 "Desde el <b>11 de septiembre de 2026</b> los fabricantes deben notificar vulnerabilidades explotadas activamente e incidentes graves: <b>alerta temprana en 24 horas, notificación principal en 72 horas</b>, e informe final en 14 días para vulnerabilidades o un mes para incidentes desde que haya medida correctora disponible. ENISA publicó el 31 de julio el material operativo de alta en la Plataforma Única de Notificación: registro de usuario del representante autorizado, envío y actualización de notificaciones, ficha técnica y preguntas frecuentes. Un acto delegado de la Comisión de 11 de diciembre de 2025 regula cuándo puede retrasarse la difusión a otros CSIRT.",
 "Es el plazo duro más próximo de toda la pila normativa europea. Cualquier cliente que fabrique, integre o actúe como representante autorizado de un producto con elementos digitales necesita un responsable de notificación con nombre y apellidos, una cuenta registrada en la plataforma y una vía de triaje de 24 horas antes del 11 de septiembre. Y hay una asimetría que conviene explicar al consejo: <b>la notificación obliga ya, pero los requisitos esenciales de fondo no lo hacen hasta el 11 de diciembre de 2027</b>, es decir, hay que notificar sobre productos que todavía no está obligado a haber hecho conformes.",
 '<a href="https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp" @L>Páginas de la Plataforma Única de Notificación de ENISA</a> y la <a href="https://digital-strategy.ec.europa.eu/en/policies/cra-reporting" @L>página de política de notificación CRA de la Comisión</a>.',
 None),

("eu", "CRA · 27 jul 2026", True,
 "La Comisión adopta la guía de aplicación del CRA, C(2026) 5252",
 "Una Comunicación con anexo que resuelve las cuestiones de alcance que llevaban meses discutiéndose: cuándo entran las <b>soluciones de tratamiento remoto de datos</b> y el <b>software libre y de código abierto</b>, qué cuenta como <b>modificación sustancial</b>, cómo determinar el <b>periodo de soporte</b> del artículo 13.8 (mínimo cinco años salvo vida útil esperada menor) y el alcance de la notificación del artículo 14. Unos 67 ejemplos trabajados, diagramas de flujo y casos de uso, orientados a microempresas y pymes.",
 "Es el instrumento de delimitación con autoridad que los clientes llevaban esperando, y llega seis semanas antes de que arranque la notificación. <b>Conviene reejecutar cualquier análisis de alcance hecho en 2025</b>, sobre todo en productos próximos al SaaS y en quien distribuya componentes de código abierto, porque las premisas pueden haber quedado obsoletas.",
 '<a href="https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation" @L>El anexo de C(2026) 5252</a>, primero el apartado de ámbito de aplicación y el de modificación sustancial.',
 None),

("eu", "CER · DOUE 13 jul 2026", True,
 "Venció el 17 de julio el plazo de identificación de entidades críticas, y ya están en el DOUE las directrices del artículo 13.5",
 "<i>Comunicación de la Comisión: Directrices sobre la aplicación del artículo 13, apartado 5, de la Directiva (UE) 2022/2557</i>, publicada como <b>C/2026/3712</b>. Orientación no vinculante sobre las medidas técnicas, de seguridad y organizativas que deben adoptar las entidades críticas: prevención de perturbaciones, protección física, mitigación y recuperación de incidentes, gestión y concienciación de seguridad del personal, frente a accidentes, catástrofes naturales, emergencias de salud pública, ataques con drones y amenazas híbridas. En paralelo, los Estados miembros debían <b>identificar</b> a sus entidades críticas antes del <b>17 de julio de 2026</b>.",
 "Pregunta a todo cliente en ámbito NIS2 si ha recibido notificación de identificación, porque <b>muchos no se habrán dado cuenta</b>. Las obligaciones CER conviven con las de NIS2, no están dentro de ellas, y la identificación dispara por sí sola los deberes de plan de resiliencia y de notificación de incidentes con su propio reloj.",
 '<a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=OJ%%3AC_202603712" @L>C/2026/3712 en el DOUE</a>, la taxonomía de medidas mapeada al artículo 13.1.',
 "El término técnico de la Directiva es «identificar», no «designar»: conviene precisarlo en documentos de cliente. No he verificado el estado de identificación en España."),

("eu", "Certificación · consulta hasta el 13 de septiembre", True,
 "ENISA consulta el esquema europeo de certificación de servicios gestionados de seguridad (EUMSS)",
 "El borrador del esquema candidato, solicitado al amparo del artículo 48.1 del Reglamento de Ciberseguridad, está en consulta pública hasta el <b>13 de septiembre de 2026</b>. Estructura por capas: requisitos horizontales de base en cinco dominios, que son diseño seguro, gestión del despliegue, disponibilidad, gestión operativa y mejora continua, más requisitos verticales por servicio, empezando por un perfil de Respuesta a Incidentes. Tres niveles de garantía: básico, sustancial y alto.",
 "Es el primer esquema europeo de certificación dirigido a servicios y no a productos, y se convertirá en la referencia para la diligencia debida de cadena de suministro del artículo 21 de NIS2 sobre proveedores de SOC y MSSP. Los dominios de base acabarán siendo la lista de comprobación de facto en las compras europeas. Los MSSP españoles deberían comparar ya el borrador con la certificación ENS para detectar huecos, y los clientes que compran MDR deberían responder mientras el texto todavía se puede mover.",
 '<a href="https://certification.enisa.europa.eu/browse-topic/eumss_en" @L>Borrador del esquema</a> y el <a href="https://www.enisa.europa.eu/news/have-your-say-on-the-certification-of-eu-managed-security-services" @L>anuncio de la consulta con el formulario de respuesta</a>.',
 None),

("eu", "Herramientas gratuitas · 13 y 30 jul 2026", False,
 "ENISA publica dos activos directamente facturables para preparación al CRA",
 "El <b>Modelo de Evaluación de Madurez de Ciberresiliencia para Pymes</b>, del 13 de julio: autoevaluación gratuita en PDF con herramienta de puntuación en .xlsx, mapeada a los requisitos del CRA y utilizable también por integradores y proveedores de servicios. Y el <b>Secure by Design and Default Playbook</b>, del 30 de julio, con 22 manuales publicados en abierto en GitHub.",
 "El modelo de madurez te da una línea base redactada por el regulador para una evaluación de preparación al CRA: mucho más fácil de vender y de defender ante un comité de auditoría que un cuadro de mando propietario, y encaja especialmente bien con pymes españolas reacias a marcos a medida. Los manuales de GitHub son un entregable de ingeniería listo para usar.",
 '<a href="https://www.enisa.europa.eu/publications/sme-cyber-resilience-maturity-assessment-model" @L>Modelo de madurez y herramienta .xlsx</a> y el <a href="https://www.enisa.europa.eu/publications/enisa-secure-by-design-and-default-playbook" @L>Secure by Design Playbook</a>.',
 None),

("eu", "Legislativo · en curso", False,
 "La revisión del Reglamento de Ciberseguridad (CSA2) está atascada en la base jurídica",
 "El procedimiento <b>2026/0011(COD)</b> sigue en la comisión ITRE con Markéta Gregorová como ponente, en estado de pendiente de decisión de la comisión: sin proyecto de informe, sin votación en comisión y sin orientación general del Consejo. El informe de situación del Consejo de mayo señaló dudas sobre la <b>base jurídica y la competencia de la UE</b> y remitió la cuestión a su Servicio Jurídico. La propuesta reforzaría el mandato de ENISA, reestructuraría la certificación, incluida la de postura de ciberseguridad, y viene acompañada de modificaciones selectivas de NIS2 que afectarían a unas 28.700 empresas.",
 "No hay nada que cumplir, y la disputa competencial hace probable el retraso: precisamente por eso importa. Los clientes oirán que viene la simplificación y querrán aplazar. No viene pronto. Lo que sí conviene incorporar a las hojas de ruta plurianuales: la certificación se está reposicionando como instrumento de reducción de carga de cumplimiento, y el concepto de punto único de notificación acabaría consolidando la notificación de incidentes de NIS2, RGPD y CRA.",
 '<a href="https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2026/0011(COD)" @L>Ficha del Observatorio Legislativo del PE</a> y la <a href="https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/789345/EPRS_BRI(2026)789345_EN.pdf" @L>nota informativa del EPRS</a>.',
 None),

("fin", "BCE y MUS · 7 jul 2026 · vence el 31 de octubre", True,
 "El BCE exige a toda entidad significativa un plan de acción sobre ciberamenaza con IA",
 "Claudia Buch escribió a los consejeros delegados de todas las entidades significativas exigiendo evaluar «sin demora» el panorama de amenaza potenciada por IA y elaborar un plan de acción integral. Literal: «Este plan de acción debe presentarse al Equipo Conjunto de Supervisión (JST) correspondiente antes del 31 de octubre de 2026.» Prioridades a corto plazo: acelerar la gestión de vulnerabilidades y parches a escala, reforzar la monitorización, la detección y la capacidad defensiva con IA, y reverificar la idoneidad de la gestión de riesgo de terceros. Los consejos deben revisar el marco de apetito de riesgo. La carta afirma que los requisitos de DORA «siguen siendo plenamente relevantes y válidos»: esto es intensificación supervisora, no norma nueva.",
 "Obliga a todas las entidades significativas españolas: Santander, BBVA, CaixaBank, Sabadell, Bankinter, Unicaja, Abanca, Ibercaja, Kutxabank y Cajamar. El plan se leerá como <b>entregable de gobernanza</b>, con controles concretos, asignación de recursos, roles con nombre y calendarios de implantación. Una presentación genérica no sobrevivirá a la revisión del JST, y cabe esperar que se contraste con los hallazgos TIC abiertos.",
 '<a href="https://www.bankingsupervision.europa.eu/press/letterstobanks/shared/pdf/2026/ssm.2026_letter_on_AI_enabled_cybersecurity_threats.en.pdf" @L>La carta, cuatro páginas</a>, en particular el desglose de corto y largo plazo y el párrafo de gobernanza.',
 None),

("fin", "España y sanciones · enmiendas hasta el 9 de septiembre", True,
 "El proyecto de ley que adapta DORA llega al Congreso, y amplía el perímetro sin hacer ruido",
 "El <i>Proyecto de Ley para la digitalización y modernización del sector financiero</i> (iniciativa 121/000105) adapta el ordenamiento español a DORA y transpone parcialmente la Directiva (UE) 2022/2556. Crea un régimen de tres niveles, muy graves, graves y leves, vinculado a los artículos 50 y 51 de DORA, que cubre fallos de gobernanza TIC, gestión de incidentes, pruebas de resiliencia y supervisión de proveedores TIC, con sanciones fijadas en cada ley sectorial. Confirma a <b>Banco de España, CNMV y DGSFP</b> como autoridades competentes con potestad para requerir documentación, inspeccionar, ordenar el cese e imponer medidas correctoras. Ventana de enmiendas: «un período de ocho días hábiles, que finaliza el día 9 de septiembre de 2026».",
 "DORA lleva siendo directamente aplicable en España pero materialmente inexigible por falta de régimen sancionador nacional: esto cierra el hueco y cambia el cálculo de riesgo en los consejos. <b>La cuestión latente es la ampliación del perímetro</b>, porque el proyecto alcanza a operadores de sistemas de pago, operadores de esquemas de pago, operadores de acuerdos de pago electrónico, procesadores de pagos y mutualidades por encima de determinados umbrales de primas. Clientes que concluyeron que quedaban fuera de DORA pueden estar dentro de un régimen español equivalente. Conviene revisar esos alcances ya.",
 '<a href="https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-106-1.PDF" @L>BOCG-15-A-106-1</a>, las disposiciones finales y el régimen de infracciones y sanciones.',
 None),

("fin", "Autoridades europeas de supervisión · 31 jul 2026", False,
 "La declaración de las AES sobre modelos frontera extiende las expectativas del BCE a seguros, fondos y CASP",
 "EBA, EIOPA y ESMA emitieron a través del Comité Mixto <i>Toward a consistent and risk-based approach for ICT risks from frontier AI models</i> (JC 2026 25). Las expectativas se estructuran en <b>prevención</b>, con inventarios de activos, diseño seguro y parcheo proactivo, <b>detección</b>, con escaneo continuo, monitorización conductual y SOC reforzado, y <b>gestión</b>, con pruebas de resiliencia, recuperación ante desastres y planes de continuidad actualizados. Invoca expresamente el artículo 4 de DORA sobre proporcionalidad y el artículo 10 de la norma técnica de regulación sobre marco de gestión del riesgo TIC.",
 "Eleva expectativas hasta ahora solo bancarias a las poblaciones supervisadas por la DGSFP y la CNMV, donde no existe carta equivalente: seguros, empresas de servicios de inversión, gestoras y proveedores de servicios de criptoactivos. Y algo importante: las AES afirman que <b>la preparación de los proveedores críticos se evaluará en los exámenes de vigilancia de 2027</b>, así que los proveedores TIC designados deberían empezar ya a evidenciar gestión del riesgo de modelos frontera.",
 '<a href="https://www.esma.europa.eu/sites/default/files/2026-07/JC_2026_25_ESA_statement_on_frontier_AI_models.pdf" @L>JC 2026 25</a>, las expectativas para entidades y luego el apartado de vigilancia de proveedores críticos.',
 None),

("fin", "JERS · publicada el 7 jul 2026", False,
 "La JERS eleva a grave el riesgo sistémico ciber derivado de modelos frontera",
 "<i>Advertencia de la Junta Europea de Riesgo Sistémico de 25 de junio de 2026 sobre riesgos ciber sistémicos derivados de modelos frontera de inteligencia artificial</i> (ESRB/2026/3), publicada el 7 de julio. Eleva la valoración de la Junta General de elevado en marzo a <b>grave</b>, e identifica cuatro focos de vulnerabilidad: tiempo hasta el parcheo, capacidad del defensor, concentración y dependencia de un número reducido de fuentes de IA, y capacidad de las autoridades. La Junta General reevaluará trimestralmente.",
 "Es el ancla macroprudencial que explica la carta del BCE y la declaración de las AES: las tres estaban deliberadamente secuenciadas. Una advertencia formal de la JERS es una referencia duradera que puedes poner delante de un consejo para justificar presupuesto. Y el eje de concentración conecta directamente con el <b>análisis de riesgo de concentración del artículo 29 de DORA y con el registro de información</b>.",
 '<a href="https://www.esrb.europa.eu/pub/pdf/warnings/esrb.warning260625_on_systemic_cyber_risks_stemming_from_frontier_ai_models~ef424708cf.en.pdf" @L>ESRB/2026/3</a>, los cuatro focos de vulnerabilidad.',
 None),

("fin", "MUS · 31 jul 2026", False,
 "Prueba de resistencia inversa del BCE: el ciber y la interrupción de terceros encabezan las amenazas en 110 bancos",
 "110 bancos supervisados directamente ejecutaron una prueba de resistencia inversa hasta un objetivo de agotamiento de 300 puntos básicos de CET1, diseñando ellos mismos sus narrativas geopolíticas. Literal: «Los incidentes ciber y la interrupción de servicios de proveedores terceros emergieron como las amenazas más prominentes.» El BCE criticó la escasa granularidad, la débil vinculación entre las narrativas de escenario y los impactos financieros, y unos supuestos de mitigación poco realistas en condiciones de estrés sistémico.",
 "Evidencia dura de que el MUS ya trata la concentración en terceros TIC como impulsor de escenario relevante para capital. Crea un puente práctico entre el registro de información y el análisis de concentración del artículo 29 de DORA y la función de pruebas de resistencia, <b>dos equipos que en la mayoría de entidades españolas no se hablan</b>. Cabe esperar que los JST prueben exactamente ese enlace.",
 '<a href="https://www.bankingsupervision.europa.eu/press/pr/date/2026/html/ssm.pr260731~93964644b0.en.html" @L>Nota de prensa</a> e <a href="https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.geopolstresstest202608.en.pdf" @L>informe temático</a>.',
 "Conviene precisar las consecuencias: el ejercicio no ajustará la orientación de Pilar 2 ni la del ratio de apalancamiento, pero las deficiencias cualitativas sí pueden considerarse en el bloque de gobernanza del SREP y afectar por esa vía al requerimiento de Pilar 2. Decir que no hay consecuencia de capital sería exagerar."),

("fin", "EBA · aplica el 1 de enero de 2027", False,
 "Las Directrices SREP revisadas de la EBA absorben el riesgo TIC y DORA",
 "La EBA ha integrado sus directrices independientes de evaluación del riesgo TIC y las de sucursales de terceros países en un marco único, alrededor de un 30 % más corto, con tratamiento reforzado del riesgo TIC incorporando DORA y una integración más amplia del concepto de resiliencia operativa. Las autoridades competentes pueden aplicar elementos anticipadamente durante la planificación supervisora.",
 "El riesgo TIC deja de evaluarse bajo una directriz separada y pasa a ser una entrada troncal del SREP, también para las entidades menos significativas supervisadas por el Banco de España. <b>Los clientes cuyos marcos de control interno mapean contra la antigua directriz de evaluación del riesgo TIC necesitan remapear antes de cierre de 2026.</b>",
 '<a href="https://www.eba.europa.eu/publications-and-media/press-releases/eba-reaches-another-important-milestone-enhancing-supervisory-efficiency-its-revised-srep-guidelines" @L>Directrices SREP revisadas definitivas</a>, apartados de TIC y resiliencia operativa.',
 None),

("std", "ISO · 27 jul 2026", True,
 "Publicada la ISO/IEC 27017:2026, los controles de nube se realinean al catálogo de 2022",
 "Edición 2.0, 39 páginas. La ISO/IEC 27017:2015 quedó anulada el mismo día, en estado 95.99. El título perdió «Code of practice for»: ahora es <i>Information security controls based on ISO/IEC 27002 for cloud services</i>. El contenido se realinea a la estructura de la ISO/IEC 27002:2022, con 93 controles en cuatro temas, sustituyendo el mapeo de 114 controles de la era 2013 sobre el que se construyó la edición anterior.",
 "Toda atestación 27017 de tu cartera está redactada contra una numeración de cláusulas que ya no existe. <b>Declaraciones de aplicabilidad, matrices de control y dosieres de aseguramiento de nube para clientes necesitan renumerarse</b>, y los proveedores que usan la 27017 como argumento comercial necesitarán auditoría de transición. No se ha publicado plazo de transición, y el organismo que normalmente lo fijaría ya no existe con ese nombre.",
 '<a href="https://www.iso.org/standard/82878.html" @L>ISO/IEC 27017:2026</a>, desde la cláusula 5 y el anexo de correspondencias. Conviene emparejarla con la ISO/IEC 27018:2025: seguridad y privacidad en la nube están ahora ambas renovadas y alineadas al catálogo de 2022.',
 None),

("std", "ISO · 3 jul 2026", False,
 "La ISO/IEC 27000:2026 ya no es la norma de vocabulario",
 "Sexta edición, <b>11 páginas</b>, frente a las 34 de la de 2018. El título ha perdido «and vocabulary»: ahora es <i>Information security, cybersecurity and privacy protection: Information security management systems, Overview</i>. Según el prólogo, la cláusula 3 <i>Terms and Definitions</i> «se ha modificado para contener únicamente definiciones de aquellos términos empleados en la presentación de los conceptos y principios descritos en este documento».",
 "Muchísima documentación de SGSI, material de formación y listas de verificación de auditoría citan la ISO/IEC 27000 como fuente normativa de las definiciones de seguridad de la información, riesgo, control o parte interesada. Esa cita queda huérfana. Quien tenga un cuerpo de políticas o un glosario que diga que se aplican los términos definidos en la ISO/IEC 27000 tiene que reapuntarlo, y ojo, porque <b>la cláusula 3 de la ISO/IEC 27001:2022 remite normativamente a la 27000</b>, de modo que esto cambia silenciosamente a qué resuelve esa remisión.",
 '<a href="https://www.iso.org/standard/27000" @L>ISO/IEC 27000:2026</a>, lista de cambios del prólogo y cláusula 3.',
 "Dónde vive ahora la terminología retirada está sin confirmar: el cuerpo del documento es de pago y no he podido abrirlo. Conviene verificarlo antes de aconsejar a un cliente sobre la fuente terminológica sustitutiva."),

("std", "Acreditación · vigente desde el 1 de enero de 2026", False,
 "IAF e ILAC ya no existen, ha cambiado la fontanería bajo cada certificado ISO 27001",
 "El International Accreditation Forum e ILAC se fusionaron en <b>Global Accreditation Cooperation Incorporated</b>, en plena operación desde el 1 de enero de 2026, con el MLA del IAF y el MRA de ILAC subsumidos en un único MRA de la Cooperación. iaf.nu e ilac.org son ya archivo. Las marcas heredadas siguen siendo válidas durante la transición; se espera una decisión sobre la fecha de lanzamiento de la nueva marca en la <b>Asamblea General de octubre de 2026</b>, y a partir de ese lanzamiento se prevé una retirada progresiva de las antiguas de unos tres años.",
 "El riesgo a corto plazo es prosaico y está muy extendido: <b>plantillas de compras y cuestionarios de riesgo de terceros que fijan la condición de firmante del MLA del IAF como criterio de aceptación.</b> En paralelo y ya vinculante: el plazo final del IAF MD 29 para la ISO/IEC 27006-1:2024 venció el <b>31 de marzo de 2026</b>, y esa norma cambió el cálculo del tiempo de auditoría. Si la entidad de certificación de un cliente sigue presupuestando con las duraciones de la 27006:2015, es una señal de alarma sobre su estado de acreditación.",
 '<a href="https://ilac.org/latest_ilac_news/launch-of-the-global-accreditation-cooperation-incorporated/" @L>Anuncio del lanzamiento</a> y el <a href="https://iaf.nu/iaf_system/uploads/documents/IAF_MD_29_27006-1_Transition_21052024.pdf" @L>calendario de transición del IAF MD 29:2024</a>.',
 "No conviene afirmar un tajante «marcas válidas hasta finales de 2028», porque el reloj de tres años no ha empezado. Qué ocurre formalmente con la serie MD del IAF bajo el nuevo organismo también está sin resolver."),

("std", "ISO · mercado activo en 2026", False,
 "La ISO/IEC 27701:2025 ya es un sistema de gestión autónomo, y la 42001 es realmente certificable",
 "La <b>27701:2025</b> ha pasado de ser una extensión que requería un SGSI 27001 a ser una <b>norma de sistema de gestión independiente</b>, retitulada <i>Privacy information management systems: Requirements and guidance</i>; la edición de 2019 queda anulada. La <b>ISO/IEC 27706:2025</b> sustituye a la TS 27006-2:2021, elevando a Norma Internacional los requisitos para entidades que certifican sistemas de gestión de privacidad. Aparte, la <b>ISO/IEC 42006:2025</b> está publicada y los esquemas de acreditación han arrancado, con la primera acreditación nacional emitida en enero de 2026.",
 "Es el mayor cambio en el alcance certificable de una práctica de SGSI. Clientes que antes no podían perseguir la 27701 sin un SGSI 27001 completo ya pueden, lo que abre encargos autónomos de certificación de privacidad que los compradores movidos por el RGPD empezarán a exigir. Y la 42001 ha pasado de asesoramiento en gobernanza de IA a <b>encargo certificable</b>, típicamente acoplado a un SGSI existente por la estructura común de las cláusulas 4 a 10. Conviene comprobar que la entidad de certificación del cliente está acreditada bajo la 42006, porque proliferan los certificados de IA no acreditados.",
 '<a href="https://www.iso.org/standard/27701" @L>ISO/IEC 27701:2025</a>, cláusulas 4 a 10, y la <a href="https://www.iso.org/standard/42006" @L>ISO/IEC 42006:2025</a> para saber qué exigir a una entidad de certificación.',
 "No he encontrado plazo oficial de transición para los certificados 27701:2019. Los blogs de entidades de certificación hablan de unos tres años; no conviene dar una fecha sin consultar a la entidad y al organismo de acreditación del propio cliente."),

("std", "NIST · novedades de 2026", False,
 "NIST: el AI RMF entra en CPRT y la guía de transición poscuántica sigue en borrador",
 "<b>El AI RMF 1.0 y el NIST AI 100-2 se incorporaron a CPRT</b> en febrero de 2026, lo que hace el AI RMF mapeable por máquina junto al CSF 2.0 y al SP 800-53 por primera vez. El SP 1347, <i>CSF 2.0: Informative References Quick-Start Guide</i>, sigue en borrador público inicial. El SP 800-172r3 y el 172Ar3 se publicaron en versión final el 13 de mayo de 2026. Mientras tanto, el <b>NIST IR 8547</b>, el documento de transición a poscuántica que contiene el calendario propuesto de retirada de RSA y ECC, lleva ya <b>21 meses</b> en estado de borrador público inicial.",
 "CPRT permite construir mapeos entre ISO/IEC 42001, AI RMF y CSF 2.0 a partir de datos mantenidos por el NIST en lugar de a mano, defendible de un modo en que una hoja de cálculo propia no lo es. Lo del IR 8547 es un riesgo vivo: <b>hay clientes citando sus fechas en documentos de consejo y en respuestas sobre resiliencia criptográfica como si estuvieran cerradas.</b> Son borrador. Conviene decirlo, y usar en su lugar las fechas del CCN como ancla española.",
 '<a href="https://csrc.nist.gov/projects/cprt" @L>CPRT</a>, <a href="https://csrc.nist.gov/pubs/sp/1347/ipd" @L>SP 1347 ipd</a> e <a href="https://csrc.nist.gov/pubs/ir/8547/ipd" @L>IR 8547 ipd</a>, marcando bien el estado de borrador en cualquier entregable.',
 None),

("ai", "Reglamento de IA · en vigor el 27 jul 2026", True,
 "El alto riesgo se aplaza al 2 de diciembre de 2027, y el aplazamiento es fecha fija, no condicional",
 "El <b>Reglamento (UE) 2026/1744</b>, el llamado Digital Omnibus on AI, adoptado el 8 de julio de 2026, publicado en el DOUE el 24 de julio y en vigor el 27 de julio, seis días antes del hito que todo el mundo tenía anotado. Las obligaciones del capítulo III se aplican ahora desde el <b>2 de diciembre de 2027</b> para los sistemas de alto riesgo del anexo III (art. 6.2) y desde el <b>2 de agosto de 2028</b> para los integrados en productos del anexo I (art. 6.1). Los nuevos artículos 75 bis a 75 quater otorgan a la Oficina de IA competencia exclusiva sobre sistemas derivados de IA de propósito general y sobre sistemas integrados en plataformas designadas como muy grandes, con multas periódicas de hasta el 5 % del volumen de negocios mundial medio diario.",
 "Toda hoja de ruta de preparación al alto riesgo vendida sobre la base del 2 de agosto de 2026 está desfasada en 16 meses. El riesgo comercial es el inverso del habitual: los clientes que sobreinvirtieron pueden ahora aplazarlo todo y perder el impulso mucho antes de 2027. Hay que rebasar el programa, no pausarlo. Y conviene recordar que las directrices de clasificación siguen en borrador, así que sale barato clasificar provisionalmente ahora y retrasar el cierre de arquitectura y del gasto en evaluación de la conformidad.",
 '<a href="https://eur-lex.europa.eu/eli/reg/2026/1744/oj/spa" @L>Reglamento (UE) 2026/1744</a>, considerando 40 y la modificación del artículo 113, y la <a href="https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act" @L>cronología oficial de la Comisión</a>.',
 "Dos trampas. Primera: las preguntas frecuentes del propio servicio de asistencia de la Comisión están desactualizadas y siguen recogiendo la redacción de la propuesta, según la cual las fechas estarían alineadas con la disponibilidad de normas. Los colegisladores eliminaron ese mecanismo condicional en favor de fechas fijas, y esas FAQ inducirán a error a cualquier cliente que las lea. Segunda: tanto la página del artículo 113 del servicio de asistencia como artificialintelligenceact.eu siguen mostrando el texto sin modificar. Cita el DOUE, no los navegadores de articulado."),

("ai", "Reglamento de IA · exigible desde el 2 de agosto", True,
 "Qué entró realmente en vigor el 2 de agosto, y el plazo de marcado del 2 de diciembre",
 "El Reglamento pasó a ser de aplicación general y <b>arrancó la exigencia</b>: transparencia del artículo 50, con el deber de informar de que se interactúa con una IA, etiquetado de ultrafalsificaciones y marcado legible por máquina de contenido sintético; competencia sancionadora de la Oficina de IA sobre proveedores de modelos de propósito general incluidos los de riesgo sistémico; y exigibilidad de la prohibición de prácticas vedadas. La exigencia se reparte en tres, entre la Oficina de IA, las autoridades nacionales competentes y el SEPD para las instituciones europeas, y la Comisión ha habilitado canales de denuncia, de alertadores y de notificación por proveedores posteriores. Las Directrices definitivas del artículo 50 se publicaron el 20 de julio. <b>Los sistemas ya comercializados antes del 2 de agosto de 2026 tienen hasta el 2 de diciembre de 2026 para cumplir el artículo 50.2.</b>",
 "La maquinaria sancionadora está viva aunque el fondo del alto riesgo no lo esté, así que la exposición a corto plazo es transparencia y prácticas prohibidas, y los nuevos canales de denuncia y alertadores elevan materialmente la probabilidad de una investigación iniciada por un tercero. La fecha de diciembre es un <b>plazo real de ingeniería</b> para el marcado interoperable de contenido, no un trámite de política, para cualquier cliente con chatbots o generación de texto o medios. Y hay que ser claro: firmar el Código de Buenas Prácticas no es un puerto seguro, porque las autoridades de vigilancia del mercado conservan plenas facultades de investigación.",
 '<a href="https://ec.europa.eu/commission/presscorner/detail/es/ip_26_1714" @L>IP/26/1714</a> y las <a href="https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems" @L>Directrices del artículo 50</a>.',
 "No conviene confundir las dos fechas del 2 de diciembre de 2026: el plazo transitorio del artículo 50.2 y, por separado, las nuevas prohibiciones del Omnibus sobre contenido íntimo no consentido y aplicaciones de material de abuso sexual infantil."),

("ai", "CEPD · consulta hasta el 30 de octubre", True,
 "Las directrices del CEPD sobre anonimización imponen un test estricto de tres criterios",
 "Las <b>Directrices 02/2026 sobre anonimización</b> fijan un test de tres criterios: imposibilidad de aislar un registro, de vincularlo y de inferir. Las <b>Directrices 03/2026 sobre web scraping para IA generativa</b> confirman que el RGPD se aplica siempre que el rastreo implique recogida, almacenamiento, organización o consulta de datos personales, con énfasis en las medidas para categorías especiales. Las Directrices 02/2025 sobre cadena de bloques se adoptaron en versión definitiva. Las dos nuevas están en consulta pública <b>hasta el 30 de octubre de 2026</b>.",
 "El test de anonimización es lo bastante estricto como para invalidar buena parte de los conjuntos de datos anonimizados sobre los que los clientes se apoyan para quedar fuera del ámbito del RGPD, <b>incluidos los corpus de entrenamiento reunidos para proyectos de IA</b>. Es una conversación de redefinición de alcance directa e inmediata. La ventana de consulta es además una oportunidad viva para presentar alegaciones en nombre de clientes antes de que el texto cristalice.",
 '<a href="https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf" @L>Directrices 02/2026 sobre anonimización</a> y <a href="https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_2020603_webscraping_v1_en_0.pdf" @L>Directrices 03/2026 sobre web scraping</a>.',
 None),

("ai", "AEPD · publicada el 28 jul 2026", False,
 "La AEPD multa a Flexicar con 680.000 euros: la integración post adquisición como fallo de seguridad del tratamiento",
 "Procedimiento EXP202410832 contra <b>Flexicar Internacional S.L.</b>: <b>400.000 euros por el artículo 5.1.f)</b> de integridad y confidencialidad, <b>250.000 por el artículo 32</b> de seguridad del tratamiento y <b>30.000 por el artículo 13</b>. Un incidente de 2024 expuso datos personales procedentes de formularios de contacto de la web, meses después de que Flexicar absorbiera a Flexicar Ibérica, integración que «amplió el perímetro de exposición». La AEPD apreció que no se habían implantado medidas de seguridad que la compañía solo adoptó tras la brecha, y que los registros de clientes bloqueados estaban mezclados con los activos sin segregación lógica.",
 "El precedente español más citable del periodo, y toca dos temas vendibles. Primero, la doctrina explícita de la AEPD de que <b>sufrir un ciberataque no exime de responsabilidad</b> cuando faltaban medidas preventivas, usando la remediación posterior al incidente como prueba de la carencia previa. Segundo, <b>la integración en operaciones corporativas como exposición del artículo 32</b>, que es un buen gancho para trabajo de apoyo en transacciones. Fíjate en que la sanción del 5.1.f) supera a la del 32: la AEPD está tratando el principio de confidencialidad como el cargo más grave, lo que cambia cómo plantear las estimaciones de exposición.",
 'La resolución EXP202410832 en la base de resoluciones de la AEPD. Merece emparejarse con las <i>Orientaciones sobre IA agéntica</i> de la AEPD, de febrero de 2026, cuyo enfoque de vulnerabilidades y amenazas encaja bien con las evaluaciones del artículo 32.',
 "El 28 de julio es la fecha de publicación en prensa, no una fecha de resolución verificada: aepd.es bloquea el acceso automatizado, así que el desglose por artículos procede de prensa jurídica española y no del texto de la resolución. Conviene leer el original antes de citar su razonamiento. Se desconoce si ha sido recurrida."),

("thr", "Exposición · principios de agosto de 2026", True,
 "Elusión de autenticación en N-able N-central: un compromiso de RMM es problema NIS2 y del artículo 28",
 "<b>CVE-2026-18556</b> y <b>CVE-2026-18577</b>, ambas CVSS 8.2, son elusiones de autenticación que conceden acceso administrativo a servidores N-central; la segunda se emitió porque la primera corrección era incompleta. Resueltas en 2026.3 HF1. Un número limitado de clientes resultó comprometido: los atacantes usaron el nombre de usuario por defecto «MSP Support» para sesiones de Take Control y a continuación hicieron reconocimiento de controlador de dominio y movimiento lateral. Entre los indicadores, un svchost.exe sospechoso en carpetas de Documentos y un servicio registrado como «Cloudflared».",
 "El compromiso de una plataforma RMM se propaga de una brecha a toda una cartera de clientes gestionados. Para clientes españoles y europeos es a la vez un asunto de <b>cadena de suministro NIS2</b> y de <b>aseguramiento del encargado del tratamiento del artículo 28 del RGPD</b>: si el proveedor de servicios gestionados de tu cliente usa N-central, es tu cliente quien soporta la obligación de notificación. La corrección incompleta es la lección operativa: verificar la versión en ejecución y no fiarse solo del aviso del fabricante.",
 'La entrada del catálogo KEV de CISA y el aviso de N-able. También con explotación activa en el periodo: CVE-2026-9198 (Langflow, ejecución remota, CVSS 9.8), CVE-2026-34486 (Apache Tomcat), CVE-2026-8037 (Progress LoadMaster, EPSS 99 %), CVE-2026-72898 (Metabase, CVSS 10.0), CVE-2026-63077 (JetBrains TeamCity), CVE-2026-68820 (elevación de privilegios en Windows) y CVE-2026-20349 (Cisco Secure Firewall).',
 "cisa.gov bloquea el acceso desde este entorno, así que las fechas de incorporación al KEV proceden de réplicas y podrían desviarse un día. Conviene confirmarlas contra el catálogo antes de circular una lista."),

("thr", "Tecnología operativa y NIS2 · del 2 de julio al 12 de agosto", False,
 "Racha densa de avisos industriales del INCIBE-CERT y tres alertas del CCN-CERT sobre dispositivos perimetrales",
 "El INCIBE-CERT publicó una secuencia sostenida de avisos sobre sistemas de control industrial: <b>Balluff</b>, 20 críticas el 2 de julio; <b>ABB</b>, 7 críticas el 7 de julio; <b>OpenPLC v3</b>, ejecución remota crítica el 11 de julio; <b>WAGO</b>, acceso remoto no autenticado durante el arranque el 14 de julio; <b>Rockwell Automation</b>, 19 críticas el 16 de julio; <b>Mitsubishi Electric MELSEC</b> el 31 de julio; y <b>Bosch BSH ELP</b> el 2 de agosto. El CCN-CERT emitió las alertas AL 05/26 y AL 06/26 el 17 de julio, sobre ejecución remota en Microsoft Exchange y SonicWall SMA1000, y AL 07/26 el 22 de julio, sobre SharePoint.",
 "Individualmente son rutina; en conjunto son señal. La concentración en fabricantes de tecnología operativa es base defendible para priorizar un encargo de <b>inventario de activos OT y gobierno del parcheo</b> con clientes españoles de industria, utilities y logística en ámbito NIS2, porque será tema de inspección. Los niveles de alerta del CCN-CERT además disparan obligaciones de respuesta para entidades en ámbito ENS y son la referencia estándar en los análisis posteriores a incidente en España.",
 '<a href="https://www.incibe.es/incibe-cert" @L>Avisos del INCIBE-CERT</a> e <a href="https://www.ccn.cni.es/es/actualidad-ccn" @L>índice de actualidad del CCN</a>.',
 None),
]

BULOS = [
 ("«Ya ha salido la ISO 27001:2026.»",
  "Falso. La ISO/IEC 27001 sigue siendo <b>edición 3, publicada el 25 de octubre de 2022, en estado 60.60</b>, con una única enmienda, la Amd 1:2024 sobre acción climática. La ISO/IEC 27002 también sigue en edición 3 con 93 controles en cuatro temas. La confusión viene casi con seguridad de la <b>ISO/IEC 27000:2026</b>, que sí se publicó el 3 de julio y es otra norma distinta. Hay que corregir la inferencia, no necesariamente la fuente: parte de ese contenido es correcto y solo está mal titulado."),
 ("«El aplazamiento del alto riesgo del Reglamento de IA está condicionado a que estén listas las normas armonizadas.»",
  "Eso era la propuesta. Los colegisladores eliminaron el disparador condicional y lo sustituyeron por fechas de calendario fijas. Varias notas de despachos, y las propias FAQ desactualizadas de la Comisión, siguen describiendo el mecanismo condicional. Quien construya una hoja de ruta sobre esa base se apoya en una disposición que no existe en el texto adoptado."),
 ("«España tiene un plazo de registro NIS2 en 2026.»",
  "Ninguna fuente primaria lo sostiene. No hay ley española de NIS2, ni registro de entidades, ni régimen sancionador: siguen rigiendo el RDL 12/2018 y el RD 43/2021. Varios blogs de consultoría bien posicionados afirman plazos y cuantías de multa de 2026 como si estuvieran en vigor. La demanda de la Comisión del 8 de julio es la refutación más limpia."),
 ("«Las sanciones del Reglamento de IA empiezan en agosto de 2026.»",
  "Un año de desfase. El capítulo XII sobre sanciones y la sección 4 del capítulo III sobre autoridades notificantes se aplican desde el <b>2 de agosto de 2025</b>. A cualquier cliente al que le hayan dicho otra cosa le han asesorado mal."),
 ("«La certificación ISO/IEC 42001 acredita el cumplimiento del Reglamento de IA.»",
  "No lo hace. La 42001 certifica gobernanza organizativa de la IA; el Reglamento exige conformidad de producto por sistema. La <b>prEN 18286</b>, primera norma armonizada específica de IA del CEN-CENELEC JTC 21, operacionaliza el artículo 17 sobre sistema de gestión de la calidad y no cubre el <b>artículo 15</b> sobre precisión, robustez y ciberseguridad, que a día de hoy no tiene ninguna norma armonizada. La 42001 es un acelerador real vía auditorías integradas, no un sustituto."),
 ("«Comprueba que el certificado sea de un firmante del MLA del IAF.»",
  "Obsoleto desde el 1 de enero de 2026. El IAF ya no opera y el MLA está subsumido en el MRA de la Global Accreditation Cooperation. Las marcas heredadas circularán en paralelo durante años, así que es cuestión de higiene documental más que de urgencia, pero las plantillas de compras que fijan IAF conviene actualizarlas."),
]

SILENCIO = [
 ("El propio ENS y el RD 311/2022", "el texto consolidado del BOE se actualizó por última vez el 6 de noviembre de 2024, y la única modificación que consta es el RD 1125/2024. Sin enmiendas, sin nuevo plazo de conformidad, sin nota interpretativa."),
 ("Nuevas Instrucciones Técnicas de Seguridad", "ninguna en 2026. Siguen vigentes la ITS de Conformidad de 2016 y las de Auditoría y de Notificación de Incidentes de 2018."),
 ("Nuevos Perfiles de Cumplimiento Específico", "ninguno confirmado. El conjunto existente, 890 UCEENS, 891 Salud y 892 NIS2, parece sin cambios, con confianza media porque ccn-cert.cni.es bloquea el acceso automatizado."),
 ("Nuevas normas técnicas de DORA en el DOUE", "ninguna identificada en el periodo. Confianza media, porque EUR-Lex bloquea la consulta automatizada y merece la pena una comprobación manual."),
 ("Nuevas designaciones de proveedores TIC críticos", "la lista sigue siendo la cohorte de 19 proveedores del 18 de noviembre de 2025. Un anuncio del ciclo 2026 es plausible en el cuarto trimestre."),
 ("Pruebas dirigidas por amenazas y TIBER-EU", "sin nueva orientación del BCE; el conjunto de 2025 está sin cambios. Sin actualización de TIBER-ES por el Banco de España."),
 ("Banco de España y CNMV", "sin publicaciones nuevas sobre DORA en el periodo. Lo más reciente es la Memoria de Supervisión 2025 del BdE, de abril, y las preguntas frecuentes de DORA de la CNMV, de febrero."),
 ("Consultas abiertas de las AES sobre DORA o resiliencia TIC", "ninguna. Las líneas actuales son indicadores de taxonomía, valoración IRRD, sanciones MiCA y estructura de mercados de renta variable."),
 ("EUCS y EUCC", "sin movimiento. EUCS sigue bloqueado por los requisitos de soberanía."),
 ("Grupo de Cooperación NIS", "sin nueva orientación confirmada; la página de la Comisión se actualizó por última vez el 11 de junio de 2026. Su biblioteca de publicaciones bloquea el acceso automatizado, así que no puede descartarse un documento de julio no listado."),
 ("Panorama de amenazas de ENISA", "el ETL 2026 no se ha publicado, y suele salir en octubre. Sigue vigente el ETL 2025."),
 ("Guía técnica de implementación de NIS2 de ENISA", "sigue en versión 1.0 de junio de 2025. Su tabla de correspondencias con ISO/IEC 27001 y 27002 continúa siendo el mejor mapeo gratuito de NIS2 disponible."),
 ("NIST SP 800-53 y SP 800-171", "sin publicación en 2026; el último parche del catálogo sigue siendo el 5.2.0 de agosto de 2025. No se ha anunciado revisión 4 de la 800-171, y el Privacy Framework 1.1 sigue sin ser definitivo."),
 ("Nuevas guías de la AEPD", "ninguna identificada en el periodo más allá de la resolución de Flexicar."),
 ("Hitos operativos de la AESIA", "sin decisión de designación, sin convocatoria de sandbox y sin actividad sancionadora. Sus competencias formales siguen supeditadas a la Ley Orgánica pendiente, aprobada en Consejo de Ministros el 26 de mayo de 2026."),
]

TITULAR = "Bruselas lleva a España al Tribunal de Justicia por NIS2, y con dinero encima de la mesa"
ENTRADA = "El silencio regulatorio del verano español es engañoso. La Comisión ha demandado a España pidiendo multa coercitiva diaria, el reglamento de ciberresiliencia empieza a exigir notificaciones en cuatro semanas, y el BCE ha puesto fecha a los planes de acción frente a la amenaza potenciada por IA."
CLAVE_1 = "El <b>8 de julio de 2026</b> la Comisión llevó a España ante el Tribunal de Justicia por no transponer NIS2, y lo hizo <b>solicitando una suma a tanto alzado más multas coercitivas diarias</b> hasta que se notifique la transposición completa. España sigue sin ley: el <i>Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad</i> no ha llegado al BOE y no consta ningún Proyecto de Ley con ese título en el Congreso."
CLAVE_2 = "La consecuencia práctica para tus encargos: se acabó el «estamos esperando a la ley española». La presión económica ha comprimido históricamente los calendarios legislativos españoles, lo que significa que los clientes tendrán un margen corto entre publicación y aplicabilidad. Hay que construir ya sobre los artículos 20 a 23 de la Directiva y sobre la CCN-STIC 892."

def check_dashes():
    """Aborta si queda algun guion largo en el contenido."""
    blobs = [TITULAR, ENTRADA, CLAVE_1, CLAVE_2]
    for it in ITEMS:
        blobs += [str(x) for x in it if isinstance(x, str)]
    for p in PLAZOS:
        blobs += [p[0], p[2], p[3]]
    for b in BULOS: blobs += list(b)
    for s in SILENCIO: blobs += list(s)
    bad = [b for b in blobs if re.search(r"[–—‒―]", b)]
    if bad:
        raise SystemExit("GUION LARGO detectado en: " + bad[0][:120])
    print("Sin guiones largos: OK")

check_dashes()

# ══════════════════════ 1. VERSION PANTALLA ══════════════════════
sec_vars = "\n".join(
    f"    --{k}:{v[0]}; --{k}-t:{v[1]};" for k, v in SEC.items())
sec_vars_dark = "\n".join(
    f"    --{k}:{SEC_DARK[k]}; --{k}-t:{SEC[k][2]};" for k in SEC)

p = []
W = p.append
W(f'''<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Briefing Ciber-GRC · España y UE · 13 de agosto de 2026</title>
<style>
:root{{
  --bg:#f6f3ee; --paper:#fffdf9; --ink:#16181b; --ink2:#474d55; --ink3:#787f88;
  --rule:#ded8ce; --hair:#efeae2; --hot:{HOT}; --hot-t:{HOTBG};
{sec_vars}
  --ser:{SER}; --san:{SAN};
}}
@media (prefers-color-scheme:dark){{
  :root{{
    --bg:#101113; --paper:#191b1e; --ink:#eef0f3; --ink2:#b6bcc4; --ink3:#878e97;
    --rule:#2e3238; --hair:#212429; --hot:#F0857C; --hot-t:#331d1c;
{sec_vars_dark}
  }}
}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);font:17px/1.62 var(--ser);
     font-feature-settings:"kern","liga"}}
.page{{max-width:880px;margin:0 auto;padding:0 22px 110px}}
.stripe{{display:flex;height:6px;margin:0 -22px}}
.stripe i{{flex:1}}
.flag{{display:flex;justify-content:space-between;align-items:baseline;gap:16px;
  font:600 10.5px/1 var(--san);letter-spacing:.2em;text-transform:uppercase;color:var(--ink3);
  padding:26px 0 13px;border-bottom:1px solid var(--ink)}}
h1{{font:600 clamp(30px,5.6vw,48px)/1.09 var(--ser);letter-spacing:-.02em;margin:26px 0 0;text-wrap:balance}}
.lede{{font:400 clamp(17px,2.1vw,19.5px)/1.55 var(--ser);color:var(--ink2);margin:18px 0 0;max-width:58ch}}
.byline{{display:flex;flex-wrap:wrap;gap:6px 20px;margin:24px 0 0;padding:13px 0;
  border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);
  font:500 11.5px/1.4 var(--san);letter-spacing:.04em;color:var(--ink3)}}
.byline b{{color:var(--ink2);font-weight:600}}
.sumario{{display:grid;grid-template-columns:repeat(auto-fit,minmax(212px,1fr));gap:2px;margin:22px 0 0}}
.sumario a{{display:block;padding:15px 16px;text-decoration:none;color:inherit;border-radius:3px}}
.sumario .n{{font:700 9.5px/1 var(--san);letter-spacing:.15em;display:block;margin-bottom:7px}}
.sumario .t{{font:400 14.5px/1.35 var(--ser);color:var(--ink2)}}
.sumario a:hover .t{{color:var(--ink)}}
.clave{{border-radius:3px;padding:28px 30px;margin:30px 0 0;border-left:5px solid var(--es);background:var(--es-t)}}
.clave .et{{font:700 10px/1 var(--san);letter-spacing:.19em;text-transform:uppercase;color:var(--es);margin:0 0 13px}}
.clave p{{margin:0 0 12px;font-size:17.5px}} .clave p:last-child{{margin-bottom:0}}
.plazos{{margin:44px 0 0}}
.plazos .et{{font:700 10.5px/1 var(--san);letter-spacing:.19em;text-transform:uppercase;color:var(--ink3);margin:0}}
.plazos .sub{{font:400 14.5px/1.5 var(--ser);color:var(--ink3);margin:9px 0 16px}}
.plazos table{{width:100%;border-collapse:collapse}}
.plazos th{{text-align:left;font:700 9.5px/1 var(--san);letter-spacing:.15em;text-transform:uppercase;
  color:var(--ink3);padding:0 14px 9px 0;border-bottom:2px solid var(--ink)}}
.plazos td{{padding:12px 14px 12px 0;border-bottom:1px solid var(--hair);vertical-align:top}}
.plazos td.f{{white-space:nowrap;font:600 14px/1.45 var(--san);width:1%}}
.plazos td.q{{font-size:16px}}
.plazos td.a{{color:var(--ink3);font:400 13.5px/1.45 var(--san)}}
.plazos tr.u td{{background:var(--hot-t)}}
.plazos tr.u td.f{{color:var(--hot);font-weight:700;padding-left:12px}}
.seccion{{margin:60px 0 0;scroll-margin-top:16px}}
.cab{{display:flex;align-items:center;gap:12px;padding:13px 18px;border-radius:3px}}
.cab h2{{font:700 11.5px/1.3 var(--san);letter-spacing:.16em;text-transform:uppercase;margin:0;color:#fff}}
.cab .cnt{{margin-left:auto;font:600 10.5px/1 var(--san);letter-spacing:.1em;color:rgba(255,255,255,.72);white-space:nowrap}}
.intro{{font:400 15.5px/1.55 var(--ser);color:var(--ink3);margin:15px 0 0;max-width:62ch}}
.noticia{{padding:32px 0 8px;border-bottom:1px solid var(--hair)}}
.noticia:last-child{{border-bottom:none}}
.marcas{{display:flex;flex-wrap:wrap;gap:9px;align-items:center;margin-bottom:12px}}
.pri{{font:700 9.5px/1 var(--san);letter-spacing:.12em;text-transform:uppercase;padding:6px 9px;border-radius:2px}}
.meta{{font:600 11.5px/1.5 var(--san);letter-spacing:.04em;color:var(--ink3)}}
.noticia h3{{font:600 clamp(21px,2.8vw,25px)/1.25 var(--ser);letter-spacing:-.012em;margin:0 0 15px;text-wrap:balance}}
.et{{font:700 9.5px/1 var(--san);letter-spacing:.16em;text-transform:uppercase;display:block;margin:0 0 6px}}
.campo{{margin:0 0 16px}} .campo p{{margin:0}}
.campo.porque{{border-radius:3px;padding:15px 17px}}
.campo.porque p{{color:var(--ink2)}}
.leer{{background:var(--paper);border:1px solid var(--rule);border-radius:3px;padding:14px 16px;margin:0 0 4px}}
.leer p{{margin:0;font-size:15px;color:var(--ink2)}}
.leer a{{text-decoration:underline;text-underline-offset:2.5px;font-weight:600}}
.aviso{{margin:12px 0 0;padding:0 0 0 14px;border-left:3px solid var(--rule);
  font:400 14.5px/1.55 var(--ser);color:var(--ink3)}}
.bloque{{border-radius:3px;padding:30px 32px;margin:34px 0 0}}
.bloque>.et{{margin-bottom:8px}}
.bloque>.sub{{font:400 15px/1.5 var(--ser);color:var(--ink3);margin:0 0 22px}}
.bulo{{margin:0 0 18px;padding-bottom:18px;border-bottom:1px solid var(--rule)}}
.bulo:last-child{{margin-bottom:0;padding-bottom:0;border-bottom:none}}
.bulo .f{{font:600 16.5px/1.4 var(--ser);margin:0 0 7px}}
.bulo .x{{color:var(--hot);font:700 14px/1 var(--san);margin-right:9px}}
.bulo p{{margin:0;font-size:15.5px;color:var(--ink2)}}
.sil p{{margin:0;padding:10px 0;border-bottom:1px solid var(--rule);font-size:15.5px;color:var(--ink2)}}
.sil p:last-child{{border-bottom:none}}
footer{{margin-top:56px;padding-top:24px;border-top:3px solid var(--ink)}}
footer p{{margin:0 0 12px;font:400 13.5px/1.6 var(--san);color:var(--ink3)}}
footer b{{color:var(--ink2);font-weight:600}}
.cierre{{margin-top:20px;padding:14px 18px;border-radius:3px;background:var(--eu-t);
  font:700 11px/1 var(--san);letter-spacing:.16em;text-transform:uppercase;color:var(--eu)}}
code{{font:500 13px/1 ui-monospace,Menlo,monospace;background:var(--hair);padding:2px 5px;border-radius:2px}}
@media(max-width:620px){{.clave,.bloque{{padding:22px 20px}} .plazos td.a{{display:none}}}}
</style></head><body><div class="page">
<div class="stripe">''')
for k in SEC:
    W(f'<i style="background:var(--{k})"></i>')
W(f'''</div>
<div class="flag"><span>Briefing Ciber-GRC · España y Unión Europea</span><span>Ed. 001 · 13.08.2026</span></div>
<h1>{TITULAR}</h1>
<p class="lede">{ENTRADA}</p>
<p class="byline"><span><b>Periodo cubierto</b> del 1 de julio al 13 de agosto de 2026</span>
<span><b>Cerrado</b> jueves 13 de agosto de 2026</span>
<span><b>18 asuntos</b> y <b>10 plazos vivos</b></span></p>
<nav class="sumario">''')
SUM = [("es","01 · ESPAÑA","El CCN obliga a autoevaluarse en IA ofensiva antes del 15 de septiembre"),
       ("eu","02 · UNIÓN EUROPEA","El CRA empieza a exigir notificación de vulnerabilidades explotadas"),
       ("fin","03 · FINANCIERO","España por fin activa el régimen sancionador de DORA"),
       ("std","04 · NORMAS","Dos normas ISO republicadas en julio, y ninguna es la 27001"),
       ("ai","05 · IA Y DATOS","El aplazamiento del alto riesgo es fecha fija, no condicional"),
       ("thr","06 · AMENAZA","Compromiso de plataforma RMM: problema NIS2 y del artículo 28")]
for k, n, t in SUM:
    W(f'<a href="#{k}" style="background:var(--{k}-t)"><span class="n" style="color:var(--{k})">{n}</span><span class="t">{t}</span></a>')
W(f'''</nav>
<div class="clave"><p class="et">Lo único que hay que retener</p><p>{CLAVE_1}</p><p>{CLAVE_2}</p></div>
<section class="plazos"><p class="et">Plazos vivos</p>
<p class="sub">Cuatro vencen antes de octubre. Los resaltados caen dentro de los próximos 35 días.</p>
<table><thead><tr><th>Fecha</th><th>Qué vence</th><th>A quién obliga</th></tr></thead><tbody>''')
for f, urg, q, a in PLAZOS:
    W(f'<tr class="{"u" if urg else ""}"><td class="f">{f}</td><td class="q">{q}</td><td class="a">{a}</td></tr>')
W('</tbody></table></section>')

cur = None
counts = {}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1
for sec, marcas, urg, tit, cambio, porque, leer, aviso in ITEMS:
    if sec != cur:
        if cur: W('</section>')
        cur = sec
        W(f'''<section class="seccion" id="{sec}">
<div class="cab" style="background:var(--{sec})"><h2>{SEC[sec][3]}</h2><span class="cnt">{counts[sec]} asuntos</span></div>''')
    pri = f'<span class="pri" style="background:var(--{sec});color:#fff">Prioritario</span>' if urg else ''
    W(f'''<article class="noticia">
<div class="marcas">{pri}<span class="meta">{marcas}</span></div>
<h3>{tit}</h3>
<div class="campo"><span class="et" style="color:var(--{sec})">Qué ha cambiado</span><p>{cambio}</p></div>
<div class="campo porque" style="background:var(--{sec}-t)"><span class="et" style="color:var(--{sec})">Por qué importa</span><p>{porque}</p></div>
<div class="leer"><span class="et" style="color:var(--{sec})">Qué leer</span><p>{leer.replace("@L", f'style="color:var(--{sec})"').replace("%%", "%")}</p></div>''')
    if aviso: W(f'<p class="aviso" style="border-left-color:var(--{sec})">{aviso}</p>')
    W('</article>')
W('</section>')

W(f'''<div class="bloque" style="background:var(--hot-t)">
<span class="et" style="color:var(--hot)">Correcciones</span>
<p class="sub">Afirmaciones que circulan y conviene desmontar en cuanto aparezcan en una reunión.</p>''')
for f, t in BULOS:
    W(f'<div class="bulo"><p class="f"><span class="x">&#10007;</span>{f}</p><p>{t}</p></div>')
W('</div>')

W(f'''<div class="bloque sil" style="background:var(--fin-t)">
<span class="et" style="color:var(--fin)">Comprobado y sin novedad</span>
<p class="sub">Para poder decírselo a un cliente con seguridad, y no por ausencia de búsqueda.</p>''')
for b, t in SILENCIO:
    W(f'<p><b style="color:var(--ink)">{b}</b>: {t}</p>')
W('</div>')

W(f'''<footer>
<p><b>Método.</b> Elaborado a partir de fuentes primarias siempre que han sido accesibles: EUR-Lex, digital-strategy.ec.europa.eu, ENISA, Supervisión Bancaria del BCE, JERS, EBA, ESMA, EIOPA, CEPD, ccn.cni.es, BOE, Congreso de los Diputados, iso.org y csrc.nist.gov. Cada plazo de la tabla se ha reverificado de forma independiente contra su fuente primaria antes de publicar.</p>
<p><b>Limitaciones de acceso de esta edición.</b> <code>ccn-cert.cni.es</code>, <code>aepd.es</code> y <code>cisa.gov</code> bloquean el acceso automatizado desde este entorno, y el texto completo de EUR-Lex falla con frecuencia. Los asuntos que dependen de esas fuentes llevan una advertencia explícita en lugar de una confianza silenciosa.</p>
<p class="cierre">Próxima edición · lunes 17 de agosto de 2026 · 07:00 CET</p>
</footer></div></body></html>''')

with open("/home/claude/briefing-ciber-grc.html", "w", encoding="utf-8") as fh:
    fh.write("\n".join(p))

