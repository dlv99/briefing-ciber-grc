# -*- coding: utf-8 -*-
"""Contenido de la edición. Se reescribe entero cada lunes.
Reglas: nada de guiones largos ni medios, cifras calculadas, % directo.
"""
from contador import CER, NIS2, dias, tanto_alzado, eur, millones, resumen

R = resumen()
CER_DIAS = R["cer"]["dias"]
CER_EUR = R["cer"]["tanto_alzado_eur"]
CER_MILL = R["cer"]["tanto_alzado_millones"]
CER_SEMANA = eur(CER["diario"] * 7, 2)
CER_DIARIO = eur(CER["diario"], 2)
CER_MINIMO = eur(CER["minimo"])
CER_COERC = eur(CER["coercitiva"], 2)

# ══════════ PALETA (no cambia) ══════════
SER = "Georgia,'Times New Roman',serif"
SAN = "Helvetica,Arial,sans-serif"

# (color, fondo, oscuro, titulo de seccion)
SEC = {
 "es":  ("#C62828", "#FDECEA", "#3A1A18", "01. España: ENS, CCN y normativa nacional"),
 "eu":  ("#1565C0", "#E8F1FB", "#152534", "02. Unión Europea: regulación horizontal"),
 "fin": ("#00796B", "#E3F2F0", "#122B29", "03. Sector financiero: DORA y supervisores"),
 "std": ("#6A1B9A", "#F4E9F8", "#261830", "04. Normas y marcos de referencia"),
 "ai":  ("#E65100", "#FDEEE2", "#33200F", "05. Reglamento de IA, datos y sanciones"),
 "thr": ("#AD1457", "#FCE9F1", "#331522", "06. Amenaza y exposición"),
}
SEC_DARK = {"es":"#F08A80","eu":"#7FB0F5","fin":"#4FC9B8","std":"#C39BF0","ai":"#F2A25C","thr":"#F08BB4"}

HOT = "#C62828"
HOTBG = "#FDECEA"

NUM        = 11
FECHA_ISO  = "2026-11-02"
FECHA_TXT  = "2 de noviembre de 2026"
PERIODO    = "del 26 de octubre al 1 de noviembre de 2026"

TITULAR = ("El plazo del Banco Central Europeo para los planes contra la ciberamenaza potenciada por IA "
           "venció el sábado, y la misma semana demostró el argumento: PHP ya se estaba explotando cuatro "
           "días antes de que existiera el parche")

ENTRADA = ("Dos relojes que nadie había puesto en hora juntos coincidieron esta semana. El <b>31 de octubre</b> "
           "venció el plazo que el <b>BCE</b> dio en julio a las entidades significativas para remitir su plan de "
           "acción frente a la ciberamenaza potenciada por IA, cuyo argumento era que los modelos de frontera "
           "<b>acortan el tiempo entre descubrir una vulnerabilidad y explotarla</b>. En esos mismos siete días, "
           "las dos vulnerabilidades críticas de <b>PHP</b> pasaron de parcheadas a <b>explotación activa "
           "confirmada por el fabricante</b> sobre interfaces de administración expuestas a Internet, entraron el "
           "26 de octubre en el catálogo estadounidense de vulnerabilidades explotadas con tres días de plazo, y "
           "el INCIBE-CERT documentó que <b>el primer intento de explotación es del 17 de octubre, cuatro días "
           "antes de la divulgación pública y de las correcciones</b>. La tesis del supervisor se verificó sola. "
           "Y en incidentes, el mayor robo de criptoactivos de la historia: <b>6.300 millones de dólares</b> a "
           "<b>Binance</b> el 29 de octubre, confirmado por la entidad y atribuido por el <b>FBI</b>, que "
           "empezó en el portátil de un ingeniero y que <b>no disparó ni una notificación europea</b>, porque "
           "la entidad no figura en el registro de criptoactivos de la <b>ESMA</b> y queda por tanto fuera de "
           "<b>DORA</b>. En España, con las Cortes disueltas, la producción normativa siguió en cero y el "
           "movimiento real fue del <b>CCN</b>; el único plazo normativo duro es un dictamen urgente del "
           "Consejo de Estado que vence el jueves.")

CLAVE_1 = ("La primera clave es una coincidencia que conviene saber contar, porque es el mejor argumento "
           "disponible para justificar un presupuesto de gestión de vulnerabilidades. El <b>7 de julio de "
           "2026</b>, en la carta <b>SSM-2026-0301</b> firmada por la presidenta del Consejo de Supervisión, el "
           "<b>BCE</b> pidió a cada entidad significativa un plan de acción frente a la ciberamenaza potenciada "
           "por IA, a remitir a su <b>JST</b> «a más tardar el 31 de octubre de 2026». Ese plazo venció el "
           "sábado, dentro de esta ventana. El día anterior, el <b>30 de octubre</b>, un miembro del Consejo de "
           "Supervisión, Pedro Machado, lo explicó en una entrevista con una frase que vale como tesis "
           "supervisora: los modelos de IA de frontera «cambian el paradigma en materia de ciberseguridad, "
           "porque acortan el tiempo entre el descubrimiento de una vulnerabilidad y su explotación», y «el "
           "mayor reto de las entidades hoy es poner en marcha ejercicios de parcheo muy rápidos y eficaces». "
           "Pues bien: en esos mismos siete días, el <b>INCIBE-CERT</b> publicó que el primer intento de "
           "explotación de las dos vulnerabilidades críticas de PHP «se remonta al 17 de octubre, cuatro días "
           "antes de la divulgación pública y de las correcciones». No es una hipótesis de laboratorio: es el "
           "intervalo en negativo. Quien tenía el activo expuesto fue atacado antes de que el parche existiera, "
           "y por eso la única defensa que funcionó en esa franja no fue parchear, sino <b>no tener la interfaz "
           "de administración mirando a Internet</b>. Palo Alto Networks lo ha cuantificado en su propio boletín "
           "y es la cifra más rentable de la semana: la misma vulnerabilidad vale <b>9,2 crítica</b> si la "
           "administración es accesible desde Internet y <b>5,2 media</b> si solo la alcanza un equipo puente.")

CLAVE_2 = ("La segunda clave es española y es de ausencia verificada, que esta semana por fin se ha podido "
           "cerrar con fuente primaria. El boletín venía arrastrando desde la edición 008 el estado de los "
           "proyectos de ley caducados sin poder reconfirmarlo, porque la ficha del Congreso no responde al "
           "acceso automatizado. Esta semana se ha alcanzado por otra ruta el listado completo de proyectos de "
           "ley de la legislatura y el resultado es categórico: son <b>115 expedientes</b>, del 121/000001 al "
           "121/000115, <b>los 115 con autor «Gobierno»</b>, de los cuales <b>89 figuran «Concluido - "
           "(Caducado)»</b>. Entre ellos, el <b>121/000088, «Proyecto de Ley de protección y resiliencia de las "
           "entidades críticas»</b>, que era la transposición de <b>CER</b>, presentado el 18 de marzo de 2026 y "
           "caducado; el <b>121/000105</b>, de digitalización y modernización del sector financiero, que era el "
           "vehículo de <b>DORA</b>; y el <b>121/000096</b>, la ley orgánica de gobernanza de la IA. Y el dato "
           "que importa de verdad: <b>barridos los 115 títulos, no existe ni un solo proyecto de ley de "
           "transposición de NIS2 en toda la legislatura</b>. Conviene medir la diferencia antes de repetirla "
           "ante un cliente, porque no son dos incumplimientos iguales: en CER hubo proyecto, llegó al Congreso "
           "y murió con la disolución, de modo que la legislatura siguiente tiene un texto del que partir; en "
           "NIS2 <b>nunca hubo texto</b>, y eso convierte el cero español de NIS2 en estructuralmente peor. "
           "Súmese que el contador de CER ya va por {dias} días y {eur} euros de lo pedido a tanto alzado, y "
           "queda explicado por qué un real decreto-ley es el escenario probable en cuanto haya gobierno.").format(
           dias=CER_DIAS, eur=CER_EUR)

# (fecha texto, vivo, qué vence, a quién afecta)
PLAZOS = [
 ("2 nov 2026", True, "Vence hoy el plazo del catálogo de vulnerabilidades explotadas para "
  "CVE-2026-111357, de Ivanti Connect Secure, que el fabricante declara explotada en cadena con otras dos; "
  "entró el 30 de octubre",
  "Cualquier organización con la pasarela Ivanti Connect Secure en el perímetro, muy habitual en gran empresa "
  "y administración"),
 ("2 nov 2026", True, "Vence hoy la consulta EBA/CP/2026/16, sobre el reporte para la validación y el "
  "seguimiento del modelo estándar inicial del sector de derivados. No es de DORA",
  "Entidades con cartera de derivados sujetas a requisitos de margen"),
 ("2 nov 2026", True, "Termina hoy, según la propia ciudad, el régimen de emergencia de Eichstätt, tras tres "
  "semanas de administración municipal paralizada por un cifrado de servidores",
  "Nadie en España de forma directa; sirve como medida real de cuánto dura una recuperación con copias "
  "correctas pero contaminadas"),
 ("3 nov 2026", True, "Vence el plazo del catálogo de vulnerabilidades explotadas para CVE-2026-110936, en "
  "Siemens Software Center, que entró el 20 de octubre",
  "Industria con base instalada de software de ingeniería de Siemens, que en España es amplia"),
 ("4 nov 2026", True, "Cierra a las 23:59 la consulta pública previa del Ministerio para la Transformación "
  "Digital sobre la propuesta de reglamento europeo de entornos digitales fiables para menores, el llamado EU "
  "Kids Act, que se apoya en el Reglamento de Servicios Digitales y en el Reglamento de IA",
  "Plataformas, tiendas de aplicaciones, proveedores de IA conversacional y sector de tecnología educativa"),
 ("5 nov 2026", True, "Fecha límite del dictamen urgente que el Consejo de Ministros pidió el 27 de octubre a "
  "la Comisión Permanente del Consejo de Estado sobre el proyecto de real decreto de requisitos de "
  "sostenibilidad energética, medioambiental y de <b>resiliencia y soberanía digital</b> en centros de datos",
  "Operadores de centros de datos, proveedores de alojamiento y de nube, y sus clientes con requisitos de "
  "localización del dato"),
 ("7 nov 2026", True, "Cierra a las 24:00 la consulta pública previa sobre las bases reguladoras de las ayudas "
  "para la contratación de banda ancha fija, los bonos de conectividad",
  "Operadores de telecomunicaciones y beneficiarios potenciales"),
 ("8 nov 2026", True, "Entra en vigor la Circular 1/2026 de la Autoridad Catalana de Protección de Datos sobre "
  "videovigilancia, veinte días después de su publicación en el Diario Oficial de la Generalitat. Deroga la "
  "Instrucción 1/2009 y somete expresamente la videovigilancia con IA al artículo 5 y al artículo 26.10 del "
  "Reglamento (UE) 2024/1689",
  "Administraciones, entidades públicas, universidades y colegios profesionales de Cataluña, y entidades "
  "privadas cuando ejercen funciones públicas"),
 ("10 nov 2026", True, "Vencen dos plazos del catálogo de vulnerabilidades explotadas: CVE-2026-111497, en el "
  "decodificador Brotli, que viaja dentro de Node.js, .NET, PowerShell, cURL y las compilaciones de PHP para "
  "Windows, y CVE-2026-48356, en Adobe Commerce y Magento",
  "Brotli alcanza a casi cualquier pila moderna por dependencia; Magento, al comercio electrónico medio y "
  "grande"),
 ("10 nov 2026", True, "El director ejecutivo de ENISA presenta a la comisión de Industria del Parlamento "
  "Europeo el Informe sobre el Estado de la Ciberseguridad en la Unión, que es la radiografía oficial del "
  "grado de aplicación de NIS2",
  "Nadie por obligación; es la fuente que conviene tener marcada para argumentar el retraso de la "
  "transposición"),
 ("10 nov 2026", True, "Día de parches de SAP, confirmado en su propia página de notas de seguridad",
  "Cualquier cliente con SAP instalado en sus propias instalaciones"),
 ("11 nov 2026", True, "Vence el plazo del catálogo de vulnerabilidades explotadas para CVE-2026-41709, en "
  "VMware ESX. Conviene decir qué es y qué no: es una laguna de registro de actividad, que Broadcom puntúa "
  "2,7 baja, y entra en el catálogo porque sirve para ocultar lo que un administrador haga después",
  "Prácticamente cualquier centro de datos español mediano o grande"),
 ("11 nov 2026", True, "Cierra la inscripción para la mesa redonda que la autoridad neerlandesa de protección "
  "de datos convoca con el sector de recobro tras su informe sobre algoritmos e IA",
  "Agencias de cobro con actividad en Países Bajos y sus matrices"),
 ("13 nov 2026", True, "Vence el plazo del catálogo de vulnerabilidades explotadas para CVE-2026-118527, la "
  "segunda de Ivanti Connect Secure de la cadena",
  "Igual que la anterior de Ivanti: perímetro de gran empresa y administración"),
 ("13 nov 2026", True, "Cierra a las 23:59 la consulta pública del Comité Europeo de Protección de Datos sobre "
  "las directrices 04/2026, que regulan cuándo procede imponer una multa administrativa <b>en lugar de</b> otra "
  "medida correctiva. Es la única consulta de ciber-GRC abierta esta semana y el listado del Comité la esconde, "
  "porque no ordena por fecha",
  "Cualquier organización con exposición sancionadora en el RGPD, y en particular quien negocie con una "
  "autoridad una medida correctiva alternativa a la multa"),
 ("15 nov 2026", True, "Cierre previsto de la encuesta pública de las diecisiete normas europeas de la serie "
  "ETSI EN 304 que darán cobertura al Reglamento de Ciberresiliencia. Cautela: la nota de ETSI de agosto dice "
  "«de mediados de septiembre a mediados de noviembre, según el vertical» y <b>no publica fecha exacta</b>; "
  "esta es la lectura prudente de ese «mediados»",
  "Fabricantes de producto con elementos digitales que vayan a necesitar presunción de conformidad"),
 ("19 nov 2026", True, "Entra en vigor la Circular 1/2026 del Banco de España sobre la Central de Información "
  "de Riesgos, veinte días después de su publicación en el BOE del 30 de octubre. Es un texto refundido que "
  "compila catorce modificaciones de la Circular 1/2013",
  "Entidades declarantes a la Central de Información de Riesgos e intermediarios de crédito inmobiliario"),
 ("20 nov 2026", True, "Cierra el plazo de inscripción presencial a las XX Jornadas STIC del CCN, o antes si se "
  "completa el aforo",
  "Responsables de seguridad del sector público y de empresas estratégicas"),
 ("24 nov 2026", True, "Arrancan las XX Jornadas STIC, del 24 al 27 de noviembre en Madrid, bajo el lema «IA "
  "ofensiva y amenaza cuántica: hacia una nueva ciberseguridad». El CCN presentará las novedades de INÉS en el "
  "módulo del ENS",
  "Sector público sujeto al ENS y su cadena de proveedores"),
 ("25 nov 2026", True, "Cierra la consulta EBA/CP/2026/17, sobre las normas técnicas de requisitos "
  "prudenciales de las empresas de servicios de inversión",
  "Empresas de servicios de inversión y sus asesores"),
 ("27 nov 2026", True, "Vence aproximadamente el plazo de un mes que la CNIL dio a FNAC para acreditar que su "
  "herramienta nueva recoge el consentimiento cuando es exigible, bajo multa coercitiva de 10.000 euros por día "
  "de retraso. El cómputo corre desde la notificación de la decisión de 22 de octubre, de modo que la fecha "
  "exacta no es pública",
  "Cualquier responsable que use datos de navegación recogidos sin base para entrenar un algoritmo de "
  "recomendación"),
 ("29 nov 2026", True, "Elecciones al Congreso de los Diputados y al Senado, convocadas por el Real Decreto "
  "806/2026, de 5 de octubre",
  "Toda la previsión regulatoria española: nada se mueve antes"),
 ("2 dic 2026", True, "Se agota el periodo de gracia del artículo 111.4 del Reglamento de IA. Conviene decirlo "
  "bien porque es la confusión más fácil de la semana: <b>no nace ninguna obligación</b> ese día. La de marcar "
  "en formato legible por máquina el contenido sintético, del artículo 50.2, rige desde el 2 de agosto de 2026. "
  "Lo que vence es el plazo que el artículo 111.4 concedió a los sistemas <b>ya introducidos en el mercado "
  "antes</b> de esa fecha, de modo que a partir del 2 de diciembre no queda inventario heredado exento",
  "Proveedores de sistemas de IA, incluidos los de uso general, que generen audio, imagen, vídeo o texto "
  "sintéticos y lleven en el mercado desde antes del 2 de agosto de 2026"),
 ("2 dic 2026", True, "Entran en aplicación las dos prácticas prohibidas nuevas que el Reglamento (UE) "
  "2026/1744 insertó en el artículo 5.1, letras b bis) y b ter), junto con los apartados 1 bis y 1 ter que "
  "acotan su alcance. Este sí es un hito que crea obligación, y el capítulo de sanciones está plenamente "
  "aplicable desde el 2 de agosto de 2025",
  "Proveedores y responsables del despliegue de sistemas generativos de imagen, vídeo o audio, y cualquiera "
  "que los integre sin medidas técnicas de prevención"),
 ("2 dic 2026", True, "Mesa redonda de la autoridad neerlandesa de protección de datos con el sector de "
  "recobro sobre uso responsable de IA y decisiones automatizadas",
  "Agencias de cobro con actividad en Países Bajos"),
 ("3 dic 2026", True, "Cierra la consulta de la Comisión Europea sobre el EU Kids Act, que es la pieza europea "
  "de la que depende la consulta española que cierra el 4 de noviembre",
  "Plataformas y proveedores de sistemas de garantía de la edad"),
 ("11 dic 2026", True, "Fecha que el artículo 35.2 del Reglamento de Ciberresiliencia fija para que haya «un "
  "número suficiente de organismos notificados en la Unión». Hoy hay <b>cero</b>, reverificado contra el censo "
  "europeo esta misma mañana. Y hay que decir tres cosas o se sobrevende: obliga a <b>los Estados</b> y no a "
  "las empresas, es obligación <b>de medios</b> porque el texto dice «se esforzarán por garantizar», y el "
  "umbral es <b>agregado en la Unión</b> y no un cupo por país",
  "Fabricantes de productos de las clases del anexo III que vayan a necesitar un tercero para evaluar la "
  "conformidad antes del 11 de diciembre de 2027"),
 ("11 dic 2026", True, "Jornada de la Comisión Europea «Product Cybersecurity: Making CRA a Reality», el mismo "
  "día que el hito del artículo 35.2",
  "Fabricantes e importadores de producto con elementos digitales"),
 ("17 dic 2026", True, "Consejo Europeo, los días 17 y 18, confirmado por el aviso a medios del Consejo de 26 "
  "de octubre. Es el primero posterior a la ventana y el único con fecha publicada",
  "Nadie por obligación; es donde podría aparecer una conclusión sobre soberanía digital"),
 ("23 dic 2026", True, "Se constituyen las nuevas Cámaras, a las diez de la mañana. Es el primer hito real del "
  "reloj de la transposición española: hasta esa fecha no hay Cortes que puedan tramitar nada",
  "Toda la previsión regulatoria española"),
 ("25 dic 2026", True, "Cierre aproximado de la votación final de la ISO/IEC DTR 22216, sobre los desarrollos "
  "técnicos de la serie 15408 y de la 18045. La ficha dice «votación iniciada: 8 semanas» desde el 30 de "
  "octubre y <b>no publica fecha</b>; esto es un cálculo propio y conviene presentarlo así",
  "Laboratorios de evaluación y organismos de certificación de producto"),
 ("31 dic 2026", True, "Cierra la consulta EBA/CP/2026/18, sobre las normas técnicas de regulación del marco de "
  "gestión del riesgo operacional. Es la consulta financiera más pertinente del trimestre para un lector de "
  "ciber-GRC, porque el riesgo TIC vive dentro de ese marco",
  "Entidades de crédito y empresas de servicios de inversión, y quien les lleve la función de riesgo "
  "operacional"),
 ("1 ene 2027", True, "Termina el régimen transitorio de la Circular 1/2026 del Banco de España: el umbral de "
  "exención de declaración individualizada a la Central de Información de Riesgos deja de estar en 3.000 euros",
  "Entidades declarantes a la Central de Información de Riesgos"),
 ("4 ene 2027", False, "Cierra la consulta EBA/CP/2026/19, sobre las normas técnicas de ejecución revisadas de "
  "las decisiones conjuntas de requisitos prudenciales específicos",
  "Grupos bancarios transfronterizos y sus colegios de supervisores"),
 ("31 ene 2027", False, "Fin de vida de las ramas 22.7 y 22.8 de Ivanti Connect Secure, declarado por el propio "
  "fabricante en el aviso de esta semana",
  "Quien siga en esas ramas tras la cadena de explotación de octubre"),
 ("28 feb 2027", False, "Fin del periodo de transición a la ISO 37001:2025, el único documento de transición de "
  "Global ACI que vence a corto plazo",
  "Organizaciones con certificación de sistemas de gestión antisoborno"),
 ("28 feb 2027", False, "Plazo revisado para las normas armonizadas de apoyo al Reglamento de IA, según el "
  "boletín de CEN-CENELEC del 28 de octubre, que lo sitúa en «febrero de 2027» sin día concreto",
  "Proveedores de sistemas de IA de alto riesgo que necesiten presunción de conformidad"),
 ("8 mar 2027", False, "Fecha indicativa de pleno en primera lectura de la modificación específica de NIS2, el "
  "expediente 2026/0012(COD). Es indicativa y es del expediente de modificación, no del Digital Omnibus, que no "
  "tiene fecha publicada",
  "Entidades esenciales e importantes, cuando llegue; hoy es solo calendario parlamentario"),
 ("2 ago 2027", False, "Plazo del artículo 111.3 del Reglamento de IA para los modelos de IA de uso general "
  "introducidos en el mercado antes del 2 de agosto de 2025",
  "Proveedores de modelos fundacionales con producto heredado"),
 ("2 dic 2027", False, "Aplicación de las secciones 1 a 3 del capítulo III del Reglamento de IA a los sistemas "
  "de alto riesgo del anexo III, tras el retraso del Reglamento 2026/1744",
  "Proveedores y responsables del despliegue de sistemas de alto riesgo por área de uso"),
 ("11 dic 2027", False, "Aplicación general del Reglamento de Ciberresiliencia. Y el artículo 69.3, que casi "
  "nadie cita: las obligaciones de notificación del artículo 14 alcanzan a <b>todos</b> los productos "
  "comercializados antes de esa fecha, no solo a los nuevos",
  "Fabricantes, importadores y distribuidores de producto con elementos digitales, con catálogo vivo "
  "incluido"),
 ("2 ago 2028", False, "Aplicación de las secciones 1 a 3 del capítulo III del Reglamento de IA a los sistemas "
  "de alto riesgo del anexo I, es decir la IA integrada como componente de seguridad en productos ya regulados",
  "Fabricantes de máquinas, ascensores, juguetes y productos sanitarios con IA dentro"),
 ("2 ago 2030", False, "Plazo del artículo 111.2 del Reglamento de IA para los sistemas de alto riesgo "
  "destinados a ser utilizados por autoridades públicas",
  "Administraciones y sus proveedores de IA"),
 ("31 dic 2030", False, "Plazo del artículo 111.1 del Reglamento de IA para los sistemas informáticos de gran "
  "magnitud del anexo X",
  "Administraciones con sistemas europeos de gran magnitud"),
]

TITS = {
 "es":  f"El contador de entidades críticas pasa de los {CER_DIAS} días y los {CER_MILL} millones, y por fin se "
        f"puede afirmar con fuente primaria que NIS2 nunca tuvo proyecto de ley",
 "eu":  "Cero organismos notificados del Reglamento de Ciberresiliencia a 39 días de su propio hito, "
        "reverificado contra el censo europeo esta misma mañana",
 "fin": "Venció el plazo del Banco Central Europeo, y 6.300 millones robados a Binance no generaron ni una "
        "notificación europea porque la entidad está fuera del perímetro de DORA",
 "std": "El NIST cierra en firme la guía de transición a la criptografía poscuántica, y las normas "
        "armonizadas del Reglamento de IA se van a febrero de 2027",
 "ai":  "El 2 de diciembre concentra dos hitos del Reglamento de IA, no uno, y solo uno de ellos crea "
        "obligación nueva",
 "thr": "PHP se estaba explotando cuatro días antes de que existiera el parche, y la cadena con el núcleo de "
        "Linux llega hasta root",
}

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = []

ITEMS += [

("es", f"Seguimiento del incumplimiento · a {FECHA_TXT}", True,
 f"El tanto alzado que la Comisión pide a España por entidades críticas llega a {CER_EUR} euros, con "
 f"{CER_DIAS} días transcurridos, y esta semana se confirma que NIS2 nunca tuvo siquiera proyecto de ley",
 f"Este bloque va todas las semanas, se haya movido algo o no, porque la cifra sube sola y es el mejor "
 f"argumento disponible para explicar por qué un real decreto-ley es probable. A día de hoy han pasado "
 f"<b>{CER_DIAS} días</b> desde que venció el plazo de transposición de la <b>Directiva (UE) 2022/2557</b>, el "
 f"17 de octubre de 2024. Al importe diario de <b>{CER_DIARIO} euros</b> que la Comisión reclama en el asunto "
 f"<b>C-616/26</b>, eso da <b>{CER_EUR} euros</b>, muy por encima del mínimo de {CER_MINIMO} euros que el "
 f"escrito fija como suelo. El delta de esta semana son siete días, es decir <b>{CER_SEMANA} euros</b>. Las dos "
 f"comprobaciones obligatorias de cada lunes, hechas: <b>no hay sentencia, ni conclusiones, ni auto en el "
 f"C-616/26</b>, sondeados nueve patrones de identificador del asunto, de los que ocho devuelven que no existe "
 f"el documento, y tampoco hay sentencia en ninguno de los seis asuntos CER hermanos; y <b>sigue sin haber "
 f"número de asunto público del recurso por NIS2</b>, barridos esta vez <b>los 1.207 avisos de asunto nuevo</b> "
 f"publicados en el Diario Oficial serie C en 2026, con el texto íntegro abierto de 1.206 de ellos, sin una "
 f"sola mención de la Directiva 2022/2555.",
 f"Hay que decir dos cosas al dar esta cifra, y las dos protegen a quien la repite. La primera: es <b>lo pedido "
 f"por la Comisión, no lo impuesto</b>; solo el Tribunal fija el importe final y puede reducirlo. La segunda, y "
 f"es la que convierte el dato en incentivo y no en anécdota: <b>el contador del tanto alzado se detiene al "
 f"transponer, no al dictarse sentencia</b>. Cada semana sin ley son {CER_SEMANA} euros más que ya no se "
 f"recuperan transponiendo después. Si llega sentencia condenatoria, el tanto alzado se congela en la fecha que "
 f"fije el Tribunal y arranca además la multa coercitiva de {CER_COERC} euros diarios, que es un régimen "
 f"distinto y peor. Y la novedad de esta semana obliga a matizar la previsión al alza en dificultad: con "
 f"<b>CER</b> hay un texto del que partir, el 121/000088 caducado, de modo que la legislatura siguiente puede "
 f"reintroducirlo; con <b>NIS2 no hay nada que reintroducir</b>, porque no se presentó nunca. Por ley ordinaria, "
 f"no antes del <b>segundo semestre de 2027</b> y con 2028 como caso central, porque las Cámaras no se "
 f"constituyen hasta el 23 de diciembre; por real decreto-ley, primer semestre de 2027 si hay gobierno en enero "
 f"o febrero. Un decreto-ley es más probable en CER que en NIS2, simplemente porque hay borrador.",
 'El aviso del asunto en el <a href="http://data.europa.eu/eli/C/2026/3986/oj" @L>Diario Oficial, serie C, '
 'C/2026/3986 de 3 de agosto de 2026</a>, la ficha del <a href="https://curia.europa.eu/juris/liste.jsf?'
 'num=C-616/26&amp;language=es" @L>asunto C-616/26 en el Tribunal de Justicia</a> y el '
 '<a href="https://www.congreso.es/proyectos-de-ley" @L>listado de proyectos de ley del Congreso</a>, donde se '
 'comprueban los 115 expedientes de la legislatura y su situación.',
 "Dos cautelas de método, que esta semana han cambiado y conviene registrar. La primera: el universo de avisos "
 "a barrer son <b>1.207</b> si se cuenta por fecha de publicación en 2026, que es el criterio correcto para "
 "detectar novedades, y no los 328 que daba la edición pasada, que eran los asuntos del Tribunal de Justicia "
 "incoados en 2026. La segunda es buena noticia operativa: el aviso de recurso por incumplimiento <b>sí "
 "indexa</b> la directiva invocada en el grafo de citas del repositorio europeo, de modo que no hace falta "
 "abrir el texto de cada uno; se ha hecho igualmente para contrastar, y las dos vías concuerdan. Y una "
 "medición propia útil: el desfase entre interponer el recurso y publicar su aviso va de <b>47 a 62 días</b> "
 "sobre los seis casos CER, de modo que el recurso de NIS2, decidido el 8 de julio, va ya <b>más lento que el "
 "precedente</b>. Ausencia de aviso sigue sin ser ausencia de recurso."),

("es", "Consejo de Ministros · 27 de octubre de 2026", True,
 "El Gobierno pide dictamen urgente al Consejo de Estado, con plazo el 5 de noviembre, sobre el real decreto "
 "que regulará requisitos de resiliencia y soberanía digital en centros de datos",
 "El Consejo de Ministros del <b>27 de octubre</b> aprobó, a propuesta del Ministerio para la Transición "
 "Ecológica y el Reto Demográfico, un acuerdo por el que «se solicita a la Comisión Permanente del Consejo de "
 "Estado la emisión de dictamen, <b>con carácter urgente, no más tarde del día 5 de noviembre de 2026</b>, en "
 "relación con el proyecto de Real Decreto por el que se regulan los requisitos de sostenibilidad energética, "
 "medioambiental y <b>de resiliencia y soberanía digital</b> aplicables a los centros de datos». El dictamen "
 "del Consejo de Estado es el último trámite preceptivo antes de aprobar un real decreto, y pedirlo con "
 "carácter urgente y fecha fija a tres semanas de las elecciones indica intención de cerrarlo antes del 29 de "
 "noviembre. Fue el <b>único asunto con contenido digital</b> de toda la referencia: el barrido completo del "
 "texto no devuelve ni una mención de ciberseguridad, NIS2, entidades críticas, DORA, inteligencia artificial, "
 "AESIA, Esquema Nacional ni protección de datos, y el <b>Ministerio para la Transformación Digital y de la "
 "Función Pública no llevó ni un solo asunto</b>.",
 "Es el único movimiento normativo español con fecha dura de la semana, y la acción que toca es de vigilancia, "
 "no de cumplimiento. Si tienes clientes que operan centros de datos, alojan en ellos o compran nube con "
 "requisitos de localización del dato, este es el expediente que hay que seguir día a día en las próximas dos "
 "semanas, porque entre el dictamen y el Consejo de Ministros puede mediar muy poco. Pero hay que ser "
 "escrupuloso con lo que todavía no se sabe, y aquí está la trampa: <b>el proyecto no está publicado</b>. No "
 "hay texto, no hay obligaciones conocidas y no hay fecha de aprobación. Cualquiera que esta semana te cuente "
 "qué va a exigir ese real decreto a los centros de datos se lo está inventando, porque ni siquiera pasó por la "
 "audiencia pública del Ministerio para la Transformación Digital, cosa coherente con que el proponente sea "
 "Transición Ecológica. Lo verificable es el plazo y el título. Con eso basta para avisar a un cliente de que "
 "viene algo y de que no le va a dar tiempo a opinar.",
 'La <a href="https://www.lamoncloa.gob.es/consejodeministros/referencias/Paginas/2026/20261027-referencia-'
 'rueda-de-prensa-ministros.aspx" @L>referencia del Consejo de Ministros de 27 de octubre de 2026</a>, donde el '
 'acuerdo figura bajo el encabezado del Ministerio para la Transición Ecológica.',
 "Ojo a una confusión fácil de la semana, porque hay dos «servicios universales» circulando y solo uno es de "
 "este ámbito. Lo que se publicó en el BOE del 29 de octubre es la modificación del acuerdo de obligaciones de "
 "servicio público al prestador del <b>servicio postal</b> universal para las elecciones, no del servicio "
 "universal de telecomunicaciones. La audiencia pública sobre el cese de elementos del servicio universal de "
 "telecomunicaciones <b>cerró el 22 de octubre</b>, antes de esta ventana. El acuerdo postal tiene, eso sí, un "
 "gancho de identidad digital: se modifica entre otras cosas por la puesta en marcha de <b>MiDNI</b> en el voto "
 "por correo."),

("es", "CCN · Guía CCN-STIC-2011, de 29 de octubre de 2026", True,
 "El Centro Criptológico Nacional publica la primera metodología española de evaluación de seguridad de "
 "productos con inteligencia artificial, con 27 requisitos y laboratorio acreditado",
 "El <b>29 de octubre</b> el <b>CCN</b> publicó la guía <b>CCN-STIC-2011, Metodología de Evaluación de "
 "Seguridad de Productos - Inteligencia Artificial (ESP-IA)</b>, con dos anexos: la plantilla de Declaración de "
 "Seguridad y la del Informe Técnico de Evaluación. La mecánica, en palabras del propio CCN: «el fabricante "
 "describe su arquitectura y responde a un cuestionario sobre las capacidades de la IA; a partir de esta "
 "información, una <b>matriz de aplicabilidad</b> determina cuáles de los <b>27 requisitos</b> previstos debe "
 "cumplir. Un <b>laboratorio acreditado y autorizado por el CCN</b> verifica cada requisito aplicable y realiza "
 "pruebas de penetración adicionales, tomando como referencia la <b>OWASP AI Testing Guide</b> y las técnicas "
 "de ataque más actuales». Las amenazas que cubre están enumeradas y son las que importan: «la evasión de "
 "decisiones, la inyección de instrucciones, el envenenamiento, la extracción del modelo, la fuga de "
 "información protegida, el agotamiento de recursos y el <b>uso indebido de herramientas y acciones por parte "
 "de sistemas agénticos</b>». Y exige dos principios: «la <b>supervisión humana antes de ejecutar acciones "
 "críticas o irreversibles</b> y la <b>trazabilidad</b> necesaria para reconstruir posteriormente la actuación "
 "de la IA».",
 "Es la pieza más aprovechable de la semana para España y conviene entender para qué sirve de verdad. No "
 "establece ningún plazo ni obliga a nadie: es metodología de evaluación voluntaria, y la antesala natural de "
 "una futura categoría de productos con IA en el <b>CPSTIC</b>, que es el catálogo que condiciona las compras "
 "públicas bajo el ENS. Dos usos inmediatos. Si asesoras a un fabricante que quiere vender IA a la "
 "Administración española, esos 27 requisitos son el guion de su hoja de ruta y la Declaración de Seguridad es "
 "el entregable; empezar ahora es ventaja competitiva de doce meses. Y si asesoras al comprador, úsalo como "
 "pliego: los dos principios que el CCN exige, supervisión humana antes de acciones irreversibles y "
 "trazabilidad reconstruible, son exactamente las dos cláusulas que faltan en casi todos los contratos de "
 "agentes de IA que se están firmando este año. Repárese además en la convergencia con el decálogo que la AEPD "
 "publicó dos días antes: dos organismos españoles distintos, en la misma semana, señalando el mismo riesgo del "
 "uso indebido de herramientas por sistemas agénticos.",
 'La <a href="https://www.ccn.cni.es/es/actualidad-ccn/1401-el-centro-criptologico-nacional-desarrolla-una-'
 'metodologia-de-evaluacion-de-seguridad-de-productos-con-inteligencia-artificial" @L>nota del CCN de 29 de '
 'octubre de 2026</a>.',
 "Cautela de verificación, que se declara: <b>el texto de la guía no se ha podido descargar</b>. El "
 "repositorio de guías CCN-STIC vive en el dominio del CERT, que rechaza el acceso automatizado, y la página "
 "pública de guías del CCN es una presentación sin listado que enlaza a ese mismo portal. Los 27 requisitos, "
 "los dos anexos y la lista de amenazas están acreditados por la nota del CCN, que es fuente primaria, pero "
 "<b>no por lectura del documento</b>. Si vas a construir una hoja de ruta sobre esos 27 requisitos, descarga "
 "la guía tú mismo antes."),

("es", "CCN · INÉS renovado, 28 de octubre de 2026", True,
 "El CCN renueva la herramienta con la que mide el ENS y publica las cifras de la campaña 2025: el índice de "
 "cumplimiento es 65,27 en categoría ALTA, que es donde están los sistemas que más importan",
 "El <b>28 de octubre</b> el CCN anunció la renovación de <b>INÉS</b>, con tres cambios operativos declarados: "
 "«<b>nuevo cuestionario</b>, adaptado a las amenazas actuales, a la realidad de los organismos y a la "
 "normativa europea»; <b>nuevo mecanismo de autenticación</b>, porque «el acceso a Gobernanza se va a realizar "
 "a través del sistema de autenticación única del CCN» y los usuarios recibirán indicaciones para «iniciar el "
 "proceso guiado de migración»; y <b>migración de sistemas conforme al nuevo Perfil de Cumplimiento Específico "
 "de Requisitos Fundamentales de Seguridad (PCE-RFS)</b>, que «permite migrar los sistemas obsoletos desde el "
 "listado de la sección Esquema Nacional de Seguridad». Y con ello las cifras de la campaña 2025, que son la "
 "radiografía oficial del ENS: «<b>2.783 organismos</b> cargaron sus datos, alrededor de un 3 % más que el año "
 "anterior, con un total de <b>23.541 sistemas TIC</b> registrados que dan servicio a cerca de <b>35 millones "
 "de usuarios</b>». El índice de cumplimiento «alcanza un valor de <b>100 en la categoría BÁSICA</b>, respecto "
 "de los organismos que han reportado; de <b>77,12 en la MEDIA</b>, y de <b>65,27 en la ALTA</b>».",
 "Esas tres cifras son el material más citable del año para una conversación con un responsable de seguridad "
 "del sector público, y hay que leerlas del revés de como parecen. El 100 en BÁSICA no es un éxito: el propio "
 "CCN lo acota con «respecto de los organismos que han reportado», de modo que mide a los que contestan, no al "
 "universo. Lo revelador es la pendiente invertida: <b>el cumplimiento baja a medida que sube la criticidad</b>, "
 "de 100 a 77,12 y a 65,27. Donde están los sistemas de categoría ALTA, que son los que manejan información "
 "cuyo compromiso causa un perjuicio muy grave, el cumplimiento declarado es de dos tercios. Si asesoras a un "
 "organismo de categoría ALTA, esa es la cifra que justifica el plan de adecuación ante su propia dirección, "
 "y viene del regulador, no de un consultor. Y el dato de 23.541 sistemas para 35 millones de usuarios sirve "
 "para dimensionar: no es un problema de unas cuantas sedes electrónicas.",
 'La <a href="https://www.ccn.cni.es/es/actualidad-ccn/1400-el-ccn-renueva-ines-con-el-fin-de-facilitar-la-'
 'adecuacion-al-ens-y-consolidar-la-informacion-de-ciberseguridad-de-los-organismos-publicos" @L>nota del CCN '
 'de 28 de octubre de 2026</a>, y la base legal que cita, el artículo 32 del Real Decreto 311/2022.',
 "Aquí hay un hallazgo lateral que es casi más importante que las cifras, y hay que presentarlo con la cautela "
 "exacta. La nota confirma, en fuente primaria del CCN y con fecha, que existe un <b>Perfil de Cumplimiento "
 "Específico de Requisitos Fundamentales de Seguridad, el PCE-RFS</b>, y que INÉS ya permite migrar a él "
 "sistemas que califica de «obsoletos». Lo que la nota <b>no</b> dice es su fecha de aprobación, su número de "
 "guía CCN-STIC asociada ni ningún plazo de migración, y el documento del perfil no se ha podido localizar "
 "porque vive en el portal del ENS, bloqueado al acceso automatizado. De modo que: el perfil existe y la "
 "migración está abierta, pero <b>no afirmes plazos de migración al PCE-RFS</b>, porque no están publicados en "
 "esta fuente. Las novedades se presentan en las Jornadas STIC, módulo del ENS, Sala 6."),

("es", "CCN · Catálogo CPSTIC de octubre, 26 de octubre de 2026", False,
 "Cuatro productos y un servicio entran en el catálogo que condiciona las compras públicas bajo el ENS, y tres "
 "de las cinco altas son de Fortinet y WatchGuard",
 "El <b>26 de octubre</b> el CCN publicó la actualización mensual del <b>CPSTIC</b>: «se han incorporado al "
 "catálogo cuatro productos incluidos en las categorías de protección de redes y sistemas, protección de la "
 "información, de dispositivos y perímetro y un servicio de control de accesos». Las altas, tal como las "
 "tabula el CCN: <b>BMC 3.8.6.11</b> de xFusion Digital Technologies en protección de redes y sistemas; "
 "<b>ZED! Q.2023</b> de PRIMX en protección de la información; <b>FortiEDR 6.0</b> de Fortinet en protección de "
 "dispositivos; <b>FortiGate</b> familias E, F y G con FortiOS 7.2 en protección de perímetro; y "
 "<b>AuthPoint</b> de WatchGuard Technologies en control de accesos. El catálogo se publica «tanto en su "
 "formato online como en la Guía CCN-STIC 105».",
 "Importa por una razón muy concreta y poco glamurosa: estar en el CPSTIC es lo que permite a un fabricante "
 "«posicionarse en los procesos de adquisición de sistemas TIC que se encuentren bajo el alcance del ENS», en "
 "palabras del propio CCN. Para quien asesora a un organismo público, el catálogo actualizado es el filtro "
 "previo de cualquier pliego de seguridad; para quien asesora al fabricante, es el trámite que decide si puede "
 "concursar. Y hay una lectura de gobernanza que conviene tener preparada, porque un cliente la va a plantear "
 "esta semana: el catálogo dio de alta FortiEDR, tres familias FortiGate y AuthPoint de WatchGuard en la misma "
 "ventana en la que el INCIBE-CERT publicó avisos de severidad crítica sobre <b>Fireware OS de WatchGuard</b>, "
 "el 28 de octubre, y sobre productos de Fortinet, el 23. Son productos y módulos distintos y <b>ninguna fuente "
 "afirma que las versiones certificadas estén afectadas</b>; no lo presentes como una incompatibilidad, porque "
 "no lo es. El punto utilizable es otro y es de gobierno: <b>estar en el CPSTIC no exime de la gestión de "
 "vulnerabilidades del fabricante</b>, y un pliego que se apoye solo en la certificación sin exigir ventanas de "
 "parcheo está incompleto.",
 'La <a href="https://www.ccn.cni.es/es/actualidad-ccn/1399-el-centro-criptologico-nacional-incorpora-cuatro-'
 'nuevos-productos-y-un-servicio-al-catalogo-cpstic" @L>nota del CCN de 26 de octubre de 2026</a> y el '
 '<a href="https://cpstic.ccn.cni.es/es/inclusion" @L>procedimiento de inclusión en el catálogo</a>.',
 "Verificación declarada: <b>el catálogo en línea y la Guía CCN-STIC 105 no se han podido abrir</b>, porque el "
 "portal CPSTIC devuelve una redirección a un sistema de gestión de bots. Las cinco altas están acreditadas "
 "por la nota del CCN y no por lectura del catálogo, de modo que el detalle de versiones y perfiles de cada "
 "producto queda <b>no reconfirmado en fuente primaria esta semana</b>."),

("es", "Autoridad Catalana de Protección de Datos · Circular 1/2026", True,
 "La primera norma española que une videovigilancia e IA entra en vigor el domingo, y lo que de verdad hay que "
 "saber es que no obliga a cambiar los carteles ya instalados",
 "Confirmada la fecha contra el texto oficial del Diario Oficial de la Generalitat, no contra la nota de "
 "prensa: la <b>Circular 1/2026</b> está firmada en Barcelona el <b>14 de octubre de 2026</b>, se publicó en el "
 "<b>DOGC número 9775 de 19 de octubre</b> y su disposición final dice que «entrará en vigor a los veinte días "
 "de haberse publicado», lo que da el <b>8 de noviembre de 2026</b>. Su disposición adicional somete los "
 "sistemas de videovigilancia con IA tanto al RGPD como al <b>Reglamento (UE) 2024/1689</b>, y cita los "
 "artículos concretos: las prácticas prohibidas de las letras e), f), g) y h) del apartado 1 del artículo 5, "
 "los apartados 3, 4 y 5 de ese mismo artículo sobre identificación remota «en tiempo real» en espacios de "
 "acceso público, y el <b>apartado 10 del artículo 26</b> sobre identificación remota en diferido. Deroga la "
 "Instrucción 1/2009. Y lleva una <b>corrección de errores</b> publicada en el DOGC 9778 de 22 de octubre que "
 "restituye la numeración del apartado 7 del artículo 14, cuyo contenido obliga a mantener a disposición de los "
 "afectados, «en un lugar fácilmente accesible», la información del artículo 13 del RGPD, pudiendo ofrecerse "
 "por web o sede electrónica.",
 "El valor va mucho más allá de Cataluña y es el ángulo que conviene explotar: mientras el Estado no puede "
 "legislar porque las Cortes están disueltas, <b>una autoridad autonómica ha fijado el estándar de hecho</b> "
 "que van a invocar auditores, delegados de protección de datos y reclamantes también fuera de Cataluña. Si "
 "tienes un cliente con videovigilancia analítica en cualquier comunidad, este es el documento que le van a "
 "citar. Para el ámbito catalán es derecho aplicable el domingo, y la lista de deberes es concreta: decidir "
 "memoria previa frente a evaluación de impacto, formalizar el encargo con la empresa de seguridad privada y "
 "repasar el capítulo 6, que es el de obligaciones y medidas de seguridad. Pero lo más útil que puedes hacer "
 "esta semana es <b>desmontar una alarma</b>, porque es el error de plazo más probable que vas a oír: su "
 "disposición transitoria dice que las obligaciones del artículo 14 sobre contenido y diseño de los carteles "
 "«son exigibles a los tratamientos de videovigilancia que se inicien a partir de la entrada en vigor», y que "
 "los carteles existentes conformes a la Instrucción 1/2009 «se pueden mantener hasta que se hayan de "
 "sustituir por su mantenimiento ordinario». Es decir: <b>el 8 de noviembre nadie tiene que cambiar la "
 "cartelería instalada</b>.",
 'La <a href="https://www.apdcat.cat/ca/normativa-i-jurisprudencia/instruccions-i-recomanacions-de-l-apdcat" '
 '@L>página de instrucciones y recomendaciones de la autoridad catalana</a>, y la '
 '<a href="https://dogc.gencat.cat/ca/document-del-dogc/?documentId=1057099" @L>ficha de la Circular en el '
 'DOGC número 9775</a>, cuyo PDF es el único texto auténtico.',
 "Una discrepancia de fecha que conviene resolver antes de citar la norma derogada, porque la propia autoridad "
 "se contradice. El <b>texto publicado en el DOGC</b>, en su disposición derogatoria, dice «Instrucció 1/2009, "
 "de <b>6 de febrer</b> de 2009». La nota de prensa de la autoridad y su página de instrucciones dicen «de "
 "<b>10 de febrer</b>». Prevalece el texto del diario oficial: si citas la instrucción derogada, usa el <b>6 de "
 "febrero de 2009</b>. Es un detalle menor hasta que un cliente lo comprueba."),

("es", "Consejo de Transparencia y Protección de Datos de Andalucía · 26 de octubre de 2026", False,
 "La autoridad andaluza publica una herramienta de autoevaluación con modelo de madurez de cinco niveles, y "
 "garantiza que no ve ninguna de las respuestas",
 "El <b>26 de octubre</b>, primer día de la ventana, el Consejo andaluz «ha puesto en marcha una herramienta de "
 "autoevaluación del cumplimiento en protección de datos, dirigida a los responsables del tratamiento del "
 "<b>sector público</b>, con el objetivo de facilitarles un diagnóstico de su situación». Lo aprovechable es su "
 "estructura: «la herramienta incorpora un <b>modelo de madurez</b> basado en niveles», y para cada cuestión la "
 "entidad se autoevalúa como «<b>inexistente, inicial, parcial, sustancial o consolidado</b>, además de la "
 "opción no aplica». El cuestionario «se estructura en <b>21 bloques temáticos</b>, que abarcan desde los "
 "principios que deben regir cualquier tratamiento hasta aspectos específicos como la <b>seguridad, las brechas "
 "de datos personales, las evaluaciones de impacto y gestión de riesgos</b>, el delegado de protección de datos "
 "o las transferencias internacionales». Genera dos informes, un resumen ejecutivo con los resultados agregados "
 "y uno completo con el detalle, y las observaciones «pueden servir como <b>plan de acción o memoria de "
 "cumplimiento</b>». Y una garantía explícita: «toda la información de la autoevaluación permanece "
 "exclusivamente en el equipo de la persona usuaria <b>sin que el Consejo tenga acceso a información "
 "alguna</b>».",
 "Esto es una herramienta gratuita que hace la mitad de un diagnóstico que se suele facturar, y lo honesto es "
 "decirlo: úsala, no compitas con ella. Su valor para un consultor es doble. Primero, como lenguaje común: un "
 "modelo de madurez de cinco niveles con los mismos nombres que usa el regulador autonómico es un marco de "
 "conversación que ningún cliente va a discutir, y encaja con la escala del ENS sin violencia. Segundo, y es lo "
 "que de verdad vale, como <b>evidencia de diligencia</b>: la propia autoridad dice que las observaciones "
 "sirven de memoria de cumplimiento, y una autoevaluación fechada con plan de acción asociado es exactamente lo "
 "que el artículo 5.2 del RGPD pide acreditar. La cláusula de confidencialidad es el argumento que desmonta la "
 "objeción obvia del cliente público, que es el miedo a autoincriminarse ante su propio supervisor. Y conviene "
 "no perder de vista el contexto: el Consejo tiene en marcha un <b>Plan de Control e Inspección sobre "
 "Protección de Datos en el Sector Público Andaluz 2026-2027</b>, de modo que la herramienta llega "
 "inmediatamente antes de una campaña de inspección.",
 'La <a href="https://www.ctpdandalucia.es/noticias/el-consejo-pone-en-marcha-herramienta-autoevaluacion-para-'
 'mejorar-el-cumplimiento-la-normativa-proteccion-datos" @L>nota del Consejo andaluz de 26 de octubre de '
 '2026</a>.',
 "El plan de inspección 2026-2027 figura destacado en la portada del Consejo pero <b>no se ha podido fechar</b> "
 "ni verificar su contenido, de modo que no consta como novedad de esta ventana y no debe citarse con fecha. "
 "Lo único verificado de él es que existe y que el propio organismo lo destaca."),

("es", "BOE · artículo 12.3 del Real Decreto 311/2022", False,
 "Un organismo de la Administración General del Estado aprueba su política de seguridad esta semana y la ancla "
 "en el decreto-ley de 2018, citando NIS2 como directiva europea y no como norma española",
 "El <b>30 de octubre</b> se publicó en el BOE, Sección III, la <b>Resolución de 8 de octubre de 2026</b> del "
 "Instituto de la Juventud por la que se aprueba su <b>Política de Seguridad de la Información</b>, «de acuerdo "
 "con lo previsto en el artículo 12.3 del Real Decreto 311/2022». Doce páginas. Su ámbito subjetivo es el que "
 "conviene retener, porque alcanza a la cadena de proveedores: «será de obligado cumplimiento para <b>todo el "
 "personal, propio o ajeno</b>, en el uso de medios digitales y en lo relativo a la información en soporte "
 "papel», y «a toda persona que acceda tanto a los sistemas TIC como a la propia información que sea gestionada "
 "por el organismo autónomo, <b>con independencia de cuál sea su destino, adscripción o relación con éste</b>». "
 "Surte efectos desde el <b>31 de octubre de 2026</b>. Y el detalle que la convierte en dato de este boletín: "
 "su marco normativo cita «el <b>Real Decreto-ley 12/2018</b>, de 7 de septiembre, de seguridad de las redes y "
 "sistemas de información que traspone la Directiva Europea NIS» y, aparte, «la <b>Directiva (UE) 2022/2555</b> "
 "del Parlamento europeo y del Consejo de 14 de diciembre de 2022».",
 "Es un asunto pequeño que sirve de prueba documental para una conversación grande. Un organismo de la "
 "Administración General del Estado aprueba su política de seguridad en octubre de 2026 y tiene que seguir "
 "anclándola en la transposición de <b>NIS1</b>, de 2018, porque la de NIS2 no existe, y cita la directiva "
 "europea como directiva, no como derecho español. Guárdalo: es la demostración, en el BOE y con fecha, de que "
 "el vacío de transposición no es una abstracción de Bruselas sino algo que ya ensucia los documentos de "
 "cumplimiento de la propia Administración. Úsalo con el cliente que pregunta «pero esto de NIS2 a mí cuándo me "
 "afecta»: le afecta ya en que su marco de referencia está desactualizado y sus cláusulas contractuales citan "
 "una norma a punto de ser sustituida. Y hay un uso directo para proveedores: ese ámbito subjetivo, «todo el "
 "personal, propio o ajeno», «con independencia de cuál sea su relación», es el modelo de redacción que "
 "cualquier organismo va a trasladar a sus pliegos. Si tienes clientes que venden a la Administración, esa "
 "frase es la obligación que van a heredar sin negociarla.",
 'La <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-22784" @L>Resolución de 8 de octubre de 2026 '
 'del Instituto de la Juventud, publicada en el BOE del 30 de octubre</a>.',
 None),

("es", "Contratación pública · BOE de 27 de octubre de 2026", False,
 "El Mando Conjunto del Ciberespacio compra una herramienta de IA para ciberoperaciones por procedimiento "
 "negociado sin publicidad, con proveedor único",
 "Dos adjudicaciones con carga ciber se publicaron en el BOE del <b>27 de octubre</b>. La primera: el <b>Estado "
 "Mayor de la Defensa</b> adjudicó la «<b>Adquisición de herramienta IA para ciberoperaciones del Mando "
 "Conjunto del Ciberespacio</b>» a <b>Alias Robotics, S.L.</b>, una PYME de Vitoria-Gasteiz, por <b>142.800 "
 "euros</b>, con fecha de adjudicación de 22 de septiembre de 2026. El procedimiento fue <b>negociado sin "
 "publicidad</b>, con la justificación literal de «proveedor único por razones técnicas» del artículo 168.a).2 "
 "de la Ley de Contratos del Sector Público. La segunda: la Subdirección General de Gestión Económica del "
 "Ministerio de la Presidencia adjudicó el «suministro e instalación de equipos <b>FIREWALL</b> para el "
 "<b>Departamento de Seguridad Nacional</b>» a Centro Regional de Servicios Avanzados, S.A., con una sola "
 "oferta recibida.",
 "No hay nada que cumplir aquí, y por eso es útil: es señal de mercado, que es lo que un consultor necesita "
 "para dimensionar su oferta. Tres lecturas. Una, de volumen: 142.800 euros es una cifra muy pequeña para una "
 "capacidad de ciberoperaciones, lo que indica que estamos ante una herramienta puntual o un piloto, no ante un "
 "programa. Dos, de competencia: proveedor único por razones técnicas y una PYME española adjudicataria dicen "
 "que en IA ofensiva aplicada el mercado nacional está muy concentrado y aún no hay oferta sustituible, lo que "
 "es una oportunidad si tienes clientes en ese nicho. Tres, y es la que vale para la mayoría: una sola oferta "
 "recibida en un contrato de cortafuegos para el Departamento de Seguridad Nacional. Cuando los procedimientos "
 "de seguridad de los organismos más sensibles reciben una oferta, el problema no es el precio: es que el "
 "pliego es tan específico que solo lo cumple quien ya está dentro. Si asesoras al comprador, ese es un riesgo "
 "de dependencia de proveedor que conviene medir antes de que se convierta en un riesgo de continuidad.",
 'Los anuncios de adjudicación <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-B-2026-35051" @L>'
 'BOE-B-2026-35051, del Estado Mayor de la Defensa</a> y '
 '<a href="https://www.boe.es/diario_boe/txt.php?id=BOE-B-2026-35037" @L>BOE-B-2026-35037, del Ministerio de la '
 'Presidencia</a>, los dos en el BOE de 27 de octubre de 2026.',
 "Sin relación con lo anterior pero en la misma semana, y conviene registrarlo para seguimiento de riesgo de "
 "terceros en el sector público: el BOE del 28 de octubre publicó una adenda al convenio entre la <b>Agencia "
 "Estatal de Administración Digital</b> y el Instituto de las Mujeres para la solución de nube híbrida "
 "<b>NubeSARA</b>, y otra entre la Secretaría de Estado de Digitalización e Inteligencia Artificial y ENISA, "
 "esta última de préstamos participativos y no de ciberseguridad. Ojo a la coincidencia de siglas: la ENISA "
 "española de financiación no es la Agencia de la Unión Europea para la Ciberseguridad."),

("es", "XX Jornadas STIC · 24 al 27 de noviembre de 2026", False,
 "El CCN pone el lema de la edición en IA ofensiva y amenaza cuántica, y la inscripción cierra el 20 de "
 "noviembre o cuando se llene el aforo",
 "Nota del CCN de 20 de octubre, anterior a la ventana pero con dos plazos vivos dentro de los próximos "
 "veinticinco días: «las <b>XX Jornadas STIC</b> se celebrarán del <b>24 al 27 de noviembre</b> en los cines "
 "Kinépolis Ciudad de la Imagen de Madrid, bajo el lema «<b>IA ofensiva y amenaza cuántica: hacia una nueva "
 "ciberseguridad</b>»», y «el plazo para solicitar la asistencia presencial permanecerá abierto <b>hasta el 20 "
 "de noviembre o hasta completar el aforo</b>». Tendrán espacio propio la <b>AEPD</b>, la Secretaría de Estado "
 "de Seguridad, la Secretaría de Estado de Digitalización e Inteligencia Artificial, la <b>AESIA</b>, la "
 "Secretaría de Estado de Telecomunicaciones e Infraestructuras Digitales y el <b>INCIBE</b>. Y según la nota "
 "de INÉS del 28 de octubre, las novedades de la herramienta «se presentarán en el módulo del Esquema Nacional "
 "de Seguridad (Sala 6)».",
 "Dos razones para que esto esté en el boletín y no solo en una agenda. La primera es de calendario personal: "
 "si trabajas con sector público español y no tienes la inscripción hecha, el aforo de estas jornadas se agota "
 "antes del plazo todos los años, y el módulo del ENS es donde se van a explicar el cuestionario nuevo de INÉS "
 "y la migración al PCE-RFS, que son precisamente los dos puntos sobre los que la nota del CCN no publica "
 "plazos. Si necesitas esas fechas, ahí es donde se van a decir. La segunda es de lectura estratégica, y "
 "aprovecha gratis: el <b>lema</b> de la edición vigésima del principal foro del CCN es IA ofensiva y amenaza "
 "cuántica. Eso te dice, mejor que cualquier informe de tendencias, dónde va a poner el regulador español sus "
 "exigencias en los próximos dos años, y encaja exactamente con las otras dos cosas que el CCN ha hecho esta "
 "misma semana, la metodología de evaluación de IA, y con el memorando poscuántico que el Banco de España firmó "
 "el 23 de octubre. Tres organismos españoles distintos apuntando al mismo par de riesgos en siete días no es "
 "casualidad: es una agenda.",
 'La <a href="https://www.ccn.cni.es/es/actualidad-ccn/1397-abiertas-las-inscripciones-para-las-xx-jornadas-'
 'stic" @L>nota del CCN de 20 de octubre de 2026</a> y la '
 '<a href="https://jornadas.ccn-cert.cni.es/es/" @L>web oficial de las Jornadas STIC</a>.',
 "Nota de verificación menor: la web oficial de las jornadas confirma «Noviembre 2026, XX Jornadas STIC» pero "
 "<b>no publica las fechas exactas</b>. El 24 al 27 está acreditado por la nota del CCN, no por la web del "
 "evento."),
]

ITEMS += [

("eu", "Reglamento de Ciberresiliencia · censo europeo, reverificado el 2 de noviembre de 2026", True,
 "A 39 días de la fecha que la propia norma se fijó, sigue habiendo cero organismos notificados en los "
 "veintisiete Estados, y España sigue sin figurar entre los quince con autoridad notificante",
 "Reverificado esta misma mañana y con el documento fechado en la mano, que es lo que lo hace citable. La lista "
 "oficial de organismos notificados del <b>Reglamento (UE) 2024/2847</b> que publica la propia Comisión lleva "
 "impreso «<b>Creation Date: 02/11/2026</b>» y dice literalmente: «LIST OF BODIES NOTIFIED UNDER: Regulation "
 "(EU) 2024/2847 [...] <b>No entries found</b>». Es decir, <b>cero organismos notificados en toda la Unión</b>, "
 "sin cambio respecto de la semana pasada. Y la prueba de control, que es obligatoria porque un campo mal "
 "puesto da ceros falsos: la misma consulta sobre el <b>EUCC</b>, Reglamento (UE) 2024/482, devuelve un "
 "documento de <b>trece páginas</b> con organismos reales, y el reglamento de máquinas devuelve 240 kilobytes "
 "de registros. El mecanismo funciona. Las autoridades notificantes siguen siendo <b>dieciséis en quince "
 "Estados</b>, con Bélgica aportando dos, y <b>España no aparece</b>, pese a tener nueve autoridades "
 "notificantes registradas para otras legislaciones. El plazo del <b>artículo 35.2</b> es el <b>11 de "
 "diciembre de 2026</b>: 39 días.",
 "Lo primero es decir con precisión qué es ese plazo, porque la diferencia entre informar y alarmar está "
 "justamente aquí y es el error más fácil de la semana: el artículo 35.2 obliga a <b>los Estados miembros</b> y "
 "no a las empresas, es una obligación <b>de medios</b> porque el texto dice que «se esforzarán por garantizar» "
 "que haya «un número suficiente de organismos notificados en la Unión», y su umbral es <b>agregado en la "
 "Unión</b>, no un cupo por país. Que España no tenga autoridad notificante no la pone en incumplimiento por sí "
 "solo, pero la deja <b>sin canal</b> para notificar organismos cuando los haya. Lo que sí es para el cliente "
 "es un termómetro de cuello de botella, y la acción es de calendario, no de expediente. Si fabrica producto de "
 "las clases del anexo III y va a necesitar un tercero que evalúe la conformidad antes del <b>11 de diciembre "
 "de 2027</b>, hoy hay cero capacidad en la Unión y el mercado de evaluación va a abrirse con demanda "
 "acumulada de tres años. La acción de este trimestre no es cerrar un expediente: es <b>reservar capacidad</b> "
 "y, si el producto es español, asumir que el organismo será de otro Estado.",
 'La <a href="https://webgate.ec.europa.eu/single-market-compliance-space/notified-bodies/notifying-authorities'
 '?filter=legislationId:167953" @L>consulta de autoridades notificantes del Reglamento 2024/2847 en el censo '
 'europeo</a>, que muestra «Search results (16)», y la lista oficial en PDF de organismos notificados de esa '
 'misma norma, que se genera al día y hoy dice «No entries found».',
 "Corrección de método respecto de lo que este boletín venía anotando, y es una mejora: la vía fiable para "
 "reverificar esto cada lunes <b>no es</b> el endpoint de búsqueda interno, que exige una clave incrustada en "
 "el frontal, sino el <b>PDF oficial de listas</b> de la Comisión, que no necesita clave, va autofechado con "
 "su fecha de generación y es más primario, porque es el documento que publica la propia Comisión. Los "
 "identificadores de legislación verificados siguen siendo: Reglamento de Ciberresiliencia <b>167953</b>, EUCC "
 "<b>164702</b>, Reglamento de IA <b>168380</b> y reglamento de máquinas <b>162400</b>. El del Reglamento de IA "
 "también devuelve «No entries found», por si alguien lo necesita."),

("eu", "Diario Oficial de la Unión Europea · del 26 al 30 de octubre de 2026", True,
 "Cero actos sobre NIS2, entidades críticas, ciberresiliencia, DORA o IA en 271 actos publicados, con el texto "
 "de 260 de ellos abierto y no solo el título",
 "Semana vacía en lo normativo europeo, y la ausencia está medida. Barrido día a día por el repositorio de la "
 "Oficina de Publicaciones: <b>271 actos</b> con identificador único, <b>76 de la serie L y 194 de la serie "
 "C</b>, repartidos en 103 el lunes 26, 37 el 27, 50 el 28, 41 el 29 y 40 el 30; el 31 de octubre y el 1 de "
 "noviembre fueron sábado y domingo y no hubo publicación. De esos 271 se abrió el <b>texto íntegro de 260</b>, "
 "no solo el título, precisamente porque un barrido por título produce falsos negativos. Resultado: <b>cero "
 "menciones</b> de la Directiva 2022/2555, de la 2022/2557, del Reglamento 2024/2847, del 2022/2554 o del "
 "2024/1689, y cero de «CSIRT», «punto único de contacto» o «resiliencia de las entidades críticas». Los once "
 "actos que no se pudieron abrir son todos correcciones de errores cuyo acto base está identificado y ninguno "
 "es de estas normas. Los cinco actos que mencionan «ciberseguridad» son cuatro dictámenes del Comité de las "
 "Regiones y una decisión del Consejo sobre créditos a la exportación.",
 "Decir que una semana está vacía y poder demostrarlo es, en este boletín, tan valioso como encontrar algo, y "
 "esta vez tiene un uso concreto. Si llevas un cuadro de mando normativo para un cliente, esta semana la "
 "casilla europea se cierra en cero con una cifra detrás, y eso vale para desmontar cualquier alerta que le "
 "llegue por otro canal. Pero hay una lectura menos obvia y más útil para el próximo trimestre: el último acto "
 "publicado que citaba NIS2 es del <b>14 de octubre de 2026</b>, el Reglamento 2026/2266. Tres semanas sin que "
 "ninguna norma europea nueva invoque NIS2, sumadas a cero medidas nacionales de transposición notificadas en "
 "la ventana, dibujan una pausa real en la maquinaria, no un hueco de barrido. La actividad europea en "
 "ciberseguridad se ha desplazado del Diario Oficial al Parlamento, donde los tres expedientes que reabren el "
 "marco siguen en comisión, y a los organismos técnicos. Conviene que tu cliente sepa que lo que viene no "
 "llegará por el diario oficial en los próximos meses, sino por una votación en comisión.",
 'Las dos correcciones de errores de la ventana, para quien las necesite: la del Reglamento de Identidad '
 'Digital Europea, <a href="http://data.europa.eu/eli/reg/2024/1183/corrigendum/2026-10-29/oj" @L>publicada el '
 '29 de octubre</a>, y la del Reglamento de Datos, '
 '<a href="http://data.europa.eu/eli/reg/2023/2854/corrigendum/2026-10-30/oj" @L>publicada el 30 de '
 'octubre</a>.',
 "Las dos correcciones de errores de la semana no afectan a la versión española y conviene decirlo para que "
 "nadie pierda una tarde: la del <b>Reglamento de Identidad Digital Europea</b> corrige solo la versión "
 "<b>eslovaca</b>, que empleaba «zabezpečenie», seguridad, donde debía decir «záruka», garantía, al hablar de "
 "los <b>niveles de garantía</b>, con cinco modificaciones en considerandos y en los artículos 5a y 12a. La del "
 "<b>Reglamento de Datos</b> corrige solo la versión <b>danesa</b>, en el párrafo segundo del artículo 7.1, "
 "donde decía «productos conectados suministrados por una mediana empresa» y debe decir «servicios relacionados "
 "prestados por una empresa que ha sido una mediana empresa». Las dos son terminológicas y no sustantivas, pero "
 "la segunda tiene un reflejo interpretativo que sirve para cualquier versión lingüística: confirma que el "
 "artículo 7.1 se lee en clave de <b>empresa que ha sido mediana</b>, es decir con periodo de arrastre."),

("eu", "Alemania · currículo del BSI para órganos de dirección, 28 de octubre de 2026", True,
 "La agencia federal alemana publica un currículo de formación en NIS2 para consejos de administración, y es "
 "el primer material oficial europeo que concreta el deber de formación del artículo 20.2",
 "El <b>28 de octubre</b> el <b>BSI</b> presentó un «<b>Curriculum für NIS2-Geschäftsleitungsschulung</b>», es "
 "decir un currículo de formación en NIS2 dirigido a los <b>órganos de dirección</b>. Dos días antes, el "
 "<b>26 de octubre</b>, había publicado además el <b>BSI-Standard 300-1</b> con la metodología "
 "<b>Grundschutz++</b>, que es la revisión de su marco de protección básica. Las dos son las únicas "
 "publicaciones del BSI en la ventana y las dos son institucionales, no alertas de amenaza.",
 "Esto resuelve un problema que tiene literalmente todo el que vende cumplimiento de NIS2 en España, y es la "
 "pregunta «¿y qué formación tiene que hacer exactamente el consejo?». El <b>artículo 20.2</b> de NIS2 obliga a "
 "los Estados a velar por que los miembros de los órganos de dirección «sigan una formación» y a que ofrezcan "
 "formación similar a sus empleados, pero la directiva <b>no dice de qué</b>, cuántas horas ni con qué "
 "evaluación. Ese vacío es lo que hace que las propuestas de formación a consejos sean hoy un folio en blanco "
 "que cada consultora rellena a su gusto, y lo que hace que un cliente no pueda acreditar que cumplió. Ahora "
 "hay un currículo publicado por la agencia de ciberseguridad del Estado miembro más avanzado en transposición, "
 "y eso te sirve en España aunque España no haya transpuesto: como <b>referencia de suficiencia</b> frente al "
 "cliente y, el día que haya ley española, como base de la que partir en vez de improvisar. Si tienes una "
 "oferta de formación a consejos en el cajón, revísala contra este documento antes de presentarla; y si tu "
 "cliente ya hizo una formación de consejo, compárala, porque el contraste es el mejor argumento para una "
 "segunda fase.",
 'El <a href="https://www.bsi.bund.de/DE/Service-Navi/Presse/Alle-Meldungen-News/alle-meldungen-news_node.html" '
 '@L>listado de novedades del BSI</a>, donde figuran la presentación del currículo del 28 de octubre y el '
 'BSI-Standard 300-1 del 26.',
 "Lo que aquí se afirma es la <b>existencia y la fecha</b> de las dos publicaciones, verificadas en el listado "
 "de novedades del BSI. El <b>contenido del currículo no se ha leído</b>: el BSI sirve sus documentos y sus "
 "notas de prensa por un canal que no responde al acceso automatizado en este entorno. De modo que no se "
 "describe aquí qué módulos tiene ni cuántas horas prevé, y quien quiera usarlo tendrá que descargarlo. Se "
 "declara también que el <b>canal de avisos técnicos del BSI</b>, que es distinto del de noticias, queda <b>no "
 "reconfirmado en fuente primaria esta semana</b>."),

("eu", "Parlamento Europeo · los tres expedientes que reabren el marco", True,
 "Son dos los expedientes que modifican NIS2, no uno, y solo uno tiene fecha de pleno publicada: el 8 de marzo "
 "de 2027",
 "Ninguno de los tres se movió en la ventana, y conviene fijar el mapa porque confundirlos lleva a dar la fecha "
 "equivocada. <b>Primero</b>, el <b>Digital Omnibus</b>, expediente <b>2025/0360(COD)</b>, propuesta COM(2025) "
 "837 de 19 de noviembre de 2025, que modifica a la vez NIS2, CER, DORA, el RGPD y el Reglamento de Datos entre "
 "otros, y deroga cuatro normas: en comisión conjunta de Industria y Libertades Civiles, estado «a la espera de "
 "decisión en comisión», con enmiendas de 27 de julio de 2026 y <b>sin fecha de pleno publicada</b>. "
 "<b>Segundo</b>, la <b>modificación específica de NIS2</b>, expediente <b>2026/0012(COD)</b>, propuesta "
 "COM(2026) 013 de 14 de enero de 2026, «en lo relativo a medidas de simplificación y alineación con el "
 "Reglamento de Ciberseguridad 2»: proyecto de informe de 24 de septiembre, enmiendas de 13 de octubre, y "
 "<b>fecha indicativa de pleno en primera lectura el 8 de marzo de 2027</b>, que es la única fecha publicada de "
 "los tres. <b>Tercero</b>, el <b>CSA2</b>, expediente <b>2026/0011(COD)</b>, COM(2026) 011 de 20 de enero de "
 "2026, que <b>deroga</b> el Reglamento (UE) 2019/881: cuatro conjuntos de enmiendas de 13 de octubre y sin "
 "fecha de pleno. La comisión de Industria no se reunió en la ventana, y lo confirma su propio aviso del 27 de "
 "octubre, que fija sus próximas reuniones el 10, el 19 y el 30 de noviembre y el 1 de diciembre.",
 "Importa por una razón de estrategia que conviene trasladar a cualquier cliente que esté ahora mismo "
 "preparándose para NIS2: <b>el marco se va a mover antes de que España lo transponga</b>. Esa es la "
 "singularidad española de este momento y nadie se la está contando. Con las Cámaras sin constituir hasta el 23 "
 "de diciembre y la previsión de ley ordinaria en el segundo semestre de 2027, es perfectamente posible que "
 "España transponga <b>una NIS2 ya modificada</b> por los dos expedientes anteriores, de modo que invertir hoy "
 "en adaptarse al detalle literal de la directiva de 2022 tiene un riesgo de obsolescencia real. La "
 "recomendación defendible es la que separa capas: lo que está en el <b>artículo 21</b>, gestión de riesgos, "
 "cadena de suministro, gestión de vulnerabilidades y continuidad, no va a cambiar de fondo y se puede hacer ya "
 "con tranquilidad; lo que depende de umbrales, categorías de entidad, formularios y plazos de notificación es "
 "lo que conviene dejar en borrador. Y una precisión para no quedar mal: la fecha del 8 de marzo de 2027 es "
 "<b>indicativa</b> y es solo del expediente de modificación de NIS2, no del Digital Omnibus.",
 'Las fichas de procedimiento del <a href="https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference='
 '2025/0360(COD)" @L>Digital Omnibus</a>, de la '
 '<a href="https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2026/0012(COD)" @L>modificación de '
 'NIS2</a> y del <a href="https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2026/0011(COD)" '
 '@L>Reglamento de Ciberseguridad 2</a>.',
 "Dato español que conviene registrar porque casi nadie lo cita: el <b>Parlamento español presentó "
 "contribución</b> sobre los dos expedientes, el de NIS2 y el de CSA2, el <b>15 de abril de 2026</b>, y el "
 "Senado francés emitió dictamen motivado sobre los dos el 1 de junio. Y un aviso de método para no inflar "
 "actividad: en las fichas de procedimiento aparecen reuniones con fechas del 23 al 28 de octubre, dentro de la "
 "ventana, pero son <b>reuniones de ponentes con representantes de intereses</b> registradas en el apartado de "
 "transparencia. Son contactos de lobby, no trámites legislativos, y presentarlos como hitos de procedimiento "
 "sería un error."),

("eu", "ENISA · comparecencia del 10 de noviembre de 2026", False,
 "El director ejecutivo de ENISA presenta en ocho días el informe que es la radiografía oficial del grado de "
 "aplicación de NIS2 en la Unión",
 "El <b>30 de octubre</b> la comisión de Industria del Parlamento Europeo anunció que el director ejecutivo de "
 "<b>ENISA</b>, Juhan Lepassaar, presentará el <b>Informe sobre el Estado de la Ciberseguridad en la Unión</b> "
 "el <b>10 de noviembre de 2026</b>. El anuncio dice que la comparecencia «brinda a los miembros de Industria "
 "una oportunidad importante de evaluar la preparación, las capacidades y las vulnerabilidades de Europa en "
 "ciberseguridad», y que el informe «ofrece una evaluación basada en datos del panorama de la ciberseguridad en "
 "la UE e identifica los ámbitos que requieren mayor actuación, incluida <b>la aplicación de la legislación</b>, "
 "la gestión de crisis cibernéticas, la seguridad de la cadena de suministro y el desarrollo de capacidades». "
 "Al margen de esto, <b>ENISA no publicó nada en la ventana</b>: su última entrada es del 21 de octubre, la "
 "declaración conjunta sobre PHP, y su última publicación del 22, un informe técnico sobre inventarios de "
 "componentes de software.",
 "No es un plazo de cumplimiento y no hay que hacer nada el día 10, pero conviene tenerlo marcado por una razón "
 "muy concreta: ese informe es el documento del artículo 18 del Reglamento de Ciberseguridad, es decir <b>la "
 "evaluación oficial de la Unión sobre cómo va la aplicación de NIS2</b>, con datos y por Estado. Para quien "
 "asesora clientes españoles, es la fuente institucional que permite decir «España va retrasada» sin que suene "
 "a opinión de consultor, y el contexto que explica por qué la Comisión mantiene dos recursos vivos contra "
 "España. Si tienes una presentación de dirección prevista para finales de noviembre o para diciembre, merece "
 "la pena esperar a ese informe antes de cerrar las cifras: es gratis, es oficial y es de hace dos semanas. Y "
 "si tu cliente es proveedor de alguna entidad esencial, el capítulo de seguridad de la cadena de suministro "
 "del informe suele ser el que marca lo que los supervisores nacionales empiezan a pedir el año siguiente.",
 'El <a href="https://www.europarl.europa.eu/committees/en/enisa-executive-director-to-present-itre/product-'
 'details/20261030CAN79838" @L>aviso de la comisión de Industria del Parlamento Europeo de 30 de octubre de '
 '2026</a>.',
 None),

("eu", "Transposición de NIS2 y CER · medidas nacionales, al 1 de noviembre de 2026", True,
 "Cero medidas nacionales notificadas en la ventana, y España es el único Estado con cero medidas en las dos "
 "directivas a la vez",
 "Barrido del repositorio europeo de medidas nacionales de ejecución con el predicado correcto, que es el de "
 "<b>fecha de notificación</b> y no el de fecha de documento. Resultado en la ventana: <b>cero medidas</b> "
 "notificadas para las dos directivas. Los totales, que son la cifra que de verdad sirve para situar a España: "
 "<b>NIS2</b> acumula <b>305 medidas notificadas de 25 de los 27 Estados</b>, y los dos que no han notificado "
 "<b>ninguna</b> son <b>España e Irlanda</b>; la última notificación fue de <b>Hungría, el 21 de octubre</b>, "
 "cinco días antes de la ventana. <b>CER</b> acumula <b>221 medidas de 24 de los 27</b>, y los tres sin "
 "ninguna son <b>España, Bulgaria y Suecia</b>; la última fue de <b>Dinamarca, el 1 de octubre</b>. No hay "
 "paquete de infracciones nuevo: el último es de <b>decisión de 30 de septiembre con comunicado de 1 de "
 "octubre</b>, leído íntegro, con cero menciones de NIS2 o de CER. Y ninguna designación nueva de autoridad "
 "competente, punto único de contacto o CSIRT publicada en la ventana.",
 "La cifra que conviene memorizar es esta: <b>España es el único Estado de la Unión con cero medidas "
 "notificadas en las dos directivas a la vez</b>. Irlanda está a cero en NIS2 pero ha notificado en CER; "
 "Bulgaria y Suecia están a cero en CER pero han notificado en NIS2. España, en las dos. Es un dato duro, "
 "comprobable y mucho más persuasivo que cualquier adjetivo, y es el que hace creíble ante una dirección que "
 "las sanciones del Tribunal de Justicia no son una amenaza retórica. Pero hay un matiz que hay que dar sí o sí "
 "cuando se cita este cuadro, porque un cliente avispado lo usará en contra: <b>haber notificado alguna medida "
 "no equivale a haber transpuesto</b>. Francia notificó quince medidas de NIS2 el 19 de julio y Países Bajos "
 "tres entre el 10 y el 16 del mismo mes, es decir <b>después</b> de que la Comisión decidiera llevarlos al "
 "Tribunal el 8 de julio, y los dos siguen demandados, porque la remisión es por no notificar la transposición "
 "<b>completa</b>. De modo que el cuadro mide actividad legislativa, no cumplimiento. Lo que no admite matiz es "
 "el cero.",
 'La <a href="https://eur-lex.europa.eu/legal-content/ES/NIM/?uri=CELEX:32022L2555" @L>relación de medidas '
 'nacionales de ejecución de la Directiva (UE) 2022/2555</a> y la '
 '<a href="https://eur-lex.europa.eu/legal-content/ES/NIM/?uri=CELEX:32022L2557" @L>de la Directiva (UE) '
 '2022/2557</a>, y el <a href="https://ec.europa.eu/commission/presscorner/detail/en/inf_26_1760" @L>último '
 'paquete de infracciones, de 30 de septiembre de 2026</a>.',
 "Dos cosas que se declaran. Una laguna temporal residual: el repositorio europeo ingiere las medidas "
 "nacionales con un desfase de dos a seis días, y se ha comprobado que el 30 de octubre había ingerido "
 "notificaciones de hasta el 29, de modo que el cero es <b>firme del 26 al 29 de octubre</b> y queda un punto "
 "ciego de viernes a domingo que se reconfirmará el lunes próximo. Y un cabo suelto que conviene registrar: de "
 "los siete Estados que la Comisión decidió llevar al Tribunal por CER el 28 de abril, seis tienen recurso con "
 "número de asunto publicado y <b>Luxemburgo no</b>; notificó una medida el 6 de mayo, ocho días después de la "
 "decisión, lo que explicaría de forma plausible que no haya recurso o que se desistiera, pero <b>no se ha "
 "encontrado fuente primaria de archivo</b> y por tanto es hipótesis, no hecho."),

("eu", "Consejo y Consejo Europeo · del 26 de octubre al 1 de noviembre de 2026", False,
 "Ningún acto, posición ni enfoque general sobre ciberseguridad o digital, y el próximo Consejo Europeo no es "
 "hasta el 17 y 18 de diciembre",
 "Comprobado el listado completo de comunicados del Consejo de la ventana: marco financiero plurianual y "
 "política agrícola el 26, posibilidades de pesca del Báltico, apoyo a Ucrania, renovación de un régimen de "
 "sanciones, asistencia a Mauritania, financiación climática y la cumbre bilateral <b>UE-Canadá</b> en Montreal "
 "los días 29 y 30. <b>Ningún acto adoptado, ninguna posición y ningún enfoque general sobre ciberseguridad o "
 "materia digital.</b> Y un dato que conviene fijar porque es el antídoto contra un bulo recurrente: el propio "
 "Consejo publicó el <b>26 de octubre</b> un aviso a medios que dice que «el Consejo Europeo tendrá lugar los "
 "<b>días 17 y 18 de diciembre de 2026</b>». El anterior fue el 15 y 16 de octubre. En la ventana <b>no hubo "
 "Consejo Europeo</b>. Lo único de la cumbre de Montreal con carga digital es la conclusión de las "
 "negociaciones sustantivas de un Acuerdo de Comercio Digital con Canadá y la incorporación de Canadá como "
 "Estado participante de la empresa común de supercomputación europea, más dos memorandos ya firmados sobre IA "
 "y sobre credenciales e identidad digital.",
 "Esto sirve para una sola cosa, y es defensiva: cerrar la puerta a datos fabricados. La formulación "
 "«conclusiones del Consejo Europeo sobre soberanía digital» es una de las que más circula en resúmenes "
 "automáticos y boletines de terceros, y es especialmente peligrosa porque suena exactamente a lo que un "
 "cliente espera oír. Si en los próximos días ves esa frase con cualquier fecha entre el 26 de octubre y el 1 "
 "de noviembre, es falsa por construcción: no hubo reunión. La cumbre con Canadá, que sí existió y sí es de "
 "esos días, es una cumbre bilateral y <b>no produce conclusiones del Consejo Europeo</b>, y su declaración "
 "conjunta es política, sin efectos jurídicos directos ni obligaciones para entidades. La fecha que de verdad "
 "hay que apuntar en la agenda es el <b>17 y 18 de diciembre</b>: es el primer foro donde podría aparecer una "
 "conclusión sobre soberanía digital con valor político real, y cae justo antes de que se constituyan las "
 "Cámaras españolas.",
 'El <a href="https://www.consilium.europa.eu/en/press/press-releases/2026/10/26/media-advisory-accreditation-'
 'for-the-european-council-17-and-18-december-2026/" @L>aviso a medios del Consejo de 26 de octubre de 2026</a>, '
 'que fija el Consejo Europeo del 17 y 18 de diciembre.',
 None),

("eu", "Comisión Europea · novedades digitales de la ventana", False,
 "Diez entradas en el canal digital de la Comisión y ninguna de ciberseguridad: lo más cerca que llega es una "
 "mesa con bancos y plataformas sobre estafas en línea, que no abre consulta",
 "Comprobadas las diez entradas publicadas en el canal de estrategia digital de la Comisión entre el 26 de "
 "octubre y el 1 de noviembre: aceptación del plan de medidas correctoras de Temu bajo el Reglamento de "
 "Servicios Digitales el 26; una mesa de la Comisión con bancos y plataformas en línea contra las estafas, "
 "también el 26; ayuda estatal austriaca a una planta de semiconductores el 27; duodécimo plenario del Código "
 "de Conducta sobre Desinformación el 28; investigación en profundidad del mercado sueco de acceso local y "
 "decisiones del código de comunicaciones electrónicas el 29; y el 30, cuatro entradas de cooperación con "
 "Canadá, el foro de mundos virtuales en Valencia y una adjudicación de la nube europea de ciencia abierta. "
 "<b>Ninguna sobre NIS2, Reglamento de Ciberresiliencia, CER, Reglamento de Ciberseguridad 2 ni los esquemas de "
 "certificación.</b> La de estafas en línea se abrió y comprobó: su apartado de próximos pasos dice que «a "
 "principios de noviembre la Comisión se reunirá también con los prestadores de plataformas en línea de muy "
 "gran tamaño», de modo que <b>no es una consulta pública con fecha de cierre</b>, son reuniones sectoriales "
 "por invitación.",
 "El único valor práctico es que te ahorra una falsa alarma. «La Comisión abre un proceso sobre estafas en "
 "línea» es el tipo de titular que llega a un cliente del sector financiero y genera una pregunta urgente el "
 "lunes por la mañana; la respuesta correcta es que no hay nada que hacer, porque no hay consulta abierta, no "
 "hay plazo y no hay obligación. Lo que sí conviene retener, por si el expediente avanza, es la base: artículo "
 "45 del Reglamento de Servicios Digitales, es decir la vía de los <b>códigos de conducta</b>, y el destino "
 "declarado es decidir «si procede elaborar un código de conducta» después de oír a la Junta Europea de "
 "Servicios Digitales y al grupo de expertos de sistemas de pago. Si un código llega a existir, la adhesión "
 "será voluntaria pero funcionará como estándar de diligencia frente al supervisor, que es exactamente cómo ha "
 "funcionado el de desinformación. Ese es el momento de preocuparse, y no es este.",
 'El <a href="https://digital-strategy.ec.europa.eu/en/news" @L>canal de novedades de estrategia digital de la '
 'Comisión Europea</a> y la entrada sobre '
 '<a href="https://digital-strategy.ec.europa.eu/en/news/commission-brings-banks-and-online-platforms-together-'
 'fight-against-online-scams" @L>la mesa con bancos y plataformas contra las estafas en línea</a>.',
 None),
]

ITEMS += [

("fin", "Registro de criptoactivos de la ESMA · comprobado el 2 de noviembre de 2026", True,
 "El mayor robo de criptoactivos de la historia, 6.300 millones de dólares, no generó ni una sola notificación "
 "a un supervisor europeo, y la razón está en un fichero público que se comprueba en dos minutos",
 "Hallazgo propio de esta edición, hecho en fuente primaria y con prueba de control. El <b>29 de octubre</b> "
 "<b>Binance</b> sufrió el compromiso de sus carteras calientes y la pérdida de unos <b>6.300 millones de "
 "dólares</b>, confirmado por la entidad en cinco comunicados propios y atribuido por el <b>FBI</b> el 31 de "
 "octubre a un actor estatal. La pregunta de cumplimiento que todo el mundo da por supuesta es qué notificó a "
 "los supervisores europeos, y la respuesta es <b>nada, y no por un vacío legal</b>. Descargados los ficheros "
 "oficiales del registro de proveedores de servicios de criptoactivos de la <b>ESMA</b>, con última "
 "actualización declarada de <b>30 de octubre de 2026</b>: hay <b>460 entidades autorizadas</b> bajo el "
 "<b>Reglamento de Mercados de Criptoactivos</b> y <b>Binance no figura entre ellas</b>, probadas todas sus "
 "denominaciones; tampoco figura en el fichero de <b>188 entidades no conformes</b>, de modo que ninguna "
 "autoridad nacional la ha listado formalmente como tal. La prueba de control valida el negativo: en ese mismo "
 "fichero <b>sí</b> aparecen Coinbase, Kraken, Bybit, OKX, Crypto.com y Gemini, y constan dieciséis "
 "proveedores con Estado miembro de origen España.",
 "La cadena de consecuencias es la pieza aprovechable, y conviene recorrerla entera porque casi nadie la hace. "
 "Si la entidad <b>no está autorizada</b> bajo el Reglamento de Mercados de Criptoactivos, entonces <b>no es "
 "entidad financiera del artículo 2 de DORA</b> por la vía del proveedor de criptoactivos; si no lo es, <b>no "
 "tiene autoridad competente europea</b>; y si no la tiene, el incidente <b>no disparó la notificación de "
 "incidente grave del artículo 19</b>, ni el plazo inicial, ni el intermedio, ni el informe final. La <b>CNMV "
 "no es su autoridad competente</b> aunque sea la autoridad de criptoactivos en España. Para un consultor esto "
 "se convierte en una pregunta de diligencia debida que cuesta dos minutos y que nadie está haciendo: antes de "
 "contratar un proveedor de servicios de criptoactivos, o de aceptar que un cliente opere con él, "
 "<b>comprueba si figura en el registro de la ESMA</b>. No es una formalidad: de ahí depende que exista un "
 "supervisor al que reclamar, un régimen de notificación que te alcance cuando el proveedor sufra un "
 "incidente, y un interlocutor distinto del servicio de atención al cliente. Esta semana ese fichero separa a "
 "seis casas de cambio conocidas de una, y la que queda fuera es la que ha perdido 6.300 millones. Y hay un "
 "segundo uso, para quien asesore a entidades que <b>sí</b> están dentro: el mismo registro es la forma de "
 "comprobar si un socio comercial está en el perímetro, lo que importa para el riesgo de terceros de los "
 "artículos 28 a 30 de DORA.",
 'El <a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-'
 'regulation-mica" @L>registro de proveedores de servicios de criptoactivos de la ESMA</a>, cuyos dos ficheros '
 'de entidades autorizadas y de entidades no conformes se descargan directamente desde esa página, y la '
 '<a href="https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-'
 'attack" @L>alerta de atribución del FBI de 31 de octubre de 2026</a>.',
 "Dos cautelas. La primera, sobre el alcance de lo que aquí se afirma: lo verificado es la <b>ausencia en el "
 "registro</b> y la cadena jurídica que de ella se sigue. <b>Por qué</b> no está autorizada es otra cuestión, y "
 "ahí lo único primario es el contexto general, es decir la declaración pública de la ESMA de junio de 2026 "
 "instando a los proveedores no autorizados a cesar su actividad y el fin del régimen transitorio del artículo "
 "143.3 el 1 de julio de 2026. Lo que circula en prensa sobre registros nacionales caducados y sobre atención a "
 "clientes europeos al amparo de la solicitud inversa <b>no se ha verificado en fuente primaria</b> y no se "
 "publica aquí como hecho. La segunda: <b>ningún regulador europeo ni ningún CERT oficial ha publicado una sola "
 "línea</b> sobre este incidente, comprobado abriendo ESMA, EBA, CNMV, Banco de España, la autoridad maltesa, "
 "CERT-EU, CERT-FR, INCIBE-CERT y CCN-CERT. La autoridad francesa no se ha podido alcanzar y queda declarada "
 "como laguna, aunque pesa poco porque no es su autoridad competente."),

("fin", "BCE · venció el 31 de octubre de 2026 el plazo de la carta SSM-2026-0301", True,
 "Las entidades significativas ya han entregado su plan contra la ciberamenaza potenciada por IA, el "
 "supervisor no ha dicho una palabra desde entonces, y la única voz de la semana avisa de que la evaluación de "
 "fondo empieza ahora",
 "El plazo venció el <b>sábado 31 de octubre</b>, dentro de la ventana. La carta que lo fijaba, leída íntegra, "
 "es la <b>SSM-2026-0301</b> de <b>7 de julio de 2026</b>, «Addressing AI-enabled cybersecurity threats», "
 "firmada por la presidenta del Consejo de Supervisión y dirigida al consejero delegado de cada entidad "
 "significativa: «este plan de acción debe remitirse al <b>equipo conjunto de supervisión</b> correspondiente a "
 "más tardar el 31 de octubre de 2026». La carta anuncia que el BCE «realizará un <b>análisis horizontal</b> de "
 "los planes de acción remitidos» y «compartirá las conclusiones de este análisis con las entidades "
 "significativas», y que «el equipo conjunto seguirá interactuando con la entidad para analizar el plan de "
 "acción y vigilará su progreso». Tras el vencimiento, <b>silencio formal comprobado en cinco canales</b>: ni "
 "nota de prensa, ni entrada del blog de supervisión, cuya última es del 5 de octubre, ni boletín de "
 "supervisión, cuyo último es del 12 de agosto, ni carta nueva a las entidades, ni declaración institucional. "
 "La única declaración verificable y fechada en la ventana es una entrevista del <b>30 de octubre</b> de Pedro "
 "Machado, miembro del Consejo de Supervisión.",
 "Lo noticiable no es que el BCE haya dicho algo nuevo, porque no lo ha dicho: es que el reloj cambió de dueño. "
 "Hasta el sábado la pelota estaba en la entidad; desde el lunes está en el equipo conjunto de supervisión, y "
 "eso tiene tres consecuencias prácticas que conviene llevar a cualquier cliente supervisado. La primera y más "
 "incómoda es la <b>comparación horizontal</b>: el plan de tu cliente no se va a juzgar contra la carta, se va "
 "a juzgar contra el de sus pares, de modo que un plan correcto pero conservador puede quedar por debajo de la "
 "media del sector sin haber incumplido nada. La segunda la dijo Machado con todas las letras y es la cita que "
 "hay que guardar: «<b>una evaluación más significativa y sustancial solo podrá hacerse una vez que recibamos "
 "los planes de acción de las entidades</b>». Traducido: lo que viene ahora son preguntas del equipo conjunto "
 "sobre lo que cada uno escribió, y la primera reunión de seguimiento es el momento en que se ve si el plan era "
 "un documento o un proyecto. La tercera es de prioridad declarada: Machado señala que «el mayor reto de las "
 "entidades hoy es poner en marcha <b>ejercicios de parcheo muy rápidos y eficaces</b> y asegurar la higiene "
 "cibernética de sus sistemas». Si el plan de tu cliente no tiene tiempos de parcheo medidos, ahí está el "
 "hallazgo.",
 'La <a href="https://www.bankingsupervision.europa.eu/press/letterstobanks/shared/pdf/2026/ssm.2026_letter_on_'
 'AI_enabled_cybersecurity_threats.en.pdf" @L>carta SSM-2026-0301 de 7 de julio de 2026</a> y la '
 '<a href="https://www.bankingsupervision.europa.eu/press/interviews/date/2026/html/ssm.in261030~21a824d8f2.en.'
 'html" @L>entrevista de Pedro Machado de 30 de octubre de 2026</a>.',
 "Tres fechas que la propia carta fija y que conviene no perder, porque son el calendario de lo que viene. "
 "<b>Febrero de 2027</b>: el BCE amplió a esa fecha, desde septiembre de 2026, la recogida anual del "
 "<b>Cuestionario de Riesgo TI</b>, de modo que ese es el siguiente hito con fecha cierta. <b>Sin fecha</b>: el "
 "análisis horizontal no tiene calendario público, ni lo tenía en julio ni lo ha ganado esta semana. Y "
 "<b>pendiente</b>: la carta anunciaba que el riesgo cuántico para los métodos de cifrado tradicionales se "
 "abordaría en «una carta separada en su momento», y a 1 de noviembre <b>esa carta sigue sin publicarse</b>. Es "
 "la única carta a entidades de 2026 publicada, y es la de julio. Dato de color de la misma entrevista, útil "
 "para dimensionar: «alrededor del <b>85 %</b> de las entidades ya usa IA generativa»."),

("fin", "BCE · discurso del economista jefe, 30 de octubre de 2026", True,
 "El Banco Central Europeo pone número al problema: los incidentes de TI y ciberseguridad ya son del 10 al "
 "12 % de todos los eventos de riesgo operacional, casi el doble que en 2018",
 "El <b>30 de octubre</b>, en un discurso titulado «AI adoption in Europe», el economista jefe del BCE publicó "
 "las cifras más concretas de la semana sobre ciberriesgo bancario: «el rápido avance de los modelos de IA está "
 "creando nuevos retos de ciberseguridad para las entidades al dejar al descubierto vulnerabilidades antes "
 "ocultas. Aunque es difícil determinar qué proporción de las amenazas se relaciona exclusivamente con el uso "
 "de modelos de IA, <b>los incidentes de TI, ciberseguridad y afines ya están aumentando, y suponen entre el "
 "10 % y el 12 % de todos los eventos de riesgo operacional en 2025, casi el doble de su incidencia en "
 "2018</b>». Y un segundo hallazgo, que es una desconexión: «las menciones al riesgo operacional de incidentes "
 "de ciberamenaza en las <b>presentaciones de resultados</b> siguen siendo más limitadas, en contraste con la "
 "evidencia de que las entidades se enfrentan a crecientes amenazas de ciberseguridad». Señala además que los "
 "ciberataques a sistemas de pago pueden llevar a las entidades a tirar de reservas de liquidez o a aumentar el "
 "recurso al banco central.",
 "La primera cifra es material de primera página para un comité de riesgos, y hay que usarla por lo que es: una "
 "serie temporal del supervisor, no una estimación de mercado. Que el riesgo tecnológico haya pasado de en "
 "torno al 6 % a entre el 10 y el 12 % de los eventos de riesgo operacional en siete años es el argumento "
 "cuantitativo que justifica reponderar el apetito de riesgo operacional, y viene del BCE, de modo que nadie en "
 "la sala la va a discutir. Pero la segunda observación es la que puede ganarte un proyecto, porque señala un "
 "riesgo que casi nadie está mirando: el supervisor está diciendo, con educación, que las entidades <b>hablan "
 "del ciberriesgo con él mucho más de lo que hablan con el mercado</b>. Esa brecha entre lo que se reporta al "
 "supervisor y lo que se cuenta en la presentación de resultados es, para una cotizada, un riesgo de "
 "información al mercado con ángulos de abuso de mercado y de informe de gestión, no solo un asunto de "
 "seguridad. Si tienes clientes cotizados, es una conversación que corresponde al secretario del consejo y al "
 "director financiero, no al responsable de seguridad, y nadie se la está planteando.",
 'El <a href="https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261030~08d9d540f0.en.html" @L>discurso '
 '«AI adoption in Europe» de 30 de octubre de 2026</a>.',
 None),

("fin", "EIOPA · cuadro de riesgos de octubre, 29 de octubre de 2026", True,
 "El supervisor europeo de seguros sube el ciberriesgo a nivel elevado y, lo que importa más, le pone "
 "perspectiva de empeoramiento, con la suscripción de ciberriesgo entre las causas",
 "El <b>29 de octubre</b> <b>EIOPA</b> publicó su cuadro de riesgos del seguro, referencia EIOPA-BoS-26-495, "
 "cuyo propio titular dice que «los riesgos de mercado y ciber siguen elevados en un entorno geopolíticamente "
 "complejo». El pasaje que importa es literal: «los riesgos de <b>digitalización</b> y <b>ciber</b> están en "
 "nivel elevado, <b>con una perspectiva que empeora</b>, lo que refleja la preocupación por los <b>modelos de "
 "IA de frontera</b>, los efectos de contagio digital de los conflictos geopolíticos y la <b>exposición de las "
 "aseguradoras a través de la suscripción de ciberriesgo</b>». Metodología declarada: datos de Solvencia II del "
 "segundo trimestre de 2026 y cierre de 2025, de <b>95 grupos aseguradores y 2.092 entidades individuales</b>, "
 "con datos de mercado a cierre de septiembre de 2026.",
 "Es el único dato supervisor nuevo y fechado de la semana que mueve una valoración de riesgo, y tiene dos "
 "lecturas según a quién asesores. Si tu cliente es una aseguradora, lo relevante es la tercera causa: EIOPA "
 "está señalando la <b>exposición por suscripción</b>, es decir que el riesgo no está solo en los sistemas de "
 "la entidad sino en su cartera de pólizas de ciber. Con los modelos de frontera acortando el intervalo entre "
 "vulnerabilidad y explotación, un evento como el de PHP de esta misma semana es exactamente el escenario de "
 "<b>acumulación</b> que puede activar muchas pólizas a la vez por una única causa raíz, y eso es modelización "
 "de catástrofe cibernética, no gestión de seguridad. Si tu cliente es un asegurado, la lectura es la inversa y "
 "hay que decírsela ahora: cuando el supervisor pone perspectiva de empeoramiento sobre la suscripción de "
 "ciberriesgo, lo que viene en la próxima renovación son <b>primas al alza, franquicias mayores y preguntas "
 "más duras en el cuestionario</b>. Quien tenga renovación en el primer trimestre de 2027 debería estar "
 "preparando ya las evidencias de control, y muy en particular las de tiempos de parcheo, que es justo lo que "
 "el BCE ha señalado como reto principal la misma semana.",
 'La <a href="https://www.eiopa.europa.eu/eiopa-risk-dashboard-highlights-market-and-cyber-risks-key-concerns-'
 'europes-insurers-2026-10-29_en" @L>nota de EIOPA de 29 de octubre de 2026 sobre el cuadro de riesgos</a>.',
 "No genera ningún plazo ni obligación: es un cuadro de riesgos, no un acto. Y conviene no sobreinterpretar la "
 "palabra «elevado», que en la escala de EIOPA es un nivel y no una alarma; lo que es noticia respecto del "
 "cuadro anterior es el <b>cambio de perspectiva</b>, no el nivel."),

("fin", "Banco de España · Circular 1/2026, BOE de 30 de octubre de 2026", True,
 "La única circular de un supervisor financiero español publicada esta semana refunde el régimen de la Central "
 "de Información de Riesgos, entra en vigor el 19 de noviembre y arrastra un transitorio que muere el 1 de "
 "enero",
 "El <b>30 de octubre</b> se publicó en el BOE la <b>Circular 1/2026, de 21 de octubre, del Banco de España, "
 "sobre la Central de Información de Riesgos</b>, firmada por el Gobernador. Su razón de ser la explica el "
 "preámbulo: la Circular 1/2013 «ha sido objeto de <b>sucesivas modificaciones, catorce desde su "
 "publicación</b>. La reiteración de reformas ha motivado la conveniencia de aprobar un <b>texto refundido</b> "
 "que compile en una única norma toda la regulación aplicable con el fin de superar la fragmentación normativa "
 "y reforzar la seguridad jurídica». Entra en vigor «a los <b>veinte días</b> de su publicación», es decir el "
 "<b>19 de noviembre de 2026</b>. Y lleva un régimen transitorio con fecha: «con el propósito de que las "
 "entidades puedan llevar a cabo las adaptaciones necesarias, la circular establece un régimen transitorio "
 "aplicable <b>hasta el 1 de enero de 2027</b>, por el que el umbral de exención de declaración individualizada "
 "se mantiene en <b>3.000 euros</b> hasta esa fecha». Flexibiliza además la remisión de determinados módulos de "
 "datos el día cinco del mes siguiente.",
 "Hay que ser honesto con el alcance antes de venderlo: <b>esto no es una circular de ciberseguridad ni de "
 "resiliencia operativa</b>, y presentarla como tal sería inflar la semana. Está aquí por tres razones legítimas. "
 "Una, es el único acto normativo de un supervisor financiero español en la ventana y trae <b>dos fechas duras "
 "en los próximos sesenta días</b>, lo que la convierte en el plazo financiero español más accionable del "
 "boletín. Dos, tiene carga de protección de datos y de riesgo de terceros que casi nadie le ve: la información "
 "que el Banco de España remite «tiene <b>carácter confidencial</b> y solo podrá ser usada o cedida conforme a "
 "lo dispuesto en el artículo 62 de la Ley 44/2002 y en la normativa de protección de datos», de modo que "
 "cualquier tratamiento de esos ficheros en un sistema de terceros entra de lleno en el artículo 28 del RGPD. "
 "Y tres, porque incorpora una palanca supervisora que conviene conocer: el Banco de España «podrá impedir "
 "temporalmente el acceso de una entidad declarante a los informes» si incumple sus obligaciones de información "
 "con la calidad y extensión requeridas. Es decir, un fallo de calidad del dato <b>corta el acceso</b>, y eso "
 "sí es un riesgo operacional con impacto inmediato en la concesión de crédito.",
 'La <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-22720" @L>Circular 1/2026, de 21 de octubre, '
 'del Banco de España, publicada en el BOE del 30 de octubre de 2026</a>.',
 "Nota de cómputo, por prudencia: la entrada en vigor se calcula a los veinte días de la publicación del 30 de "
 "octubre, lo que da el <b>19 de noviembre</b>. El texto no fija el día expresamente, de modo que si vas a "
 "poner esa fecha en un calendario de cliente, conviene recontar el plazo sobre el propio BOE."),

("fin", "Banco de España y Banco de Portugal · memorando de 23 de octubre de 2026", True,
 "Dos bancos centrales de la zona euro firman un programa de cooperación en criptografía poscuántica, y lo "
 "hacen justo donde el BCE lleva cuatro meses debiendo una carta",
 "Es del <b>23 de octubre</b>, tres días antes de la ventana, y entra porque pasó desapercibido y porque "
 "arrastra consecuencia. El Banco de España y el Banco de Portugal «han firmado un <b>Memorándum de "
 "Entendimiento</b> por el que se comprometen a desplegar un <b>Programa de Cooperación en Criptografía Post "
 "Cuántica</b> durante la reunión de alto nivel que han celebrado este jueves y viernes en Lisboa. El objetivo "
 "es hacer frente de forma más eficaz a los <b>riesgos emergentes de ciberseguridad y estabilidad financiera</b> "
 "que plantea el desarrollo de la computación cuántica». Lo que lo hace relevante es el encaje: la carta del "
 "BCE de julio anunciaba que el riesgo cuántico para los métodos de cifrado tradicionales se trataría en «una "
 "carta separada en su momento», y a 1 de noviembre <b>esa carta sigue sin publicarse</b>. Y la misma semana, "
 "el <b>CCN</b> ha puesto la amenaza cuántica en el lema de sus Jornadas STIC y el <b>NIST</b> ha cerrado en "
 "firme su guía de transición poscuántica.",
 "La utilidad es de anticipación, que es la mercancía más escasa en este oficio. Cuando dos bancos centrales "
 "nacionales firman un programa bilateral sobre una materia en la que su supervisor común ha anunciado una "
 "carta y no la ha emitido, lo que suele significar es que el trabajo técnico va por delante del acto "
 "supervisor y que el acto llegará. Para un cliente del sector financiero español, eso convierte la "
 "<b>criptoagilidad</b> en una conversación de este trimestre y no del año que viene, y la pregunta concreta "
 "que conviene llevarle es la que nadie sabe responder: <b>¿tiene inventariado dónde usa criptografía, con qué "
 "algoritmos y con qué vida útil del dato cifrado?</b> Sin ese inventario no hay plan de migración posible, y "
 "es lo primero que va a pedir cualquier carta del BCE cuando salga. Súmese el ángulo jurídico que casi nadie "
 "plantea: en DORA, las obligaciones criptográficas están en la sección 4 del Reglamento Delegado (UE) "
 "2024/1774, que ya exige una política de gestión de claves y de controles criptográficos con revisión de la "
 "idoneidad de los algoritmos. Es decir, la base para exigir criptoagilidad <b>ya existe</b> y no hace falta "
 "esperar a la carta.",
 'La <a href="https://www.bde.es/wbe/es/noticias-eventos/actualidad-banco-espana/notas-banco-espana/el-banco-de-'
 'espana-y-el-banco-de-portugal-refuerzan-la-cooperacion-en-migracion-a-la-criptografia-cuantica-y-riesgos-de-'
 'ciberseguridad.html" @L>nota del Banco de España de 23 de octubre de 2026</a>.',
 None),

("fin", "EBA · venció el 26 de octubre de 2026 el plazo que movió la vulnerabilidad de PHP", False,
 "Cerraron cinco consultas y no cuatro, no hubo más prórrogas, y la Autoridad ya tiene su web funcionando con "
 "normalidad",
 "Confirmado contra la página de consultas de la Autoridad: el plazo prorrogado venció el <b>26 de octubre</b>, "
 "primer día de la ventana, y <b>no hubo ninguna prórroga adicional</b>. El motivo de la prórroga lo explicó la "
 "propia <b>EBA</b> el 22 de octubre: «el 21 de octubre de 2026, <b>CERT-EU</b> alertó a las organizaciones de "
 "dos fallos críticos de seguridad en software utilizado para operar muchos sitios web, incluido el de la "
 "Autoridad Bancaria Europea. Como precaución, la EBA <b>retiró su web el miércoles 21 de octubre a las 13:00</b> "
 "mientras se aplicaban las actualizaciones de seguridad necesarias. La web se restableció el <b>jueves 22 a "
 "las 14:00</b>. La EBA <b>no ha detectado ninguna brecha</b> y ningún dato se ha visto comprometido». "
 "Precisión respecto de lo que publicó este boletín: las consultas prorrogadas eran cuatro, EBA/CP/2026/12, 13, "
 "14 y 02/10, <b>ninguna de DORA</b>, pero ese 26 de octubre cerraron en realidad <b>cinco</b>, porque la "
 "EBA/CP/2026/15, sobre pagos de garantía de depósitos de fondos de clientes, vencía ese día por su plazo "
 "original. La web responde ya con normalidad.",
 "El episodio es pequeño y es la mejor anécdota de la semana para una conversación de continuidad, por una "
 "razón: <b>el supervisor bancario europeo tuvo que apagar su propia web durante veinticinco horas por la misma "
 "vulnerabilidad que esta semana ha pasado a explotación activa confirmada</b>, y al hacerlo movió plazos "
 "regulatorios que afectaban a todo el sector. Es el ejemplo perfecto de que una vulnerabilidad de componente "
 "no es un problema del equipo de sistemas: tiene efectos de calendario regulatorio. Llévalo al cliente que "
 "todavía discute si su web institucional es un activo crítico. Y repárese en lo bien hecho que está el "
 "comunicado, que vale como plantilla: dice la fecha y la hora exacta de apagado y de restablecimiento, dice "
 "qué no ha pasado, «no ha detectado ninguna brecha y ningún dato se ha visto comprometido», y dice qué plazos "
 "se mueven y hasta cuándo. Tres cosas que casi ningún comunicado de incidente contiene.",
 'La <a href="https://www.eba.europa.eu/publications-and-media/consultations" @L>página de consultas de la '
 'Autoridad Bancaria Europea</a>, donde las cinco consultas figuran con rango de 23 de julio al 26 de octubre '
 'de 2026.',
 "Discrepancia de ficha que conviene conocer si alguien va a reconstruir este expediente: la página de "
 "consultas sigue mostrando para la <b>EBA/CP/2026/02/10</b>, sobre la metodología de imposición de multas en "
 "el reglamento de criptoactivos, su rango original del 26 de junio al 28 de septiembre, <b>sin reflejar la "
 "prórroga</b> que sí recoge la nota del 22 de octubre. Es un desajuste de la ficha web, no del plazo. Y una "
 "trazabilidad honesta: la nota del 22 de octubre <b>no se ha podido servir desde la propia página de la "
 "EBA</b>; su texto se ha verificado en una reproducción literal fechada ese día y corroborado con las fechas "
 "que efectivamente muestra la página de consultas."),

("fin", "DORA · sin novedad en la ventana, y la lista de proveedores críticos sigue siendo la de 2025", False,
 "Cero normas técnicas nuevas en todo 2026, ninguna designación nueva de proveedor crítico y la actualización "
 "anual de la lista, que toca en noviembre, aún no ha salido",
 "Comprobado y con resultado cerrado. <b>Normas técnicas:</b> los actos de nivel 2 más recientes que completan "
 "<b>DORA</b> siguen siendo el Reglamento 2025/1190, de pruebas de penetración basadas en amenazas, y el "
 "Reglamento 2025/532, de subcontratación de servicios TIC; <b>no consta ningún acto de 2026</b>, y por tanto "
 "ninguno en la ventana. <b>Proveedores terceros críticos:</b> la lista publicada sigue siendo la de "
 "<b>noviembre de 2025</b>, con <b>diecinueve entidades designadas</b>, encabezada por la fórmula «de "
 "conformidad con el artículo 31, apartado 9, de DORA, la lista de proveedores terceros de servicios TIC "
 "críticos designados a escala de la Unión es la siguiente». El elemento más reciente de toda la página de "
 "supervisión es de <b>enero de 2026</b>, el memorando con el Reino Unido. La propia página recuerda que la "
 "lista se actualiza con periodicidad anual por el artículo 31.8, y la de 2026 <b>no estaba publicada</b> al "
 "cierre de la ventana. <b>TIBER-EU y TIBER-ES:</b> toda la documentación del marco sigue siendo la versión de "
 "2025, sin un solo documento nuevo ni actualizado. Y ni la EBA, ni ESMA, ni EIOPA publicaron material de DORA "
 "en la ventana.",
 "Decirlo en voz alta tiene valor, porque la percepción del mercado es la contraria: <b>DORA lleva todo 2026 "
 "sin producir una sola norma técnica nueva</b>. El marco de nivel 2 está cerrado desde julio de 2025 y lo que "
 "queda es aplicación y supervisión, no normativa. Para un cliente financiero, eso significa que el argumento "
 "de «estamos esperando a ver qué más sale» ya no se sostiene, y que lo que viene no son normas sino "
 "<b>preguntas</b>. La acción de noviembre es muy concreta y conviene ponerla en el calendario: la lista de "
 "proveedores críticos se actualiza una vez al año y la de 2025 salió el <b>18 de noviembre</b>, de modo que la "
 "de 2026 es esperable en las próximas tres semanas. Cuando salga, hay que hacer una cosa inmediatamente: "
 "cruzar las designaciones nuevas contra el <b>registro de información</b> del cliente, porque un proveedor que "
 "entra en la lista cambia de régimen y arrastra consecuencias contractuales por los artículos 28 a 30. Quien "
 "tenga ese cruce preparado lo resolverá en una tarde; quien no, en un trimestre.",
 'La <a href="https://www.esma.europa.eu/dora-oversight" @L>página de supervisión de DORA de las Autoridades '
 'Europeas de Supervisión</a>, con la lista de proveedores designados de noviembre de 2025 y la guía de '
 'actividades de supervisión de julio de 2025.',
 "Dos cosas sobre el mercado español, y la primera es la que sorprende: en <b>once ediciones</b> de este "
 "boletín, el régimen de notificación de incidentes graves de DORA <b>no ha aparecido ni una vez</b> en la "
 "sección de incidentes. No es casualidad ni laguna de búsqueda, y hay una razón estructural que conviene "
 "repetirle al cliente: <b>bajo DORA las notificaciones de incidentes graves van a la autoridad competente y "
 "no son públicas</b>, igual que no lo son las del Mecanismo Único de Supervisión, las del Banco de España ni "
 "las de la Dirección General de Seguros. Ausencia de noticias no es ausencia de incidentes. La segunda: la "
 "sección de ciberseguridad de la <b>CNMV</b> no se ha tocado desde el 15 de octubre, y sus dos piezas de "
 "doctrina propia, la de ciberresiliencia ante modelos de IA de frontera y la de resiliencia poscuántica, "
 "siguen siendo la referencia nacional más cercana a lo que el BCE pidió en julio."),
]

ITEMS += [

("std", "NIST · IR 8547 en versión final, 27 de octubre de 2026", True,
 "El NIST cierra en firme, dos años después del borrador, el documento de referencia de la transición a la "
 "criptografía poscuántica, con 2030 y 2031 como fechas de corte para los sistemas más sensibles",
 "El <b>27 de octubre</b> el <b>NIST</b> publicó la versión <b>final</b> del <b>NIST IR 8547, «Transition to "
 "Post-Quantum Cryptography Standards»</b>, que llevaba en borrador desde el 12 de noviembre de 2024. El "
 "historial del propio documento lo confirma: borrador 12/11/24, final 27/10/26. Qué es, en sus palabras: «este "
 "informe describe el enfoque del NIST para la transición desde los algoritmos criptográficos vulnerables a la "
 "computación cuántica hacia algoritmos poscuánticos de firma digital y esquemas de establecimiento de claves. "
 "<b>Identifica las normas criptográficas vulnerables existentes y las normas resistentes a la computación "
 "cuántica a las que los productos y servicios de tecnologías de la información tendrán que migrar</b>». Las "
 "fechas, que el NIST recoge de la normativa estadounidense: «la Memoria de Seguridad Nacional 10 estableció el "
 "año <b>2035</b> como objetivo principal para completar la migración; la Orden Ejecutiva 14412 aceleró ese "
 "calendario, exigiendo que los activos federales de alto valor y los sistemas de alto impacto migren para "
 "<b>2030</b> en establecimiento de claves y <b>2031</b> en firmas digitales».",
 "Son obligaciones del sector público federal estadounidense y no obligan a nadie en España, pero son la "
 "referencia de facto que están adoptando los calendarios europeos de criptoagilidad, y por eso importan por "
 "dos vías. La primera es de cadena de suministro: si tu cliente vende tecnología a la administración "
 "estadounidense o a cualquiera que le venda a ella, esas fechas <b>le llegan por contrato</b>, y 2030 está a "
 "cuatro ejercicios presupuestarios. La segunda es la que vale para el resto, y es que este documento resuelve "
 "gratis la parte más difícil de un plan de migración: <b>identifica qué normas criptográficas son vulnerables "
 "y a qué norma concreta migra cada una</b>. Ese mapeo es exactamente lo que falta en todos los planes "
 "poscuánticos que se están escribiendo y es lo que convierte un inventario criptográfico en una hoja de ruta. "
 "Nótese la coincidencia de la semana, que no es casual: el NIST cierra su guía, el Banco de España y el Banco "
 "de Portugal firman un programa poscuántico, el CCN pone la amenaza cuántica en el lema de sus jornadas, y el "
 "comité de seguridad de la ISO mueve dos proyectos de criptografía basada en retículos. Cuatro señales en "
 "siete días.",
 'El <a href="https://csrc.nist.gov/pubs/ir/8547/final" @L>NIST IR 8547 en versión final, de 27 de octubre de '
 '2026</a> y la <a href="https://www.nist.gov/news-events/news/2026/10/nist-report-provides-guidelines-'
 'transition-post-quantum-cryptography" @L>nota de prensa del NIST del mismo día</a>.',
 "Fue la única publicación del NIST en la ventana. Comprobadas las cien publicaciones más recientes de su "
 "centro de recursos: sin movimiento en el marco de ciberseguridad, ni en el SP 800-53, ni en el SP 800-171, "
 "ni en el marco de gestión de riesgos de IA, ni en los FIPS 203, 204 y 205. Lo inmediatamente anterior son "
 "tres borradores iniciales de los días 8, 21 y 22 de octubre. Y se declara una laguna concreta: <b>no se ha "
 "podido comprobar si hubo versión nueva de OSCAL</b>, porque sus versiones se publican en un repositorio de "
 "código no alcanzable en este entorno; lo único afirmable es que ni las noticias ni las publicaciones del "
 "NIST lo mencionan en la ventana."),

("std", "CEN-CENELEC · boletín de 28 de octubre de 2026", True,
 "El plazo de las normas armonizadas que dan presunción de conformidad en el Reglamento de IA se desplaza a "
 "febrero de 2027, y la petición de normalización de la Comisión se ha revisado para encajarlo",
 "El <b>28 de octubre</b>, en el boletín «On the spot» número 77 de <b>CEN-CENELEC</b>, se publicó una entrada "
 "titulada «Recta final antes de la publicación de las normas armonizadas de apoyo al Reglamento de IA» que "
 "dice literalmente: «<b>tras las modificaciones adoptadas en el Ómnibus Digital sobre IA en junio de 2026, la "
 "entrada en vigor de las obligaciones para los sistemas de IA de alto riesgo se postergó debido esencialmente "
 "a la indisponibilidad de las normas armonizadas necesarias para su aplicación. En consecuencia, la petición "
 "de normalización de la Comisión Europea se ha revisado para alinearse con los nuevos calendarios, fijando el "
 "plazo para las normas armonizadas de apoyo en febrero de 2027</b>». Y sobre el estado real del trabajo: «si "
 "bien se ha avanzado significativamente en el último año, con varias normas en camino de completarse en "
 "plazo, la Comisión Europea reiteró la <b>necesidad crítica de normas de alta calidad</b>». El pleno número "
 "quince del comité europeo de IA se celebró del 6 al 9 de octubre en Winterthur.",
 "Esta es la pieza que cierra el círculo del Reglamento de IA y conviene contarla entera, porque explica un "
 "retraso que muchos clientes han leído como un indulto y no lo es. La secuencia real es: no había normas "
 "armonizadas, por eso se retrasaron las obligaciones de alto riesgo a diciembre de 2027 y agosto de 2028, y "
 "ahora la petición de normalización se reajusta a febrero de 2027 para que las normas lleguen antes. Es decir, "
 "<b>el retraso de las obligaciones no fue una concesión política, fue una imposibilidad material</b>, y eso "
 "cambia el consejo que hay que dar: nadie debería contar con otro retraso, porque el cuello de botella se está "
 "resolviendo. La acción concreta para un cliente con sistema de alto riesgo es de secuencia: la primera norma "
 "armonizada, la EN 18286:2026 sobre el sistema de gestión de la calidad, ya está citada en el Diario Oficial "
 "desde el 14 de octubre y da presunción de conformidad; empezar por ella es lo barato, porque es gestión y no "
 "producto, y lo que llegue en febrero de 2027 se montará encima.",
 'La <a href="https://www.cencenelec.eu/news-events/news/2026/newsletter/ots-77-etuc/" @L>entrada del boletín '
 'número 77 de CEN-CENELEC, de 28 de octubre de 2026</a>.',
 "Cautela de atribución que hay que mantener si se cita: la entrada está publicada en el sitio de CEN-CENELEC "
 "pero <b>la firma la Confederación Europea de Sindicatos</b>, que es uno de los organismos del anexo III con "
 "voz en la normalización europea. Es la declaración de una parte interesada alojada en el boletín oficial del "
 "organismo de normalización, <b>no una nota de la Comisión ni del propio comité de IA</b>, y la revisión de la "
 "petición de normalización que menciona conviene confirmarla contra el documento de la Comisión antes de "
 "citarla como hecho firme. La propia entrada añade la posición sindical: pide «preservar los borradores de "
 "consenso de alta calidad desarrollados en los últimos años, garantizando que no se comprometan las "
 "salvaguardas esenciales en la carrera por cumplir calendarios acelerados»."),

("std", "ISO/IEC JTC 1/SC 27 · del 27 al 31 de octubre de 2026", False,
 "Ocho proyectos del comité de seguridad de la información cambian de etapa en cinco días, dos de ellos de "
 "criptografía poscuántica, y el comité de inteligencia artificial no mueve ni uno",
 "Barrido ficha por ficha del ciclo de vida de las <b>576 entradas del catálogo del SC 27</b> y de las <b>96 "
 "del SC 42</b>, porque es la única forma de obtener fechas exactas. Resultado: <b>ocho proyectos con trece "
 "eventos de etapa, todos del SC 27, y cero del SC 42</b>. Los dos más cerca de publicarse: la <b>ISO/IEC "
 "29192-4/FDAmd 2</b>, de criptografía ligera con técnicas asimétricas, pasó a etapa 50.00 el 30 de octubre, "
 "es decir texto final registrado para aprobación formal; y la <b>ISO/IEC DTR 22216</b>, sobre los desarrollos "
 "técnicos de la serie 15408 y de la 18045, abrió el 30 de octubre votación con la anotación literal «votación "
 "iniciada: 8 semanas». Los demás: <b>ISO/IEC WD 14888-5</b>, firmas digitales con mecanismos <b>basados en "
 "retículos</b>, inició estudio de borrador el 31 de octubre; y abrieron consulta de borrador de comité la "
 "<b>ISO/IEC CD 25456</b>, de detección de ataques de inyección de datos biométricos, la <b>ISO/IEC CD "
 "27505</b>, de privacidad en interfaces cerebro-ordenador, la <b>ISO/IEC CD 27566-2</b>, de sistemas de "
 "garantía de la edad, la <b>ISO/IEC CD TS 27568</b>, de seguridad y privacidad de gemelos digitales, y la "
 "<b>ISO/IEC WD 7709.3</b>, de procesamiento de datos de múltiples fuentes.",
 "Ninguno de estos ocho crea obligación y ninguno es del núcleo del sistema de gestión, de modo que no hay nada "
 "que hacer esta semana. El valor es de anticipación a dos y tres años, y hay dos señales que merecen "
 "atención. La primera: el comité <b>está empujando criptografía poscuántica por la vía ISO</b>, en paralelo al "
 "NIST y la misma semana en que el NIST cierra su guía. Para un cliente europeo eso importa, porque una norma "
 "ISO es la referencia que un auditor europeo acepta sin discusión, mientras que un documento del NIST siempre "
 "admite la objeción de ser normativa estadounidense. La segunda: la <b>ISO/IEC 27566-2, de garantía de la "
 "edad</b>, es el proyecto de esta lista con más probabilidad de acabar convertido en obligación regulatoria "
 "europea a medio plazo, y la coincidencia con el EU Kids Act, cuya consulta española cierra el miércoles, no "
 "es casual: cuando el reglamento europeo exija sistemas de verificación de edad, esta será la norma que dé "
 "presunción de cumplimiento. Si tienes clientes de plataformas o de comercio con restricción de edad, "
 "conviene seguirla.",
 'Las fichas de la <a href="https://www.iso.org/standard/90706.html" @L>ISO/IEC 29192-4/FDAmd 2</a>, de la '
 '<a href="https://www.iso.org/standard/91721.html" @L>ISO/IEC DTR 22216</a>, de la '
 '<a href="https://www.iso.org/standard/92017.html" @L>ISO/IEC WD 14888-5</a> y de la '
 '<a href="https://www.iso.org/standard/90011.html" @L>ISO/IEC CD 27566-2</a>.',
 "Aviso de método importante, que corrige lo que este boletín venía suponiendo. El <b>feed de catálogo por "
 "comité de la ISO no funciona como feed</b>: la ruta redirige y acaba sirviendo la página de catálogo "
 "completa, con las etapas actuales pero <b>sin fechas</b>, de modo que cualquier barrido que dependa de él "
 "produce semanas vacías falsas. La única vía que da fechas verificadas es abrir el bloque de ciclo de vida de "
 "cada ficha, que es lo que se ha hecho con las 672 entradas de los dos comités. Y el dominio principal de la "
 "ISO rechaza el acceso automatizado: la alternativa que sirve el mismo catálogo y las mismas fichas es el "
 "subdominio de comités. Sobre plazos: la ISO <b>no publica en la ficha la fecha de cierre</b> de las "
 "consultas, de modo que las cuatro consultas de borrador abiertas el 30 y el 31 de octubre no tienen cierre "
 "determinable, y las ocho semanas de la DTR 22216 son un cálculo propio."),

("std", "Global ACI · el IAF y el ILAC ya no existen, y conviene dejar de citarlos", False,
 "La organización que emite los documentos obligatorios de acreditación cesó operaciones el 1 de enero de "
 "2026, sus documentos siguen siendo válidos, y esta semana publicó su marco estratégico",
 "Hallazgo estructural que afecta al lenguaje de cualquier informe de certificación. El sitio del <b>IAF</b> "
 "muestra en cabecera: «<b>el IAF cesó operaciones el 1 de enero de 2026</b>. Este sitio web es un sitio "
 "heredado mantenido únicamente con fines de archivo y referencia». El sucesor es <b>Global Accreditation "
 "Cooperation Incorporated</b>, Global ACI, que absorbe al IAF y al <b>ILAC</b> y «comenzó a operar el 1 de "
 "enero» de 2026. Lo que importa para no romper nada: los documentos antiguos <b>no han caducado</b>. La propia "
 "página de documentos de Global ACI dice que «en virtud de las Resoluciones de Global ACI <b>2025-25 y "
 "2025-29</b>, los documentos del IAF y del ILAC especificados <b>siguen siendo válidos hasta que se adopten "
 "los documentos equivalentes de Global ACI</b>». En la ventana publicó un único documento, el <b>Global "
 "ACI-GOV-038</b>, marco estratégico 2026-2028, de <b>26 de octubre</b>, que es de gobernanza y no crea plazos. "
 "Sus reuniones anuales se celebraron en Ciudad de Panamá del 19 al 26 de octubre.",
 "Es un detalle de nomenclatura que cuesta credibilidad cuando se falla. Si tus informes, tus pliegos o tus "
 "cláusulas contractuales citan «documentos obligatorios del IAF», llevan diez meses citando una organización "
 "que no existe, y es el tipo de error que un auditor detecta en el primer párrafo. La corrección es sencilla y "
 "conviene hacerla con la cita de las dos resoluciones a mano, porque la pregunta inmediata del cliente va a "
 "ser si su certificado sigue valiendo: sí, y la base es que los documentos siguen vigentes hasta que se "
 "adopten los equivalentes. Y hay un punto de fondo con consecuencias reales a medio plazo, que es el que "
 "merece seguimiento: entre las resoluciones adoptadas en Panamá está la <b>2026-69</b>, que fija un periodo de "
 "transición de <b>dos años</b> para la futura ISO/IEC 17065, que es la norma de requisitos para los organismos "
 "que certifican productos, procesos y servicios. Esa es la vía por la que pasan el <b>EUCC</b> y el "
 "<b>Reglamento de Ciberresiliencia</b>. Todavía no genera fecha, porque la norma no está publicada, pero "
 "cuando lo haga afectará a la capacidad de evaluación de conformidad justo cuando más falta hace.",
 'La <a href="https://global-aci.org/en/documents/" @L>página de documentos de Global ACI</a>, con la tabla de '
 'referencias cruzadas de documentos del IAF y del ILAC, y su '
 '<a href="https://global-aci.org/en/global_aci-documents/resolutions/" @L>repositorio de resoluciones</a>.',
 "Dos precisiones. Sobre transiciones, la categoría de documentos técnicos de transición de Global ACI contiene "
 "<b>exactamente cuatro</b> documentos, y <b>ninguno afecta a la ISO/IEC 27001, a la 42001 ni a la 42006</b>: "
 "son los de la ISO 37001:2025, que vence el 28 de febrero de 2027, y los de la ISO/IEC 17024:2026, la ISO "
 "14001:2026 y la ISO 9001:2026, los tres en 2029. Y sobre la fecha de las resoluciones de Panamá: <b>no se ha "
 "podido fijar</b>, porque se identifican por sede y número sin fecha de adopción, de modo que no puede "
 "afirmarse si se adoptaron dentro de la ventana o en los días 19 al 25. El único anclaje temporal es que una "
 "de ellas elige a un miembro del comité ejecutivo «por un mandato de tres años que comienza el 26 de octubre "
 "de 2026»."),

("std", "ENAC · dieciséis meses sin esquema de acreditación para certificar sistemas de gestión de IA", False,
 "La norma que regula a los certificadores de sistemas de gestión de inteligencia artificial se publicó en "
 "julio de 2025 y España sigue sin esquema de acreditación anunciado",
 "Comprobado y confirmado a 2 de noviembre de 2026: <b>ENAC no ha anunciado ningún esquema de acreditación "
 "sobre la ISO/IEC 42006</b>, que es la norma de requisitos para los organismos que auditan y certifican "
 "sistemas de gestión de inteligencia artificial. Tres verificaciones: ninguna noticia de su canal de "
 "actualidad ni de su sección sectorial de ciberseguridad lo menciona, y su elemento más reciente es del <b>14 "
 "de octubre</b>; el documento que regularía esa acreditación, los <b>Criterios Generales de Acreditación de "
 "Entidades de Certificación de Sistemas de Gestión</b>, está en revisión 16 de <b>marzo de 2026</b> y <b>no "
 "menciona ni la ISO/IEC 42001 ni la 42006</b>; y no hay referencia a ninguna de las dos en su repositorio "
 "documental público. La <b>ISO/IEC 42006:2025</b> se publicó el <b>7 de julio de 2025</b>: van dieciséis "
 "meses. Lo más reciente de ENAC en ciberseguridad de producto es de abril de 2026, la primera acreditación "
 "para certificar ciberseguridad en sistemas de automatización y control industrial conforme a la serie "
 "62443.",
 "Esto hay que saberlo porque evita vender algo que no se puede entregar. Si un cliente pide una "
 "<b>certificación acreditada</b> de su sistema de gestión de IA conforme a la ISO/IEC 42001, hoy en España no "
 "se le puede conseguir: hay certificadores que emiten certificados de 42001, pero <b>sin acreditación "
 "nacional</b> detrás, porque no existe el esquema. La diferencia no es formal y conviene explicarla antes de "
 "firmar: un certificado no acreditado vale como evidencia de diligencia interna y como argumento comercial, "
 "pero no se beneficia de los acuerdos de reconocimiento internacional y es cuestionable ante un supervisor "
 "que pregunte quién vigila al certificador. El consejo honesto para un cliente que quiere adelantarse al "
 "Reglamento de IA es implantar la 42001 ahora y certificar cuando haya esquema, porque la implantación es lo "
 "que lleva tiempo y el certificado se emite en semanas. Y conviene decir en qué queda la urgencia: con las "
 "obligaciones de alto riesgo desplazadas a diciembre de 2027 y agosto de 2028, hay margen, pero dieciséis "
 "meses de retraso en el esquema cuando el reloj regulatorio ya corre es una señal de capacidad nacional que "
 "merece estar en el radar.",
 'El <a href="https://www.enac.es/actualidad" @L>canal de actualidad de ENAC</a> y los Criterios Generales de '
 'Acreditación de Entidades de Certificación de Sistemas de Gestión, en revisión 16 de marzo de 2026.',
 "Se declara una limitación: el <b>buscador documental de ENAC</b> es un formulario que no se ha podido "
 "consultar de forma automatizada, de modo que la conclusión se apoya en el canal de actualidad, en la sección "
 "sectorial de ciberseguridad y en la lectura completa del documento de criterios, pero <b>no en un barrido "
 "exhaustivo del repositorio</b>."),

("std", "ETSI · nota de 29 de octubre de 2026, y las diecisiete normas del Reglamento de Ciberresiliencia", False,
 "ETSI anuncia una especificación para prevenir la generación de ultrafalsificaciones, y por separado mantiene "
 "en encuesta pública las diecisiete normas que darán presunción de conformidad en el Reglamento de "
 "Ciberresiliencia",
 "El <b>29 de octubre</b> <b>ETSI</b> publicó una nota titulada «ETSI presenta una norma nueva para reducir la "
 "producción de ultrafalsificaciones dañinas», sobre la <b>ETSI TS 104 275</b>, elaborada por su comité de "
 "seguridad de la inteligencia artificial, que aplica los requisitos básicos de ciberseguridad para modelos y "
 "sistemas de IA a la IA generativa con el objetivo de <b>prevenir el daño antes de que el contenido exista</b>: "
 "«los esfuerzos para combatir las ultrafalsificaciones se han centrado principalmente en <b>detectar</b> "
 "contenido manipulado <b>después</b> de haber sido creado», y «a medida que se vuelven más omnipresentes, las "
 "organizaciones de IA necesitan apoyo para abordar los riesgos mucho antes». La especificación «esboza además "
 "escenarios de prueba y criterios de aprobado y suspenso». Y por separado, sigue abierta la encuesta pública "
 "de las <b>diecisiete normas europeas de la serie ETSI EN 304</b> que darán cobertura al Reglamento de "
 "Ciberresiliencia, sometidas a 41 organizaciones miembro, con un procedimiento de aprobación que va «de "
 "mediados de septiembre a mediados de noviembre de 2026, según el vertical».",
 "La especificación de ultrafalsificaciones es útil por un motivo que no es el obvio. No sirve para detectar un "
 "vídeo falso, que es lo que todo el mundo pide: sirve para <b>exigir a un proveedor de IA generativa que "
 "demuestre que su modelo no la produce</b>, y lo hace con escenarios de prueba y criterios de aprobado y "
 "suspenso. Eso es exactamente lo que falta en cualquier pliego de contratación de IA generativa, y es un "
 "requisito que se puede copiar literalmente. Si tienes clientes contratando modelos generativos, ahí hay una "
 "cláusula lista. Lo de las diecisiete normas del Reglamento de Ciberresiliencia es más importante a medio "
 "plazo y conviene entender el encaje con el cero de organismos notificados: esas normas son la vía por la que "
 "un fabricante podrá acreditar conformidad <b>sin</b> depender de un tercero, de modo que cuanto antes se "
 "publiquen, menos presión habrá sobre un sistema de evaluación que hoy tiene cero capacidad. Si tu cliente "
 "fabrica producto con elementos digitales, los borradores están accesibles y leerlos ahora es ventaja: dicen "
 "qué va a tener que demostrar en 2027.",
 'La <a href="https://www.etsi.org/newsroom/press-releases/etsi-unveils-new-standard-to-reduce-production-of-'
 'harmful-deepfakes/" @L>nota de ETSI de 29 de octubre de 2026</a> y la '
 '<a href="https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-'
 'standards-supporting-the-cyber-resilience-act/" @L>nota de 13 de agosto de 2026 sobre las diecisiete normas '
 'del Reglamento de Ciberresiliencia</a>.',
 "Dos precisiones de fecha, y la primera es una trampa fácil. La <b>ETSI TS 104 275 no es una norma de esta "
 "semana</b>: lleva fecha de portada de <b>septiembre de 2026</b>. Lo que cae en la ventana es el anuncio, del "
 "29 de octubre, y presentarla como publicada esta semana sería incorrecto. La segunda: la nota de agosto "
 "sobre las diecisiete normas <b>no da fecha concreta de cierre</b> de la encuesta; dice «mediados de "
 "noviembre» según el vertical, y el 15 de noviembre que figura en la tabla de plazos de esta edición es la "
 "lectura prudente de ese «mediados», no un dato publicado. No se ha podido confirmar en fuente de la ventana "
 "que la encuesta haya cerrado ni con qué fecha. Se declara además que el programa de trabajo y el índice de "
 "entregables de ETSI no son alcanzables de forma automatizada, de modo que lo afirmado sobre ETSI se apoya en "
 "su sala de prensa y no en su catálogo completo."),
]

ITEMS += [

("ai", "Reglamento de IA · el 2 de diciembre de 2026 concentra dos hitos, no uno", True,
 "A treinta días, vencen a la vez el periodo de gracia del marcado de contenido sintético y la entrada en "
 "aplicación de dos prohibiciones nuevas, y solo el segundo crea obligación",
 "Verificado contra el articulado consolidado del <b>Reglamento (UE) 2024/1689</b> tal como lo modificó el "
 "<b>Reglamento (UE) 2026/1744</b>, en vigor desde el 27 de julio de 2026. <b>Primer hito.</b> El artículo "
 "111.4 dice: «los proveedores de sistemas de IA, incluidos los sistemas de IA de uso general, que generen "
 "contenido sintético de audio, imagen, vídeo o texto y <b>se hayan introducido en el mercado antes del 2 de "
 "agosto de 2026</b> adoptarán las medidas necesarias para cumplir lo dispuesto en el artículo 50, apartado 2, "
 "<b>a más tardar el 2 de diciembre de 2026</b>». Y el artículo 50.2, que no fue modificado, es el del marcado: "
 "los proveedores «velarán por que los resultados de salida estén <b>marcados en un formato legible por "
 "máquina</b> y que sea posible detectar que han sido generados o manipulados de manera artificial». <b>Segundo "
 "hito.</b> El artículo 113 consolidado exceptúa de la aplicación general «el artículo 5, apartado 1, párrafo "
 "primero, letras b bis) y b ter), y el artículo 5, apartado 1 bis, y apartado 1 ter, <b>que serán aplicables a "
 "partir del 2 de diciembre de 2026</b>». Son dos prácticas prohibidas nuevas: generar o manipular material "
 "sexual no consentido de persona identificable, y material del artículo 2, letras c) y e), de la Directiva "
 "2011/93/UE.",
 "La distinción entre los dos hitos es la diferencia entre asesorar bien y asustar, y conviene tenerla clara "
 "antes de que un cliente pregunte. El del <b>artículo 111.4 no crea ninguna obligación nueva</b>: la de marcar "
 "el contenido sintético en formato legible por máquina rige desde el 2 de agosto de 2026, porque el artículo "
 "50 está en el capítulo IV y no figura entre las excepciones del artículo 113. Lo que vence el 2 de diciembre "
 "es el <b>periodo de gracia</b> que se concedió al inventario ya comercializado antes de agosto, de modo que a "
 "partir de ese día <b>no queda producto heredado exento</b>. La acción concreta, y es de inventario, no de "
 "proyecto: identificar qué sistemas generativos del catálogo del cliente estaban en el mercado antes del 2 de "
 "agosto de 2026, porque son exactamente los que pierden la exención. El del <b>artículo 5 sí crea obligación "
 "nueva</b>, y conviene no minimizarlo, porque el capítulo de sanciones es plenamente aplicable desde el 2 de "
 "agosto de 2025 y el artículo 5 es la infracción más gravemente sancionada, la del artículo 99.3. Los "
 "apartados 1 bis y 1 ter acotan el alcance de forma relevante: la comercialización solo está prohibida cuando "
 "esa generación sea la <b>finalidad prevista</b> del sistema, o cuando el diseño, el entrenamiento, la "
 "arquitectura o las funcionalidades hagan de ella «un resultado razonablemente previsible y reproducible sin "
 "requerir modificación técnica significativa» <b>y</b> el sistema no tenga medidas técnicas de seguridad "
 "adecuadas para evitarla de forma fiable. Ahí está el deber: si tu cliente integra un modelo generativo de "
 "imagen, lo que le protege son <b>las barreras técnicas documentadas</b>.",
 'El <a href="https://eur-lex.europa.eu/eli/reg/2026/1744/oj" @L>Reglamento (UE) 2026/1744, de 8 de julio de '
 '2026, publicado en el Diario Oficial el 24 de julio</a> y el '
 '<a href="https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27" @L>texto consolidado del Reglamento de IA a '
 '27 de julio de 2026</a>, que es el que hay que citar a partir de ahora.',
 "Corrección y ampliación de lo que publicó este boletín la semana pasada. La corrección de la edición 010 "
 "sobre el artículo 111.4 <b>era correcta y queda confirmada</b> contra el articulado: ese apartado es "
 "aplicable desde el 2 de agosto de 2026 y el 2 de diciembre se agota un periodo de gracia. Lo que faltaba es "
 "que <b>ese mismo día concentra un segundo hito</b>, el de las dos prohibiciones nuevas, que sí es una "
 "obligación que nace. Y una ampliación útil de lo que trajo el Ómnibus y casi nadie ha contado: el artículo 4, "
 "de alfabetización en IA, se reescribió a una obligación de «adoptar medidas para apoyar el desarrollo de la "
 "alfabetización en IA», con la aclaración expresa de que «<b>esta obligación no exige a los proveedores o "
 "responsables del despliegue garantizar ningún nivel específico de alfabetización en IA de ninguna "
 "persona</b>»; y se introdujo la categoría de <b>empresa de mediana capitalización</b>, con documentación "
 "técnica simplificada y multas reducidas por el nuevo artículo 99.6 bis."),

("ai", "AEPD · decálogo de asistentes y agentes de IA, 27 de octubre de 2026", True,
 "La Agencia publica el primer documento español que advierte de la inyección indirecta de instrucciones, y lo "
 "hace con un ejemplo real de un agente que cerró un trato y dio la dirección del usuario",
 "El <b>27 de octubre</b> la <b>AEPD</b> publicó «<b>Asistentes y agentes de IA: Decálogo para personas "
 "usuarias</b>», bajo el lema «Que la IA actúe por ti, no sin ti». Su eje lo resume una frase: «cuando el "
 "asistente <b>solo responde</b>, un error es una respuesta equivocada», frente al salto a la acción autónoma, "
 "que cambia la naturaleza del error. Propone cinco preguntas previas a delegar: «<b>qué puede ver</b> el "
 "asistente, <b>qué puede recordar</b>, <b>qué puede hacer en nuestro nombre</b>, <b>dónde envía los datos</b> "
 "y <b>si afecta a otras personas</b>». Recomienda conceder «solo los accesos imprescindibles», no pulsar "
 "«permitir siempre» sin comprender su alcance y exigir confirmación «antes de enviar, compartir, pagar o "
 "contratar». Y el párrafo que lo distingue de cualquier otra guía de uso: advierte de la <b>inyección "
 "indirecta de instrucciones</b>, porque «una web, un correo, un documento o una <b>invitación de "
 "calendario</b> pueden contener instrucciones ocultas, <b>incluso invisibles a simple vista, como un texto "
 "blanco sobre fondo blanco</b>, destinadas a que el agente haga algo distinto de lo que le pidió la persona». "
 "Su premisa de gobernanza: «<b>el agente prepara y la persona aprueba</b>». Cita un caso real: un usuario que "
 "eligió permitir siempre, y «el agente cerró el trato y facilitó su dirección» al comprador.",
 "Es la pieza más utilizable de la semana para una conversación con un cliente que ya tiene agentes de IA "
 "funcionando, y conviene aprovecharla por dos vías. La primera, aunque esté dirigido a personas usuarias, es "
 "material corporativo listo: las cinco preguntas son un cuestionario de evaluación de herramienta que se puede "
 "pegar en una política de uso aceptable tal cual, y la frase «el agente prepara y la persona aprueba» es el "
 "principio de diseño que convierte una discusión abstracta sobre autonomía en un requisito verificable. La "
 "segunda es la más valiosa y es la de inyección indirecta: es <b>la primera vez que un regulador español "
 "describe ese vector por escrito</b>, con el ejemplo del texto blanco sobre fondo blanco, y eso te permite "
 "llevarlo a un comité sin que parezca una preocupación de laboratorio. Repárese en la convergencia con lo que "
 "el <b>CCN</b> publicó dos días después: su metodología de evaluación de productos con IA cubre expresamente "
 "«la inyección de instrucciones» y «el uso indebido de herramientas y acciones por parte de sistemas "
 "agénticos», y exige «supervisión humana antes de ejecutar acciones críticas o irreversibles». Dos organismos "
 "españoles, en la misma semana, pidiendo lo mismo. Si tu cliente despliega agentes con permisos de escritura "
 "en correo o en sistemas de negocio, ahí tienes dos fuentes oficiales para exigir aprobación humana.",
 'La <a href="https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-publica-un-decalogo-para-'
 'delegar-tareas-en-asistentes" @L>nota de prensa de la AEPD de 27 de octubre de 2026</a>, que acompaña al '
 'decálogo.',
 "La AEPD traslada además una exigencia a los proveedores que conviene retener para una negociación "
 "contractual: deberían ofrecer «<b>permisos comprensibles que distingan consultar de actuar</b>». Esa "
 "distinción, consultar frente a actuar, es la que no existe en casi ninguna herramienta del mercado y la que "
 "conviene pedir expresamente en un pliego. Y en el ámbito laboral el decálogo es tajante: usar «únicamente los "
 "asistentes autorizados por cada organización» y no conectar correo o documentos profesionales a una cuenta "
 "personal de IA."),

("ai", "CEPD · consulta viva hasta el 13 de noviembre de 2026 que el propio listado esconde", True,
 "Cerraron el 30 de octubre las directrices de anonimización y las de rastreo web para IA generativa, y queda "
 "abierta una tercera sobre cuándo procede multar en lugar de aplicar otra medida",
 "Dos cierres y una apertura que casi se pierde. <b>Cerraron el 30 de octubre de 2026 a las 23:59</b>, sin "
 "prórroga, las <b>directrices 02/2026 sobre anonimización</b> y las <b>directrices 03/2026</b>, cuyo título "
 "oficial es «<b>on web scraping in the context of generative AI</b>», es decir sobre el <b>rastreo web en el "
 "contexto de la IA generativa</b>. Las dos figuran ya como cerradas a aportaciones. Y sigue <b>abierta</b> una "
 "tercera que el listado del Comité coloca fuera de la secuencia cronológica, de modo que una lectura "
 "superficial concluye que no hay ninguna: las <b>directrices 04/2026 sobre la aplicación de la facultad de "
 "imponer multas administrativas en relación con otras medidas correctivas en virtud del RGPD</b>, en consulta "
 "del <b>21 de septiembre al 13 de noviembre de 2026 a las 23:59</b>. Al margen de esto, el <b>CEPD</b> no "
 "publicó nada en la ventana: su última entrada es del 16 de octubre.",
 "Las dos que han cerrado son, juntas, la pieza doctrinal más importante del año para quien trabaje con modelos "
 "generativos, y conviene entender por qué el solapamiento no es casual: <b>anonimización</b> y <b>rastreo web "
 "para IA generativa</b> son las dos patas de la misma cadena, la de los datos con los que se entrena un "
 "modelo. Cuando salgan las versiones finales, hay que leerlas a la vez. La que sigue abierta es la que tiene "
 "un uso inmediato y es de las que no se repiten: las directrices 04/2026 regulan <b>cuándo una autoridad debe "
 "multar y cuándo puede aplicar otra medida correctiva en su lugar</b>. Eso afecta directamente a la estrategia "
 "de cualquier organización que esté o pueda estar en un procedimiento, porque es la doctrina con la que un "
 "delegado de protección de datos podrá argumentar que un requerimiento o una advertencia es suficiente. Si "
 "tienes clientes con exposición sancionadora real, aportar a esa consulta antes del viernes 13 es barato y "
 "tiene retorno; y si no, al menos conviene leer el borrador, porque anticipa el criterio que se va a aplicar. "
 "Encaja con la armonización de la metodología de multas que el propio Comité adoptó el 21 de septiembre.",
 'Las fichas de las <a href="https://www.edpb.europa.eu/public-consultations/guidelines-042026-on-the-'
 'application-of-the-power-to-impose-administrative_en" @L>directrices 04/2026, abiertas hasta el 13 de '
 'noviembre</a>, de las <a href="https://www.edpb.europa.eu/public-consultations/guidelines-022026-on-'
 'anonymisation_en" @L>directrices 02/2026 sobre anonimización</a> y de las '
 '<a href="https://www.edpb.europa.eu/public-consultations/guidelines-032026-on-web-scraping-in-the-context-of-'
 'generative-ai_en" @L>directrices 03/2026 sobre rastreo web e IA generativa</a>.',
 "Corrección a este boletín, y es de las que conviene hacer rápido: la edición pasada describió las "
 "<b>directrices 03/2026 como «sobre extraterritorialidad»</b>. No lo son. Son sobre el rastreo web en el "
 "contexto de la IA generativa, y <b>no existe en el repositorio del Comité ninguna directriz 03/2026 sobre "
 "extraterritorialidad</b>. El error importa porque cambia a quién afectaba la consulta: no a responsables "
 "fuera de la Unión, sino a cualquiera que entrene o use modelos entrenados con datos rastreados de la web. Y "
 "un aviso de método que se confirma: el listado de consultas públicas del Comité <b>no ordena por fecha ni "
 "pone las abiertas primero</b>, de modo que hay que ir a las fichas individuales o se concluye que no hay "
 "ninguna viva."),

("ai", "Garante italiano · dictamen sobre IA en la Administración, difundido el 29 de octubre de 2026", True,
 "Una autoridad de control europea admite por escrito que suprimir un dato en el origen no borra sus efectos "
 "en un modelo ya entrenado, y exige garantías adicionales por eso",
 "En su boletín número 555, de <b>29 de octubre de 2026</b>, el <b>Garante</b> italiano difundió el "
 "<b>provvedimento número 760 de 7 de octubre</b>, un dictamen <b>favorable con condiciones</b> sobre el "
 "proyecto de reglamento de la Provincia autónoma de Trento que regula el uso de sistemas de IA en apoyo de la "
 "actividad administrativa, cuya primera aplicación prevista es la protocolización y la gestión documental. El "
 "titular del propio Garante es «sí condicionado», con «necesarias mayores garantías para el tratamiento de "
 "datos personales y el ejercicio efectivo de los derechos de los interesados». Dos objeciones. La primera, de "
 "jerarquía normativa: hay que definir los elementos esenciales de los tratamientos con fuentes adecuadas, "
 "«remitiendo a actos de rango al menos reglamentario o, para las categorías particulares de datos, a un acto "
 "administrativo general de la Provincia». La segunda es la que vale como doctrina, y la toma de la propia "
 "evaluación de impacto del proyecto: «<b>corregir o suprimir un dato en el origen no significa necesariamente "
 "modificar sus efectos sobre un modelo de IA ya entrenado</b>».",
 "Esa segunda frase es oro y conviene guardarla con la referencia exacta, porque resuelve una discusión que "
 "aparece en todos los proyectos de IA y que hasta ahora se zanjaba con opiniones. La pregunta es siempre la "
 "misma: si un interesado ejerce el derecho de supresión del artículo 17, ¿hay que reentrenar el modelo? Y la "
 "respuesta honesta, que es técnicamente incómoda, es que borrar el registro de la base de datos no elimina lo "
 "que el modelo aprendió de él. Lo que esto cambia es quién lo dice: ya no es una objeción técnica del "
 "proveedor, es <b>una autoridad de control europea reconociéndolo por escrito en un dictamen</b>, y "
 "exigiendo garantías adicionales en consecuencia en lugar de exigir lo imposible. Tres usos. Para el "
 "responsable del tratamiento, es la base para documentar en la evaluación de impacto por qué la supresión se "
 "ejecuta en el origen y qué medidas compensatorias se aplican sobre el modelo. Para la negociación con un "
 "proveedor de IA, es el argumento para exigir que explique qué hace su sistema cuando llega una supresión, "
 "porque la mayoría de los contratos no lo dice. Y para cualquier cliente del sector público que esté "
 "preparando un reglamento de uso de IA, el dictamen es una lista de requisitos ya validada por un regulador. "
 "Conecta directamente con las directrices 02/2026 del Comité Europeo sobre anonimización, cuya consulta cerró "
 "el día anterior.",
 'El <a href="https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10313206" @L>boletín número 555 '
 'del Garante, de 29 de octubre de 2026</a>, que difunde el provvedimento 760 de 7 de octubre de 2026.',
 "En el mismo boletín, dos sanciones que son recordatorios útiles. Por el <b>concurso de notarios</b>: 15.000 "
 "euros al Consejo Nacional del Notariado por publicar en su plataforma los resultados de las pruebas escritas "
 "con anotaciones y comentarios, y 20.000 al Ministerio de Justicia por exponer los resultados, incluidos los "
 "nombres de los <b>no admitidos</b> al oral, a la entrada de su sede, cuando la normativa sectorial «prescribe "
 "la mención únicamente de los candidatos admitidos». Y a Barbuti Spa, 5.000 euros, con una doctrina que "
 "conviene conocer: «<b>la existencia de una dirección dedicada no exonera a las empresas de la obligación de "
 "reconocer y gestionar las solicitudes recibidas por otros canales corporativos</b>». Es decir, un formulario "
 "de ejercicio de derechos no cierra las demás puertas."),

("ai", "Autoridad neerlandesa · algoritmos e IA en el recobro, 29 y 30 de octubre de 2026", False,
 "El supervisor examina 29 agencias de cobro, concluye que es real el riesgo de decisiones totalmente "
 "automatizadas sin que las empresas lo sepan, y publica además su política de ejecución",
 "Dos publicaciones de la autoridad neerlandesa en la ventana. La primera, del <b>29 de octubre</b>: un informe "
 "sobre algoritmos e IA en <b>agencias de cobro</b>, sobre una muestra de <b>29</b>. Usos detectados: estimar "
 "la probabilidad de cobro a partir de puntuación de crédito, ubicación e historial de pagos para priorizar "
 "deudores, y «<b>enriquecimiento de expedientes</b>», es decir buscar automáticamente datos en registros y en "
 "internet, incluidos contacto, bancarios, empresariales y actividad en redes sociales. La línea roja es "
 "literal: «es esencial que las agencias de cobro <b>nunca dejen las decisiones sobre deudores completamente al "
 "ordenador</b>. En decisiones importantes debe intervenir siempre un empleado humano». Y el hallazgo más "
 "incómodo: «la autoridad considera real la posibilidad de que se produzca en la práctica una toma de "
 "decisiones <b>totalmente automatizada, y por tanto prohibida, sin que las agencias sean conscientes</b>». La "
 "segunda, del <b>30 de octubre</b>: la autoridad «ha hecho pública su <b>política de ejecución</b>, sobre el "
 "uso de los instrumentos de ejecución cuando las organizaciones no cumplen las normas de privacidad», tras "
 "una consulta pública de abril con doce respuestas incorporadas.",
 "El informe de recobro tiene una lectura que va mucho más allá de las agencias de cobro neerlandesas, y es la "
 "que conviene llevarse: <b>el riesgo que el supervisor señala es que la decisión automatizada ocurra sin que "
 "nadie en la organización lo sepa</b>. Eso pasa cuando un sistema de puntuación prioriza, filtra o descarta y "
 "el empleado que firma se limita a validar lo que la herramienta ya decidió. Es el escenario del artículo 22 "
 "del RGPD por la puerta de atrás, y es rigurosamente común en cualquier proceso de alto volumen: concesión de "
 "crédito, selección de personal, detección de fraude, priorización de reclamaciones. La pregunta que hay que "
 "hacerle a un cliente es muy concreta y casi nunca tiene respuesta: <b>¿con qué frecuencia su revisor humano "
 "se aparta de la recomendación del sistema?</b> Si la respuesta es «casi nunca» o «no lo medimos», la "
 "intervención humana es nominal y la decisión es automatizada en la práctica. Las tres recomendaciones de la "
 "autoridad son el remedio y se pueden aplicar tal cual: intervención humana real en decisiones de gran "
 "impacto, inventariar qué datos personales se tratan y contrastarlo con la normativa, y transparencia hacia el "
 "afectado sobre el uso de sistemas algorítmicos. La política de ejecución, por su parte, es lectura obligada "
 "para cualquiera con exposición en Países Bajos, y llega tres semanas después de una multa de 824.990.000 "
 "euros.",
 'La <a href="https://www.autoriteitpersoonsgegevens.nl/actueel/ap-informeert-incassobureaus-over-'
 'verantwoorde-inzet-ai" @L>nota de la autoridad neerlandesa de 29 de octubre de 2026 sobre IA en el '
 'recobro</a> y la <a href="https://www.autoriteitpersoonsgegevens.nl/actueel/handhavingsbeleid-ap-gepubliceerd" '
 '@L>publicación de su política de ejecución, de 30 de octubre</a>.',
 "Dos plazos de aquí salen, los dos dentro de los próximos treinta días: la autoridad convoca una <b>mesa "
 "redonda con el sector el 2 de diciembre</b> y la <b>inscripción cierra el 11 de noviembre</b>."),

("ai", "CNIL · 7 millones de euros a FNAC, 29 de octubre de 2026", False,
 "La autoridad francesa sanciona que un rastreador de la aplicación móvil recogiera el historial de navegación "
 "sin consentimiento, y lo usara además para entrenar el algoritmo de recomendación",
 "El <b>29 de octubre</b> la <b>CNIL</b> publicó la deliberación <b>SAN-2026-015</b>, de <b>22 de octubre</b>, "
 "por la que sanciona a <b>FNAC DARTY PARTICIPATIONS ET SERVICES con 6.000.000 de euros y a FNAC DIRECT con "
 "1.000.000</b>, siete millones en total. Los hechos: un rastreador de la aplicación móvil de Fnac recogía el "
 "<b>historial de navegación sin consentimiento</b>, para recomendaciones de producto y <b>para entrenar el "
 "algoritmo de recomendación</b>, y la formación restringida subrayó que los usuarios habían elegido <b>no</b> "
 "ser rastreados en la aplicación. La base es el artículo 82 de la ley francesa de protección de datos, es "
 "decir el régimen de rastreadores y no el RGPD general. El razonamiento es literal: «tales operaciones no "
 "entraban en el ámbito de las exenciones», y «no podían, por tanto, llevarse a cabo <b>sin el consentimiento "
 "previo</b> de los interesados». Además de la multa, la CNIL ordena acreditar <b>en el plazo de un mes</b> que "
 "la herramienta nueva recoge el consentimiento cuando es exigible, bajo <b>multa coercitiva de 10.000 euros "
 "por día</b> de retraso, y publica la decisión.",
 "Es la sanción de la semana con más capacidad de trasladarse a España, y lo relevante no es el importe sino "
 "<b>dónde está exactamente el incumplimiento</b>: no en el tratamiento posterior, sino en la lectura del "
 "dispositivo sin consentimiento. Esa es la zona donde se solapan tres regímenes que casi nadie mira juntos, y "
 "aquí está la lección que conviene llevar a cualquier cliente con aplicación móvil o comercio electrónico: el "
 "artículo 82 francés es el equivalente del <b>artículo 22.2 de la ley española de servicios de la sociedad de "
 "la información</b>, de modo que el mismo hecho es sancionable en España por la misma vía. Y la agravante es "
 "la que apunta al futuro: los datos se usaron <b>para entrenar un algoritmo</b>. Cuando el dato de entrada "
 "está viciado en origen, lo que queda contaminado es el modelo, y esta semana el Garante italiano ha dicho por "
 "escrito que suprimir el dato en el origen no borra sus efectos sobre un modelo ya entrenado. Juntando las dos "
 "cosas: un cliente que entrena recomendadores con datos de navegación recogidos sin base válida tiene un "
 "problema que <b>no se arregla dejando de recogerlos</b>. La pregunta a hacer es qué modelos se entrenaron, "
 "con qué datos y desde cuándo, y conviene hacerla antes de que la haga un reclamante.",
 'La <a href="https://www.cnil.fr/fr/sanction-cookies-app-fnac" @L>nota de la CNIL de 29 de octubre de 2026 '
 'sobre la deliberación SAN-2026-015</a>.',
 "Nota de cómputo: el plazo de un mes corre desde la <b>notificación</b> de la decisión de 22 de octubre, que "
 "no es pública, de modo que el vencimiento exacto no se puede fijar; cae en torno al <b>22 al 29 de "
 "noviembre</b>. Si se cita en un informe, conviene presentarlo como aproximado."),

("ai", "AEPD · el informe de brechas de octubre no ha salido, y el de septiembre da 939 notificaciones", False,
 "El último informe mensual publicado sigue siendo el de septiembre, con 939 notificaciones, el 73 % de origen "
 "externo y el phishing como vector dominante",
 "Comprobado por dos vías: la página de notificaciones de brechas de la <b>AEPD</b> declara «última "
 "modificación: 20 de octubre de 2026», anterior a la ventana, y sus informes mensuales en PDF listados para "
 "2026 llegan hasta <b>septiembre</b>; sondeada además la dirección del informe de octubre, que no existe. "
 "<b>El informe de octubre no estaba publicado al cierre de la ventana</b> y es esperable en noviembre. Las "
 "cifras del de septiembre, que son las vigentes: «<b>939 notificaciones</b> recibidas, 888 de ellas a través "
 "del formulario en Sede Electrónica; <b>809</b> por parte de organizaciones del ámbito privado; <b>857</b> "
 "indican brecha de confidencialidad, 33 de integridad y 83 de disponibilidad; <b>688</b> indican origen "
 "externo; <b>685</b> indican carácter malintencionado; <b>90</b> implican categorías especiales de datos, de "
 "las cuales 95 se refieren a datos de salud; 410 indican severidad baja y <b>14 severidad muy alta</b>; "
 "<b>231</b> tienen implicaciones transfronterizas». El informe destaca el <b>phishing</b> como vector habitual, "
 "con credenciales robadas mediante páginas que «suplantan portales de acceso a las herramientas de "
 "productividad en la nube más populares».",
 "Dos usos, y el segundo es el que casi nadie aprovecha. El primero es de contexto: 939 notificaciones en un "
 "mes, con 685 malintencionadas, es la cifra que sitúa a un cliente que acaba de sufrir una brecha y cree que "
 "le ha pasado algo excepcional. Y la tendencia la dio la propia Agencia el 20 de octubre: «las brechas "
 "notificadas en el <b>primer semestre de 2026 superan a las recibidas durante todo 2025</b>». El segundo uso "
 "es el que vale para una propuesta: mira el desglose por tipología. <b>857 de confidencialidad frente a 83 de "
 "disponibilidad</b> significa que lo que se notifica en España es fuga de datos, no caída de servicio, y eso "
 "choca de frente con dónde invierten casi todos los planes de seguridad, que es en continuidad y "
 "recuperación. Un plan de respuesta calibrado para el ransomware está mal calibrado para lo que de verdad "
 "ocurre nueve de cada diez veces. Y el aviso de fondo del informe de septiembre merece citarse porque es "
 "contracorriente: la Agencia dice que «la responsabilidad última <b>no debe recaer sobre los miembros de la "
 "organización</b>», sino en medidas de detección y respuesta. Es decir, el regulador está diciendo que culpar "
 "al empleado que pinchó no es una medida.",
 'La <a href="https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/brechas-de-'
 'datos-personales-notificacion/notificaciones-de-brechas-de-datos-personales" @L>página de notificaciones de '
 'brechas de la AEPD</a>, con los informes mensuales de 2026, y la '
 '<a href="https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-recibe-mas-de-3.000-'
 'notificaciones-de-brechas-de" @L>nota de 20 de octubre de 2026 sobre el primer semestre</a>.',
 "Se declara una laguna: el repositorio de resoluciones de la AEPD responde pero <b>ordena por relevancia y "
 "no por fecha</b>, y rechaza cualquier parámetro de orden o de filtro, de modo que <b>no se ha podido obtener "
 "el listado exhaustivo de resoluciones sancionadoras publicadas en la ventana</b>. Verificada al menos una "
 "publicación del 27 de octubre, que es un procedimiento de derechos y no sancionador. Para este extremo "
 "concreto: <b>no reconfirmado en fuente primaria esta semana</b>. Indicio, no confirmación: la última sanción "
 "española difundida por el Comité Europeo sigue siendo de 22 de septiembre."),

("ai", "AESIA · sin novedad, y reconoce por escrito que sus dieciséis guías están pendientes del Ómnibus", False,
 "La agencia española de supervisión de la IA no publicó nada en la ventana, y sus guías del banco de pruebas "
 "regulatorio advierten de que habrá que actualizarlas",
 "Comprobado con precisión, porque las direcciones de <b>AESIA</b> llevan el sello de fecha incorporado: su "
 "última noticia publicada es del <b>20 de octubre de 2026</b>, anterior a la ventana, y las precedentes son "
 "del 30 y el 29 de septiembre. <b>Nada entre el 26 de octubre y el 1 de noviembre.</b> Lo que sí consta, en su "
 "página de guías, es una advertencia propia sobre las dieciséis guías del piloto del banco de pruebas "
 "regulatorio, de las cuales la número 11 es la de ciberseguridad: «los documentos están sujetos a un proceso "
 "permanente de evaluación y revisión y <b>serán actualizadas de acuerdo al Ómnibus Digital que modifica el "
 "Reglamento de Inteligencia Artificial</b>». No hay fecha comprometida para esa actualización.",
 "Hay que decir con claridad en qué situación deja esto a España, porque es el hueco institucional más "
 "relevante del país en esta materia y conviene que un cliente lo entienda bien. <b>AESIA está designada y "
 "notificada</b>, de modo que la autoridad existe; pero la ley orgánica que le daba competencias formales, el "
 "expediente <b>121/000096</b>, figura <b>caducada</b>, verificado esta semana en el listado de proyectos de "
 "ley del Congreso. La consecuencia práctica, y es verificable: <b>hoy ninguna autoridad española puede imponer "
 "las multas de los artículos 99 y siguientes del Reglamento de IA</b>, porque el régimen sancionador nacional "
 "cayó con la disolución. Y hay un obstáculo adicional que conviene conocer antes de prometer plazos: el "
 "artículo 86.1 de la Constitución <b>impide arreglarlo por real decreto-ley</b>, porque afecta a derechos "
 "fundamentales; es decir, aquí la vía rápida no existe, a diferencia de lo que pasa con CER. Para el cliente, "
 "la lectura correcta no es «no hay riesgo»: el Reglamento es directamente aplicable y las obligaciones rigen, "
 "lo que falta es quién sanciona en España. Y el día que haya ley, el régimen sancionador será aplicable a "
 "conductas que ya eran ilícitas. La segunda lectura es de método: si tu cliente construyó su cumplimiento "
 "sobre las guías del banco de pruebas, la propia agencia avisa de que van a cambiar.",
 'El <a href="https://www.aesia.gob.es/es/actualidad" @L>canal de actualidad de AESIA</a> y su página de guías '
 'del piloto del banco de pruebas regulatorio.',
 None),

("ai", "Autoridad Catalana · modelo DPIA-FRIA, 29 de octubre de 2026", False,
 "La autoridad catalana fusiona en un solo procedimiento la evaluación de impacto en derechos fundamentales y "
 "la de protección de datos, que es la cuestión metodológica abierta desde 2024",
 "El <b>29 de octubre</b>, en la tercera reunión de su red de delegados de protección de datos, la <b>Autoridad "
 "Catalana</b> presentó el <b>Modelo DPIA-FRIA</b>, que «integra en un solo modelo la <b>evaluación de impacto "
 "sobre los derechos fundamentales (FRIA)</b>, obligatoria para los sistemas de IA de alto riesgo, y la "
 "<b>evaluación de impacto de protección de datos (DPIA)</b>, obligatoria cuando un tratamiento de datos supone "
 "un alto riesgo para las personas», porque «se trata de dos procedimientos exigidos por el Reglamento de "
 "inteligencia artificial y el Reglamento general de protección de datos, respectivamente». Lo describe como "
 "«una herramienta pionera a escala internacional» y «dinámica», que se adaptará según las mejoras que "
 "propongan los usuarios. Se elaboró en el grupo de trabajo de la red con el apoyo del profesor Alessandro "
 "Mantelero. Antecedente: la aplicación FRIA está disponible desde principios de octubre, y el modelo FRIA "
 "catalán previo «ha sido acogido internacionalmente y recomendado y asumido como propio por otros países del "
 "mundo como Brasil, el País Vasco, Croacia y Malta».",
 "Resuelve un problema práctico muy concreto que tiene cualquiera que haya hecho las dos evaluaciones: "
 "<b>solapan en un 70 % y se hacen por separado, con dos equipos y dos documentos que luego no cuadran</b>. "
 "Fusionarlas en un procedimiento único es la respuesta metodológica que se está esperando desde que el "
 "Reglamento de IA introdujo la FRIA sin explicar cómo convive con la DPIA del artículo 35 del RGPD, y que "
 "venga de una autoridad de control y no de una consultora le da un peso que nadie va a discutir en una "
 "auditoría. Dos cosas que conviene tener claras antes de usarlo. Primera, el calendario: no responde a ningún "
 "plazo inminente, porque el Ómnibus desplazó las obligaciones de alto riesgo a diciembre de 2027 y agosto de "
 "2028. Precisamente por eso es el momento de adoptarlo, en el espacio de preparación que acaba de abrirse y "
 "sin la prisa que arruina estos ejercicios. Segunda, su naturaleza: es <b>una herramienta metodológica "
 "voluntaria, no una disposición de obligado cumplimiento</b>, a diferencia de la Circular 1/2026 de la misma "
 "autoridad. Y una observación de fondo que vale la pena registrar: la adopción del modelo FRIA catalán por "
 "Brasil, Croacia, Malta y el País Vasco convierte a una autoridad autonómica en exportadora de metodología "
 "mientras el Estado no puede legislar. Es el segundo caso en dos semanas.",
 'La <a href="https://www.apdcat.cat/ca/actualitat/noticies/2026/APDCAT-presenta-DPIA-FRIA" @L>nota de la '
 'Autoridad Catalana de Protección de Datos de 29 de octubre de 2026</a>.',
 "En la misma jornada, la <b>Autoridad Vasca</b> presentó su herramienta para ayudar a las administraciones "
 "públicas a clasificar sistemas de IA, «ofreciendo una clasificación del nivel de riesgo, nulo, limitado o "
 "alto». Está acreditado en la nota de la autoridad catalana y <b>no en fuente propia de la autoridad vasca</b>, "
 "que no publicó nada en la ventana: su última entrada es del 23 de octubre, sobre la alerta de PHP."),

("ai", "Polonia · multa por no responder al supervisor, 26 de octubre de 2026", False,
 "La autoridad polaca multa a una asociación por ignorar dos requerimientos de información, y lo hace con una "
 "cuantía simbólica que es justamente el mensaje",
 "El <b>26 de octubre</b> la autoridad polaca de protección de datos sancionó a una asociación con "
 "<b>10.082 eslotis</b>, precisando en su propia nota que equivale al <b>0,012 % del máximo</b> del artículo "
 "83.5 del RGPD. La base no es un tratamiento ilícito: es el <b>artículo 58, apartado 1, letras a) y e)</b>, "
 "es decir la <b>falta de cooperación con la autoridad de control</b>. La asociación «no respondió a ninguno de "
 "los escritos», ni a dos requerimientos de información ni a la correspondencia posterior, en una conducta que "
 "la autoridad califica de «pasiva y despectiva hacia el organismo estatal y hacia el procedimiento en curso» "
 "y de carácter «intencional», durante más de diez meses.",
 "Es un asunto pequeño con una enseñanza que conviene tener a mano, porque la situación es mucho más frecuente "
 "de lo que parece: una organización recibe un requerimiento de información de una autoridad de protección de "
 "datos, no sabe qué contestar, teme autoincriminarse y decide no responder. Este expediente dice que eso es "
 "<b>una infracción autónoma y sancionable, con independencia de que el tratamiento de fondo fuera lícito o "
 "no</b>. Y la cuantía es el mensaje: el 0,012 % del máximo es casi testimonial, lo que indica que la autoridad "
 "no buscaba castigar sino sentar el principio de que el silencio tiene coste. Para un cliente que reciba un "
 "requerimiento, el consejo es el obvio y aun así hay que darlo: se contesta siempre, dentro de plazo, aunque "
 "la respuesta sea pedir una ampliación o acotar el alcance. No contestar convierte un expediente dudoso en un "
 "expediente perdido, y añade un agravante de intencionalidad que luego pesa en la graduación de cualquier "
 "sanción posterior.",
 'La <a href="https://uodo.gov.pl/pl/138/4638" @L>nota de la autoridad polaca de protección de datos de 26 de '
 'octubre de 2026</a>.',
 "En la misma semana, la autoridad polaca publicó una sentencia del Tribunal Supremo Administrativo que "
 "<b>confirma</b> una decisión suya sobre la obtención del consentimiento para tratar datos de salud, "
 "observaciones a un proyecto de modificación de la ley de educación y una reunión sobre el código de conducta "
 "para medios de comunicación."),
]

ITEMS += [

("thr", "PHP · explotación activa confirmada y catálogo con plazo ya vencido", True,
 "Las dos vulnerabilidades críticas de PHP se estaban explotando el 17 de octubre, cuatro días antes de que "
 "existiera el parche, y el plazo de tres días del catálogo venció el 29 de octubre",
 "La semana pasada eran dos vulnerabilidades parcheadas con pruebas de concepto circulando. Esta semana han "
 "cruzado el umbral, y lo han hecho con tres hechos verificables. <b>Uno: explotación activa confirmada por el "
 "fabricante.</b> El boletín de <b>Palo Alto Networks</b>, actualizado el <b>29 de octubre</b> y con urgencia "
 "elevada a la máxima el 27, dice literalmente: «<b>se ha observado explotación activa dirigida a la interfaz "
 "de administración de Palo Alto Networks expuesta a Internet</b>», con madurez de explotación «ATACADA». El "
 "<b>CERT-FR</b> lo recoge el 28 y, con más prudencia, habla de «<b>tentativas</b> de explotación». <b>Dos: "
 "entraron en el catálogo de vulnerabilidades explotadas el 26 de octubre</b>, primer día de la ventana, con "
 "plazo de <b>tres días</b>, el más corto que se concede, de modo que <b>venció el 29</b>. <b>Tres, y es el "
 "dato de la semana:</b> el INCIBE-CERT publicó el 29 de octubre que «el <b>primer intento de explotación "
 "registrado por telemetría se remonta al 17 de octubre, cuatro días antes de la divulgación pública y de las "
 "correcciones</b>». El parche se publicó el 21 de octubre a las 13:30. Y hay una <b>tercera vulnerabilidad de "
 "PHP sin parche</b>, la CVE-2026-115560, divulgada el 23 de octubre, que no está en el catálogo.",
 "La cifra de los cuatro días es la más valiosa del boletín de esta semana y conviene saber usarla, porque "
 "demuestra algo que normalmente solo se argumenta: <b>hubo una ventana en la que parchear era imposible porque "
 "el parche no existía, y durante esa ventana ya se estaba atacando</b>. Eso rompe la lógica de cualquier plan "
 "de seguridad construido solo sobre tiempos de parcheo, y obliga a hablar de lo único que protegió a alguien "
 "entre el 17 y el 21 de octubre: la <b>exposición</b>. Palo Alto ha puesto el número y es el argumento más "
 "rentable que vas a poder dar este mes: la misma vulnerabilidad vale <b>9,2 crítica</b> si la interfaz de "
 "administración es accesible desde Internet y <b>5,2 media</b> si solo la alcanza un equipo puente. No es un "
 "control nuevo ni caro: es sacar la administración de Internet. Dos acciones concretas para esta semana. "
 "Primera, inventario contra la lista real de productos afectados, que está publicada y mantenida en el "
 "repositorio del CERT neerlandés al que remiten CERT-EU, CERT-FR e INCIBE: ya incluye Citrix, Oracle, HPE, "
 "Broadcom, Sage CRM, Mitel, Siemens, Schneider, ABB, B&amp;R, Hikvision y más. Segunda, para la tercera "
 "vulnerabilidad sin parche, la mitigación única es <b>session.upload_progress.enabled=0</b> y reiniciar "
 "<b>todos</b> los procesos de trabajo; no sirve hacerlo desde la aplicación.",
 'El <a href="https://security.paloaltonetworks.com/CVE-2026-109618" @L>boletín de Palo Alto Networks, '
 'actualizado el 29 de octubre de 2026</a>, la '
 '<a href="https://www.incibe.es/incibe-cert/publicaciones/bitacora-de-seguridad/dos-vulnerabilidades-criticas-'
 'de-php-afectan-servidores-web" @L>bitácora del INCIBE-CERT de 29 de octubre</a> y el '
 '<a href="https://github.com/NCSC-NL/php2shell" @L>inventario de productos afectados del CERT neerlandés</a>.',
 "Precisión obligada para no exagerar, porque es el error más probable de la semana: <b>la explotación "
 "confirmada es de la interfaz de administración de PAN-OS expuesta a Internet</b>, no de todo lo que use PHP. "
 "Citrix, Oracle, Schneider y Siemens, en sus propios boletines y contextos, <b>no declaran explotación</b>, y "
 "el INCIBE registra «Explotación: No» en esos cuatro avisos. El titular correcto es «explotación activa "
 "confirmada en PAN-OS expuesto a Internet», no «explotación activa de todo lo que use PHP». Y conviene citar "
 "al CERT-FR por lo que dice, tentativas, y apoyar la afirmación fuerte en Palo Alto y en el catálogo. Sobre "
 "las mitigaciones provisionales, CERT-EU advierte literalmente que «solo una actualización corrige "
 "completamente estas vulnerabilidades; las medidas siguientes reducen la exposición a vías de ataque "
 "concretas pero <b>no hacen segura una instalación</b>», y añade un aviso crítico: no usar los límites de "
 "memoria del sistema operativo como sustituto, «porque pueden provocar el fallo de asignación vulnerable»."),

("thr", "Catálogo de vulnerabilidades explotadas · diez entradas nuevas y una cadena hasta root", True,
 "La entrada del núcleo de Linux dice en su propia descripción que se encadena con las dos de PHP para "
 "implantar puertas traseras y ejecutar como root",
 "Descargado el catálogo en su versión del <b>30 de octubre</b>, con 1.766 entradas en total. Son <b>diez "
 "entradas nuevas</b> con fecha de incorporación entre el 26 de octubre y el 1 de noviembre, y <b>ninguna de "
 "las diez</b> tiene campaña de ransomware conocida asociada. Las dos de <b>PHP</b> el 26; <b>CVE-2026-111497</b> "
 "en el decodificador <b>Brotli</b> de Google, 9,8 crítica, y <b>CVE-2026-48356</b> en Adobe Commerce y "
 "Magento, 9,3, el 27; <b>CVE-2026-41709</b> en VMware ESX y <b>CVE-2026-46300</b> en el núcleo de Linux el "
 "28; <b>CVE-2026-76418</b> en Cisco Secure Firewall ASA y FTD y <b>CVE-2026-97229</b> en GitLab, con "
 "<b>10,0</b>, el 29; y las dos de Ivanti Connect Secure el 30. La más instructiva es la del núcleo de Linux, "
 "porque su descripción lo dice todo: «<b>esta vulnerabilidad puede encadenarse con CVE-2026-109618 y "
 "CVE-2026-109619 para implantar puertas traseras web en PHP y ejecutar comandos como root</b>». Es 7,8 alta y "
 "local, es decir inútil por sí sola, y letal detrás de una ejecución remota sin autenticar.",
 "Esa cadena es la lección técnica de la semana y conviene trasladarla a la forma en que tu cliente prioriza. "
 "Una vulnerabilidad local de <b>7,8</b> en el núcleo de Linux no entra en ningún plan de parcheo urgente, "
 "porque exige acceso previo al sistema; el problema es que esta semana ese acceso previo lo regalaba una "
 "ejecución remota <b>sin autenticar</b> en PHP. Juntas, convierten un servidor web expuesto en root. La "
 "conclusión práctica es que <b>la puntuación individual de una vulnerabilidad no mide su riesgo cuando existe "
 "una cadena</b>, y que cualquier priorización que se haga solo por severidad va a dejar fuera el segundo "
 "eslabón. Es también el mejor argumento disponible contra la objeción que oirás esta semana: «esa es local, no "
 "corre prisa». Y hay un dato de encuadre que hay que dar siempre con este catálogo, porque evita un error de "
 "lectura habitual: sus plazos <b>obligan jurídicamente solo a las agencias federales estadounidenses</b>. Para "
 "una empresa española son referencia de priorización, no obligación legal. Pero tanto el artículo 21 de NIS2 "
 "como DORA exigen gestión de vulnerabilidades basada en riesgo, y la explotación activa confirmada es el "
 "criterio de riesgo más fuerte que existe. Úsalo así y es inatacable.",
 'El <a href="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json" @L>catálogo '
 'de vulnerabilidades explotadas conocidas, en su versión de 30 de octubre de 2026</a>.',
 "Trampa de fecha que afecta a cuatro de las diez: <b>lo nuevo es la entrada en el catálogo, no el "
 "descubrimiento</b>. La de Adobe Commerce se publicó el 14 de julio de 2026, la del núcleo de Linux el 23 de "
 "mayo, la de GitLab el 13 de octubre y la de VMware ESX el 30 de julio. Decir «vulnerabilidad nueva» sería "
 "incorrecto; lo correcto es «entra en el catálogo de explotadas». Y una precisión sobre la de VMware que "
 "conviene hacer para no alarmar: es una <b>laguna de registro de actividad</b> que Broadcom puntúa <b>2,7 "
 "baja</b>, y entra en el catálogo porque permite que un administrador haga operaciones sin que queden "
 "registradas. Estar en el catálogo no equivale a ser crítica."),

("thr", "Perímetro de red · cuatro explotaciones confirmadas por fabricante en siete días", True,
 "Palo Alto, Ivanti, Cisco y Arista declaran explotación activa de sus propios productos en la misma semana, y "
 "las cuatro atacan el plano de gestión",
 "Cuatro fabricantes distintos, cuatro declaraciones propias, todas en la ventana. <b>Ivanti Connect "
 "Secure</b>, boletín modificado el <b>29 de octubre</b>: «somos conscientes de explotación en la naturaleza "
 "que afecta a un número limitado de clientes <b>cuando CVE-2026-104935, CVE-2026-111357 y CVE-2026-118527 se "
 "encadenan</b>», con versiones corregidas 25.1.1.3 y 22.8R2.6, y fin de vida de las ramas 22.7 y 22.8 el 31 "
 "de enero de 2027. <b>Cisco Secure Firewall ASA y FTD</b>, boletín del <b>28 de octubre a las 19:15</b>, "
 "CVE-2026-76418, 8,6 alta: «en octubre de 2026 el PSIRT de Cisco tuvo conocimiento de <b>explotación activa</b> "
 "de esta vulnerabilidad»; el efecto es recarga del equipo, es decir <b>denegación de servicio y no ejecución "
 "de código</b>, y lo peor es que «<b>no hay soluciones alternativas</b>» y la mitigación, desactivar la "
 "autenticación secundaria, «rebaja la postura de seguridad». <b>Arista VeloCloud Orchestrator</b>, "
 "CVE-2026-114625, 9,9 crítica, con el fabricante confirmando explotación activa: una inyección SQL permite "
 "suplantar a un operador superusuario y <b>basta el rol de solo lectura</b> para escalar; solo la variante "
 "instalada en el cliente requiere acción. Y <b>Palo Alto</b>, con la cadena de PHP.",
 "El patrón es lo único que hay que retener, porque es más útil que las cuatro fichas juntas: <b>el 100 % de la "
 "explotación activa confirmada por fabricante esta semana está en el plano de gestión del perímetro</b>. No en "
 "los datos, no en el puesto de trabajo, no en el correo: en las interfaces de administración de cortafuegos, "
 "pasarelas VPN y orquestadores de red. El vector común no es una tecnología, es una decisión de arquitectura "
 "que se tomó hace años y nadie ha revisado. Eso convierte la recomendación de esta semana en una sola frase "
 "verificable que puedes llevar a cualquier cliente: <b>enumera qué interfaces de administración de equipos de "
 "red son alcanzables desde Internet y sácalas de ahí</b>. Dos detalles que merecen atención propia. El de "
 "Cisco rompe la salida fácil, porque no hay mitigación que no empeore la seguridad, de modo que la única opción "
 "real es actualizar; conviene saberlo antes de prometer una ventana de mantenimiento cómoda. Y el de Arista es "
 "el que hay que contarle a quien reparte permisos a la ligera: <b>un usuario de solo lectura escalaba a "
 "operador superusuario</b>, lo que convierte una cuenta considerada inocua en una vía de compromiso total del "
 "orquestador de la red.",
 'El <a href="https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935" '
 '@L>aviso de Ivanti, modificado el 29 de octubre de 2026</a>, el '
 '<a href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-'
 'tunnel-dos-s6mgkb75" @L>aviso de Cisco de 28 de octubre</a> y el '
 '<a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos/inyeccion-sql-en-velocloud-orchestrator-de-'
 'arista" @L>aviso del INCIBE-CERT sobre Arista VeloCloud de 26 de octubre</a>.',
 "Para quien tenga pasarelas Ivanti, conviene recordar el plan de respuesta que el CERT-FR publicó el 14 de "
 "octubre y que sigue siendo válido, porque no es técnico sino de criterio: aislar, tomar instantánea de disco "
 "y de memoria, <b>no apagar</b>, asegurar los registros, y «<b>considerar comprometidos los secretos "
 "almacenados en el equipo o que hayan transitado por él en claro</b>», con rotación de credenciales de "
 "directorio, certificados, contraseña de administración, claves de interfaz de programación y tiques Kerberos. "
 "El propio CERT-FR añade que «tiene conocimiento de lateralización utilizando esos secretos». Con un "
 "compromiso de pasarela, parchear no es terminar."),

("thr", "INCIBE-CERT · 35 avisos en la ventana, 27 de ellos críticos", False,
 "Diecinueve de los treinta y cinco avisos son consecuencia de solo dos fallos de componente, y Cisco deja "
 "varios productos sin versión corregida hasta marzo de 2027",
 "Contado sobre las páginas del propio <b>INCIBE-CERT</b>, con paginación completa: <b>21 avisos de seguridad "
 "generales y 14 de sistemas de control industrial, 35 en total, de los cuales 27 son de importancia «5 "
 "Crítica»</b>. La distribución por días va de siete el 26 a cero el 31 y el 1. Y el patrón es inequívoco: "
 "<b>al menos 19 de los 35 son consecuencia directa de las dos vulnerabilidades de PHP o de la de Brotli</b>. "
 "El INCIBE está relayando, producto por producto, la exposición indirecta a dos fallos de componente: Citrix, "
 "Oracle, Broadcom, HPE, Sage CRM, Mitel, Palo Alto, Siemens, Schneider, ABB, B&amp;R, HMS Networks, Welotec, "
 "Contec, Sprecher, Wibu-Systems e Hikvision. Dato incómodo y accionable del aviso de Cisco del 29, ampliado el "
 "30: hay productos confirmados afectados <b>sin versión corregida disponible</b>, y el propio aviso pone "
 "fechas: «Smart PHY: actualización prevista para <b>marzo de 2027</b>»; Secure Endpoint e Intersight, "
 "noviembre de 2026; Secure Workload, AI Canvas, Webex Connect y CLI Analyzer, «versión y fecha pendientes de "
 "especificar». El único parche ya disponible de ese grupo es el de la gestión de licencias en local.",
 "Dos usos muy prácticos. El primero es de dimensionamiento honesto: cuando un cliente ve 27 avisos críticos en "
 "una semana, la reacción natural es el pánico o la parálisis, y la respuesta correcta es que <b>no son 27 "
 "problemas, son dos</b>, replicados en veintitantos productos. Eso cambia la táctica por completo: en lugar de "
 "abrir 27 expedientes, se barre el inventario contra dos identificadores y se prioriza por exposición. El "
 "segundo es el que de verdad duele y casi nadie gestiona: <b>hay productos en los que no se puede hacer nada "
 "porque el fabricante no ha publicado el parche</b>, y en un caso la fecha prometida es marzo de 2027, cuatro "
 "meses y medio. Esa situación no es un hallazgo de seguridad, es una <b>decisión de riesgo que corresponde al "
 "negocio</b> y que hay que documentar como tal: riesgo aceptado temporalmente, con medidas compensatorias, "
 "fecha de revisión y firma de quien lo acepta. Si tu cliente tiene alguno de esos productos de Cisco, ese "
 "documento es el entregable de esta semana, y es exactamente el tipo de evidencia que un supervisor o un "
 "asegurador va a pedir después.",
 'Los avisos de <a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos" @L>alerta temprana del '
 'INCIBE-CERT</a> y los de <a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos-sci" @L>sistemas '
 'de control industrial</a>.',
 "Trampa de recuento que conviene conocer si alguien reconstruye estas cifras, porque es muy fácil inflarlas. "
 "Cinco avisos del INCIBE llevan en el <b>título</b> una fecha dentro de la ventana, del tipo «[Actualización "
 "26/10/2026]», y sin embargo su <b>fecha de publicación es el 23 de octubre</b>: son QNAP, Tenable, Mitel, "
 "Palo Alto y, en industriales, Johnson Controls. <b>No se han contado</b> como avisos de la ventana, porque el "
 "contenido se actualizó dentro pero la publicación es de antes. Y al revés: tres sí cuentan aunque el título "
 "lleve otra fecha, porque su publicación cae dentro. Dos avisos de la ventana afectan además a sistemas de "
 "administraciones españolas, los dos de severidad media o alta: la videoteca de las Cortes de Castilla-La "
 "Mancha y el gestor de vídeo PuMuKIT, de uso extendido en universidades públicas."),

("thr", "Dos plazos vencidos del catálogo que siguen sin resolución visible", False,
 "Collabora sobre Nextcloud y el orquestador de Arista vencieron el 26 de octubre, los dos con puntuación "
 "superior a 9,8, y ninguno tiene aviso oficial nuevo",
 "Seguimiento de los dos plazos que la edición pasada daba como vencederos el 26 de octubre. <b>CVE-2026-110447 "
 "en el servidor CODE integrado de Collabora Online sobre Nextcloud</b>: sigue en el catálogo con fecha de "
 "incorporación de 23 de octubre y <b>plazo vencido el 26</b>, sin prórroga ni cambio de entrada; es una "
 "inyección de comandos del sistema operativo que permite ejecución remota de código «cuando el servidor CODE "
 "no está en ejecución», con <b>9,8 crítica</b> confirmada en el registro nacional estadounidense, cuyo análisis "
 "se cerró el 30 de octubre. Lo que pasó en la ventana es que Nextcloud publicó el <b>27 de octubre</b> un lote "
 "de <b>seis avisos de seguridad</b>, pero son <b>otras</b> vulnerabilidades, con riesgos de denegación de "
 "servicio, confidencialidad y elusión de política, <b>ninguna de ejecución remota y ninguna es la "
 "CVE-2026-110447</b>. <b>CVE-2026-114625 en el orquestador VeloCloud de Arista</b>: igualmente vencido el 26, "
 "con 9,9 crítica y explotación confirmada por el fabricante, y lo que llegó en la ventana fue el aviso del "
 "INCIBE-CERT, publicado precisamente el 26, el mismo día en que expiraba el plazo.",
 "Esto sirve para dos cosas, y la primera es una advertencia de método: <b>no presentes los seis avisos de "
 "Nextcloud del 27 de octubre como la resolución de la vulnerabilidad crítica</b>, porque no lo son, y es un "
 "error muy fácil de cometer si se mira solo el nombre del producto y la fecha. La vulnerabilidad del 23 de "
 "octubre sigue clasificada como explotada, su plazo está vencido y lo nuevo es un lote distinto. La segunda es "
 "de inventario, y afecta a un perfil de cliente muy concreto en España: <b>Nextcloud con Collabora integrado "
 "es muy común en administraciones locales, universidades y pymes</b> que buscan soberanía del dato, y es "
 "precisamente el tipo de despliegue que se hace una vez, funciona y se olvida, sin contrato de mantenimiento "
 "ni responsable asignado. Si asesoras a un ayuntamiento o a una universidad, esa pregunta vale la llamada: "
 "¿tenéis Nextcloud, con la aplicación de Collabora integrada, y quién lo actualiza? Con el agravante de que "
 "la condición de explotabilidad es que el servidor CODE <b>no</b> esté en ejecución, es decir que el riesgo "
 "está justamente en las instalaciones donde la función apenas se usa.",
 'El <a href="https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh" @L>aviso de '
 'seguridad de Collabora Online</a> y el '
 '<a href="https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199" '
 '@L>aviso de seguridad 0199 de Arista</a>. Para VeloCloud, las versiones corregidas son 5.2.3.18, 6.1.3.10 y '
 '6.4.2.12, y las instancias alojadas ya están corregidas.',
 None),

("thr", "Brotli · la misma vulnerabilidad, declarada explotada por unos y no por otros", False,
 "El catálogo estadounidense y el INCIBE la dan por explotada y Microsoft dice en su propio aviso «Exploited: "
 "No», y las dos cosas son verdad en su ámbito",
 "<b>CVE-2026-111497</b>, en el decodificador <b>Brotli</b> de Google, 9,8 crítica: «un valor de retorno no "
 "comprobado permite a un atacante remoto no autenticado corromper la memoria del estado adyacente del "
 "decodificador, revelar contenidos sensibles de memoria, provocar una denegación de servicio o "
 "potencialmente <b>ejecutar código arbitrario</b> mediante un flujo comprimido manipulado». Afecta a Brotli "
 "1.0.3 a 1.0.9, 1.1.0 y 1.2.0, y se corrige en <b>1.2.1</b>. Es un problema de cadena de suministro y no de un "
 "producto: viaja dentro de Node.js, .NET, PowerShell, cURL, las compilaciones de PHP para Windows, varios "
 "productos de Cisco, el gestor de Broadcom y Palo Alto. Entró en el catálogo el <b>27 de octubre</b> y el "
 "INCIBE marca «Explotación: Sí». Pero el aviso de <b>Microsoft</b>, publicado el 25 de octubre y revisado el "
 "26, el 30 y el 31, dice en su tabla de explotabilidad «divulgada públicamente: sí, <b>explotada: no</b>», con "
 "evaluación «explotación más probable», y precisa que «la descompresión Brotli <b>no está habilitada por "
 "defecto</b> en una instalación estándar de .NET o ASP.NET Core; las aplicaciones deben activarla "
 "manualmente».",
 "La discrepancia no es un error de nadie y conviene explicarla bien, porque es la que va a generar la "
 "discusión de la semana en un comité técnico: <b>las dos afirmaciones son verdad en su ámbito</b>. El "
 "componente Brotli está siendo explotado en algún producto, lo que justifica la entrada en el catálogo; y "
 "Microsoft no observa explotación en su propia superficie, que además exige activación manual. Lo que <b>no</b> "
 "se puede escribir, y aparecerá en algún resumen esta semana, es «Microsoft confirma explotación»: no lo hace. "
 "La utilidad práctica es doble. Primero, para priorizar: en el mundo .NET el riesgo real depende de si la "
 "aplicación activó la descompresión automática de respuestas, de modo que la pregunta al equipo de desarrollo "
 "es muy concreta y se contesta en una tarde. El INCIBE añade el mismo matiz para cURL: «puede alcanzar el "
 "decodificador vulnerable si se habilita la descompresión automática de respuestas; esta opción está "
 "desactivada por defecto, pero algunas aplicaciones o bibliotecas pueden activarla». Segundo, y es el "
 "aprendizaje de fondo: esta es la tercera vulnerabilidad de la semana que no está en un producto sino en un "
 "<b>componente que viaja dentro de otros</b>. Sin inventario de dependencias, no hay forma de responder a "
 "ninguna de las tres, y ahí es donde el inventario de componentes de software deja de ser un requisito "
 "burocrático del Reglamento de Ciberresiliencia y se convierte en la herramienta que se necesita el martes.",
 'El <a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111497" @L>aviso de Microsoft '
 'sobre CVE-2026-111497</a> y el '
 '<a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos/escritura-fuera-de-limites-en-php-para-'
 'windows" @L>aviso del INCIBE-CERT sobre PHP para Windows de 29 de octubre</a>.',
 "Detalle de versionado que ahorra una confusión: las compilaciones de <b>PHP para Windows</b> corregidas son "
 "la <b>8.5.12-1, 8.4.27-1, 8.3.36-1 y 8.2.35-1</b>, donde el sufijo «-1» indica la recompilación de Windows "
 "que incorpora Brotli 1.2.1; <b>el número de versión de PHP no cambia</b>. Quien compruebe solo la versión de "
 "PHP concluirá que está parcheado cuando no lo está."),
]

BULOS = [
 ("«La ISO publicó la norma 27028 sobre los atributos de los controles del 27002.»",
  "<b>Corrección a este boletín, edición 010.</b> No está publicada. La ficha de la <b>ISO/IEC 27028</b> dice "
  "«Stage: International Standard under publication [60.00]» desde el <b>20 de octubre de 2026</b>, y la línea "
  "«60.60 International Standard published» <b>aparece sin fecha</b>, es decir no se ha producido. La etapa "
  "60.00 suele resolverse en semanas, así que es razonable esperarla entre noviembre y enero, pero la ISO no "
  "publica fecha prevista y no debe darse por hecha. Lo que sí está publicada es la <b>ISO/IEC 27090</b>, de "
  "amenazas contra sistemas de IA, el 14 de octubre de 2026."),
 ("«Las directrices 03/2026 del Comité Europeo de Protección de Datos son sobre extraterritorialidad.»",
  "<b>Corrección a este boletín, edición 010.</b> Son «<b>Guidelines 03/2026 on web scraping in the context of "
  "generative AI</b>», es decir sobre el <b>rastreo web en el contexto de la IA generativa</b>, y <b>no existe "
  "en el repositorio del Comité ninguna directriz 03/2026 sobre extraterritorialidad</b>. El error cambia a "
  "quién afectaba la consulta que cerró el 30 de octubre: no a responsables de fuera de la Unión, sino a "
  "cualquiera que entrene modelos con datos rastreados de la web. Y el par real es más interesante, porque "
  "anonimización y rastreo web son las dos patas de la misma cadena de datos."),
 ("«El expediente 121/000104 del Congreso es el proyecto de ley de servicios digitales.»",
  "No lo es. Verificado hoy en el listado de proyectos de ley: el <b>121/000104</b> es el «Proyecto de Ley de "
  "medidas extraordinarias para el fortalecimiento y consolidación del Sistema para la Autonomía y Atención a "
  "la Dependencia». El de servicios digitales y ordenación de los medios es el <b>121/000068</b>, presentado el "
  "30 de julio de 2025. Los dos figuran «Concluido - (Caducado)», de modo que la conclusión no cambia, pero la "
  "referencia sí: quien cite el 121/000104 como el de servicios digitales estará citando otra ley."),
 ("«Los proyectos de ley del Gobierno de la legislatura fueron 110.»",
  "<b>Corrección a este boletín, edición 010.</b> Son <b>115</b>, del 121/000001 al 121/000115, sin ningún "
  "hueco en la numeración, y <b>los 115 con autor «Gobierno»</b>. De ellos, <b>89 figuran «Concluido - "
  "(Caducado)»</b>. El dato importa porque es la base del barrido que permite afirmar que no existe proyecto de "
  "transposición de NIS2: si el universo está mal contado, la ausencia no se sostiene. Ahora está contado y "
  "verificado."),
 ("«El paquete de infracciones de la Comisión es mensual y sale el día 1 o 2 de cada mes.»",
  "<b>Corrección de método de este boletín.</b> En 2026 <b>no ha sido mensual ni ha caído los días 1 y 2</b>. "
  "Las fechas reales de decisión son: 29 de enero, 10 de marzo, 28 de abril, 3 de junio, 7 de julio y 30 de "
  "septiembre, con el comunicado publicado <b>al día siguiente</b> en cada caso. La cadencia es de seis a ocho "
  "semanas en día variable. Vigilar solo los días 1 y 2 produce falsos negativos, y conviene redactar «decisión "
  "de 30 de septiembre, comunicado de 1 de octubre» para que no parezca un error."),
 ("«El plazo del 11 de diciembre obliga a los fabricantes a tener organismo notificado.»",
  "No. El <b>artículo 35.2</b> del Reglamento de Ciberresiliencia obliga a <b>los Estados miembros</b> y no a "
  "las empresas, es obligación <b>de medios</b> porque el texto dice que «se esforzarán por garantizar», y su "
  "umbral es <b>agregado en la Unión</b>, no un cupo por Estado. Presentarlo como un plazo que incumplen los "
  "fabricantes sería un error profesional grave. Y ojo al citar el texto español: el Diario Oficial dice "
  "literalmente «Los Estados se esforzarán», no «Los Estados miembros»."),
 ("«CERT-EU advirtió esta semana sobre las vulnerabilidades de PHP.»",
  "No. Su aviso <b>2026-018</b> es del <b>23 de octubre</b> y su última versión es de ese mismo día; el "
  "2026-019, sobre GitLab, es del 22. <b>CERT-EU no publicó ni actualizó nada entre el 26 de octubre y el 1 de "
  "noviembre.</b> Es un dato con significado propio: la Unión no elevó formalmente su postura en la semana en "
  "que PHP pasó a explotación confirmada; lo hicieron los CERT nacionales y los fabricantes. Lo mismo vale para "
  "el <b>CCN-CERT</b>: su alerta <b>AL 11/26</b> sobre PHP es del 21 de octubre y la AL 10/26 sobre Ivanti del "
  "14, y ninguna de las dos es de esta semana."),
 ("«Microsoft confirma la explotación de la vulnerabilidad de Brotli.»",
  "No lo hace. Su propio aviso dice «divulgada públicamente: sí, <b>explotada: no</b>», con evaluación "
  "«explotación más probable». Quien la da por explotada es el catálogo estadounidense, que la incorporó el 27 "
  "de octubre, y el INCIBE, que marca «Explotación: Sí». <b>Las dos cosas son verdad en su ámbito</b>: el "
  "componente se explota en algún producto y Microsoft no observa explotación en su propia superficie, que "
  "además exige activación manual de la descompresión. La frase correcta no atribuye la confirmación a "
  "Microsoft."),
 ("«La ETSI publicó esta semana una norma contra las ultrafalsificaciones.»",
  "La <b>ETSI TS 104 275</b> lleva fecha de portada de <b>septiembre de 2026</b>. Lo que cae en esta ventana es "
  "<b>el anuncio</b>, del 29 de octubre, no la publicación. Es el mismo tipo de desplazamiento que produce el "
  "relay de un CERT: el <b>CERTFR-2026-AVI-1385</b> está fechado el 26 de octubre y sus fuentes son más de "
  "diecisiete boletines de Broadcom <b>todos del 21 de octubre</b>; y el AVI-1383, del 26, relaya un boletín de "
  "Microsoft del 25. La fecha del intermediario nunca es la del fabricante."),
 ("«El IAF ha publicado un documento obligatorio nuevo de acreditación.»",
  "El <b>IAF y el ILAC cesaron operaciones el 1 de enero de 2026</b> y su sucesor es <b>Global Accreditation "
  "Cooperation Incorporated</b>. El sitio del IAF lo dice en cabecera: «este sitio web es un sitio heredado "
  "mantenido únicamente con fines de archivo y referencia». Sus documentos <b>siguen siendo válidos</b> hasta "
  "que Global ACI adopte los equivalentes, por las <b>resoluciones 2025-25 y 2025-29</b>, y eso hay que decirlo "
  "así cuando un cliente pregunte si su certificado sigue valiendo. Pero el lenguaje «documentos obligatorios "
  "del IAF» lleva diez meses desactualizado."),
 ("«Hubo un segundo ciberataque a la Universidad de Copenhague el 26 de octubre.»",
  "<b>Lo desmintió la propia universidad al día siguiente.</b> El lunes 26 anunció un ataque nuevo que motivó "
  "el apagado de dos sistemas administrativos; el <b>martes 27 rectificó</b>: no era un ataque nuevo, sino "
  "actividad dentro del sistema que al principio lo pareció, y el apagado se mantenía por estar ligado al "
  "ataque original. <b>No existe un segundo incidente</b>: quien lo cuente como dos está contando uno de más. "
  "Es, además, un caso de estudio en comunicación de crisis sobre el coste de calificar la causa de una "
  "anomalía antes de tenerla."),
 ("«El regulador suizo y el danés abrieron investigación formal esta semana.»",
  "Las dos notas son del <b>23 de octubre</b>, tres días antes de la ventana: la del supervisor suizo sobre el "
  "proveedor de software de las cajas de previsión y la del danés sobre el caso del registro central de "
  "personas. La prensa especializada las replicó el <b>26</b>, lo que crea una falsa ventana. Regla práctica "
  "que esta semana ha evitado dos admisiones indebidas: <b>cuando un medio informa de la actuación de un "
  "regulador, ir a la nota del regulador y tomar su fecha de publicación</b>, nunca la del medio."),
 ("«La Charité cifra en casi 140.000 los afectados por el ataque a su servidor web.»",
  "<b>La página propia de la Charité no da ninguna cifra.</b> El desglose que circula, con unos 46.000 "
  "empleados y estudiantes, 1.500 destinatarios de prensa y 90.000 personas que usaron el formulario de "
  "contacto, procede de respuestas de un portavoz a la consulta de un medio, y el total «casi 140.000» es una "
  "<b>suma redondeada hecha por el medio</b>, no una cifra publicada por la entidad. El incidente entra en este "
  "boletín con fecha de confirmación de 30 de octubre; la cifra, no."),
 ("«El Consejo Europeo adoptó conclusiones sobre soberanía digital a finales de octubre.»",
  "<b>No hubo Consejo Europeo en la ventana.</b> El anterior fue el 15 y 16 de octubre y el próximo es el "
  "<b>17 y 18 de diciembre de 2026</b>, según el aviso a medios que el propio Consejo publicó el 26 de octubre. "
  "Lo que hubo los días 29 y 30 fue la <b>cumbre bilateral UE-Canadá</b> en Montreal, que no adopta "
  "conclusiones del Consejo Europeo. Es el segundo lunes consecutivo que este bulo aparece con fecha distinta, "
  "lo que sugiere que se está generando automáticamente."),
 ("«Las normas armonizadas del Reglamento de IA llegan en 2026.»",
  "El plazo para las normas armonizadas de apoyo está ahora en <b>febrero de 2027</b>, según el boletín de "
  "CEN-CENELEC del 28 de octubre, que explica que la petición de normalización de la Comisión «se ha revisado "
  "para alinearse con los nuevos calendarios». Lo que sí existe ya es la primera, la <b>EN 18286:2026</b> sobre "
  "el sistema de gestión de la calidad, citada en el Diario Oficial el 14 de octubre de 2026. Cautela de "
  "atribución: esa entrada del boletín la firma la Confederación Europea de Sindicatos, no la Comisión ni el "
  "comité."),
 ("«El 2 de diciembre nace la obligación de marcar el contenido generado por IA.»",
  "No nace: <b>se agota un periodo de gracia</b>. La obligación de marcar en formato legible por máquina, del "
  "<b>artículo 50.2</b>, rige desde el <b>2 de agosto de 2026</b>, porque el artículo 50 está en el capítulo IV "
  "y no figura entre las excepciones del artículo 113. El 2 de diciembre vence el plazo que el artículo 111.4 "
  "concedió a los sistemas introducidos en el mercado <b>antes</b> de esa fecha. Lo que sí nace ese día son las "
  "dos prohibiciones nuevas del artículo 5.1, letras b bis) y b ter), que es un hito distinto y que casi nadie "
  "está contando."),
]

SILENCIO = [
 ("BOE", "Revisados íntegramente por la interfaz de datos abiertos los sumarios del 26, 27, 28, 29, 30 y 31 de "
  "octubre, <b>1.576 asuntos en todas las secciones</b> y no solo en la I, repartidos en seis ediciones y siete "
  "diarios, porque el día 28 tuvo dos ediciones por el real decreto de luto oficial por el accidente "
  "ferroviario de Urda. <b>Cero disposiciones generales</b> sobre ciberseguridad, NIS2, entidades críticas, "
  "DORA, Esquema Nacional de Seguridad, Instrucciones Técnicas de Seguridad, INCIBE, CNI, CCN o AESIA, y "
  "<b>cero menciones</b> de NIS2, entidades críticas, DORA o AESIA en todo el BOE de la ventana. Dato "
  "llamativo: los días <b>26 y 27 no hubo ningún asunto en la Sección I</b>, y toda la producción reglamentaria "
  "de la semana se concentró del 29 al 31. El <b>1 de noviembre no hubo edición</b>, confirmado porque la "
  "interfaz devuelve que la información no existe. Nota de método para quien repita el recuento: el JSON anida "
  "parte de los asuntos bajo claves de texto, de modo que un recorrido superficial del árbol devuelve unos "
  "1.548 y <b>pierde 28 asuntos</b>; la cifra correcta, con recorrido recursivo, es 1.576."),
 ("Congreso de los Diputados", "<b>Alcanzado por fin, y con resultado cerrado.</b> Llevaba dos ediciones "
  "declarado como fuente inaccesible, y esta semana se ha llegado al listado completo de proyectos de ley de la "
  "legislatura por otra ruta. <b>115 expedientes</b>, del 121/000001 al 121/000115, los 115 con autor "
  "«Gobierno», de los cuales <b>89 figuran «Concluido - (Caducado)»</b>. Verificados uno a uno los cuatro que "
  "este boletín sigue: <b>121/000088</b>, «Proyecto de Ley de protección y resiliencia de las entidades "
  "críticas», presentado el 18/03/2026, caducado; <b>121/000105</b>, «por la que se modifican diversas leyes "
  "para la digitalización y modernización del sector financiero», que era el vehículo de DORA, presentado el "
  "17/07/2026, caducado; <b>121/000096</b>, la ley orgánica de gobernanza de la IA, presentado el 28/05/2026, "
  "caducado; y <b>121/000068</b>, el de servicios digitales y medios, presentado el 30/07/2025, caducado. Y el "
  "hallazgo que cierra una afirmación que llevaba tres ediciones sin poder reconfirmarse: barridos los 115 "
  "títulos, <b>no existe ni un solo proyecto de ley de transposición de NIS2 en toda la legislatura</b>. La "
  "actividad de la Diputación Permanente sigue sin poder comprobarse en su propia ficha, pero su única huella "
  "en el BOE de la ventana son dos acuerdos de becas de formación de 13 de octubre, que son administrativos."),
 ("Consejo de Ministros", "Hubo <b>una sola reunión</b> en la ventana, la del martes 27 de octubre, y ninguna "
  "extraordinaria; comprobado contra el índice de referencias. Leída íntegra, el barrido devuelve <b>cero "
  "menciones</b> de ciber, ciberseguridad, NIS2, entidades críticas, DORA, inteligencia artificial, AESIA, "
  "Esquema Nacional o protección de datos. Dato limpio y citable: el <b>Ministerio para la Transformación "
  "Digital y de la Función Pública no llevó ni un solo asunto</b>, y la búsqueda literal de «Transformación "
  "Digital» y «Función Pública» en el texto completo devuelve cero coincidencias. La única aparición de la "
  "palabra «digital» en todo el documento es la del acuerdo de centros de datos, que está en este boletín. Dos "
  "asuntos con interés tangencial: límites de gasto plurianual para que el Instituto de la Juventud tramite un "
  "contrato de equipamiento de red inalámbrica, y la financiación del desarrollo y lanzamiento de los satélites "
  "PAZ 2 y SPAINSAT NG-III."),
 ("Audiencias públicas y consultas del Ministerio para la Transformación Digital", "<b>Comprobado y no se abrió "
  "ninguna nueva en la ventana.</b> En audiencia e información pública, la entrada más reciente cerró el "
  "<b>22 de octubre</b> y ninguna permanece abierta: era la del proyecto de orden de cese de elementos del "
  "servicio universal de telecomunicaciones, que conviene no confundir con el servicio postal universal del BOE "
  "del 29. En consultas públicas previas hay <b>dos abiertas, las dos publicadas antes de la ventana</b> y las "
  "dos con plazo corto, que están en la tabla de plazos: el EU Kids Act, publicada el 20 de octubre, y los "
  "bonos de conectividad, del 7. Para el archivo: la consulta previa que cubría el <b>Ómnibus Digital</b>, que "
  "modifica entre otras NIS2 y CER, cerró el 29 de marzo de 2026. Y dos expedientes ciber ya cerrados que "
  "conviene recordar porque son los que faltan: el real decreto sobre seguridad y resiliencia de las redes y "
  "servicios de comunicaciones electrónicas, cuya audiencia cerró el 31 de diciembre de 2025, y el real decreto "
  "sobre autoridades en relación con elementos digitales, materia del Reglamento de Ciberresiliencia, que cerró "
  "el 23 de enero de 2026. Ninguno de los dos ha salido."),
 ("CCN y CCN-CERT", "Alcanzado y con resultado mixto. <b>Tres publicaciones del CCN en la ventana, y las tres "
  "están en este boletín</b>: la metodología de evaluación de productos con IA el 29, la renovación de INÉS el "
  "28 y la actualización del catálogo CPSTIC el 26. <b>Ninguna alerta ni aviso de seguridad del CCN-CERT con "
  "fecha en la ventana</b>: las dos últimas de la serie AL son anteriores, la AL 11/26 sobre PHP del 21 de "
  "octubre y la AL 10/26 sobre Ivanti del 14. Matiz obligado y honesto: el <b>repositorio propio de avisos del "
  "CCN-CERT no es alcanzable</b> de forma automatizada, y el listado de actualidad que sí se ha leído muestra "
  "fecha de publicación pero no de última modificación, de modo que si el CCN-CERT revisó el contenido de la "
  "AL 11/26 durante la ventana, eso queda <b>no reconfirmado en fuente primaria esta semana</b>. Y un dato que "
  "dice mucho: la página doctrinal del CCN sobre NIS2 sigue fechada en <b>agosto de 2024</b> y continúa "
  "describiendo la directiva como la que «debería de haber sido traspuesta antes del 17 de octubre de 2024» y "
  "la de entidades críticas como «actualmente en proceso de transposición»."),
 ("ENS, Instrucciones Técnicas y registro de certificaciones", "Resultado parcial, y se declara como tal. Lo "
  "que sí se puede afirmar sin reserva: <b>no se publicó ninguna Instrucción Técnica de Seguridad nueva ni "
  "ninguna modificación de una existente en el BOE</b> de la ventana, barrido literal de los 1.576 asuntos con "
  "cero coincidencias. Lo que <b>no</b> se puede afirmar: que sigan siendo cuatro las vigentes, porque el "
  "portal del ENS, que es la lista autorizada, devuelve una redirección a un sistema de gestión de bots en "
  "todos los intentos. Igual ocurre con el <b>registro de entidades certificadas en el ENS</b>, de modo que "
  "esta semana <b>no hay total, ni certificaciones nuevas, ni tendencia</b>, y la cifra de doce certificaciones "
  "de la edición pasada no se puede continuar. Los dos puntos quedan <b>no reconfirmados en fuente primaria "
  "esta semana</b>. El régimen habilitante sigue siendo la disposición adicional segunda del Real Decreto "
  "311/2022, en su redacción dada por el Real Decreto 1125/2024."),
 ("INCIBE e INCIBE-CERT", "Alcanzado con reintentos, hasta ocho por dirección, porque el sitio alterna "
  "respuestas correctas, errores y conexiones cerradas: <b>ningún «no hay nada» de este boletín se apoya en un "
  "solo fallo</b>. <b>35 avisos</b> en la ventana, 21 generales y 14 de sistemas de control industrial, 27 de "
  "ellos críticos, que están en la sección de amenaza. <b>Dos entradas en la bitácora de ciberseguridad</b>, la "
  "de las vulnerabilidades de PHP el 29 y la del acceso no autorizado al identificador de una compañía de "
  "videojuegos el 27, con 11,7 millones de registros y la investigación ya concluida según su último estado "
  "oficial. El <b>blog no publicó nada</b>: su entrada más reciente sigue siendo del 17 de septiembre. En la "
  "sala de prensa, <b>una sola nota</b>, del 27 de octubre, sobre el cierre del programa RETECH con las "
  "comunidades autónomas, que no publica fecha límite y a la que no conviene atribuirle un plazo."),
 ("AEPD", "Alcanzada y con una sola publicación en la ventana, el decálogo de agentes de IA del 27 de octubre, "
  "que está en este boletín. <b>El blog no publicó nada</b>: su última entrada es del 21 de octubre, sobre el "
  "incremento de las notificaciones de brechas. <b>El informe mensual de brechas de octubre no había salido</b> "
  "al cierre de la ventana, verificado por doble vía. Y se declara una laguna concreta: el repositorio de "
  "resoluciones responde pero <b>ordena por relevancia y rechaza cualquier parámetro de orden o filtro</b>, de "
  "modo que <b>no se ha podido obtener el listado exhaustivo de resoluciones sancionadoras publicadas en la "
  "ventana</b>; ese extremo queda <b>no reconfirmado en fuente primaria esta semana</b>. Indicio, no "
  "confirmación: la última sanción española difundida por el Comité Europeo sigue siendo la del 22 de "
  "septiembre."),
 ("Diario Oficial de la Unión Europea y Tribunal de Justicia", "Barrido completo con resultado cerrado. "
  "<b>271 actos</b> publicados del 26 al 30 de octubre, con el <b>texto íntegro abierto de 260</b> y no solo el "
  "título, porque un barrido por título produce falsos negativos: <b>cero menciones</b> de las cinco normas que "
  "sigue este boletín. Los once no abiertos son todos correcciones de errores con acto base identificado y "
  "ninguno es de estas normas. El 31 de octubre y el 1 de noviembre no hubo publicación. En el Tribunal, los "
  "<b>72 avisos judiciales</b> de la ventana se publicaron todos en una sola edición, la del 26 de octubre, y "
  "se leyó el texto de 71: <b>cero coincidencias</b> con NIS2, CER, el Reglamento de Ciberresiliencia o DORA. "
  "Los dos únicos asuntos nuevos ante el Tribunal de Justicia son <b>peticiones de decisión prejudicial</b>, no "
  "recursos por incumplimiento, y van de aditivos alimentarios y de productos de doble uso. Los diecinueve "
  "avisos de «recurso interpuesto» son todos ante el Tribunal General, es decir de particulares, y versan sobre "
  "marcas, azúcar, competencia y función pública."),
 ("ENISA, CERT-EU y los esquemas de certificación", "<b>Comprobado y no hay nada en la ventana en ninguno de "
  "los tres.</b> ENISA: su última entrada es del <b>21 de octubre</b>, la declaración conjunta sobre PHP, y su "
  "última publicación del 22, un informe técnico sobre inventarios de componentes de software; lo único de la "
  "ventana es el anuncio de su comparecencia del 10 de noviembre, que está en este boletín. CERT-EU: su aviso "
  "más reciente es el <b>2026-019 del 22 de octubre</b>, sobre GitLab, y el 2026-018 sobre PHP es del 23 con "
  "última versión de ese día; <b>no publicó ni actualizó nada</b> entre el 26 y el 1. Esquemas: la plataforma "
  "única de notificación del Reglamento de Ciberresiliencia sigue en capacidad operativa inicial desde el 11 de "
  "septiembre, el <b>EUCC</b> sigue aplicable con organismos activos, el esquema de servicios gestionados sigue "
  "en consulta desde julio y el <b>esquema de servicios en nube sigue siendo solo un esquema candidato "
  "solicitado a ENISA, no adoptado</b>, con la página de la Comisión sin tocar desde el 9 de septiembre."),
 ("DORA, TIBER y los supervisores financieros", "<b>Comprobado y no hay nada.</b> Cero normas técnicas de nivel "
  "2 de DORA en todo 2026; ninguna designación nueva de proveedor tercero crítico, con la lista todavía en la "
  "de noviembre de 2025 y diecinueve entidades; ningún plan de supervisión, petición de información ni tasa "
  "publicada; ninguna pregunta frecuente nueva de las Autoridades Europeas de Supervisión. <b>TIBER-EU y "
  "TIBER-ES</b> sin un solo documento nuevo: todo el marco sigue siendo la versión de 2025. <b>JERS</b>, "
  "ninguna recomendación, informe ni aviso; sus últimas publicaciones son discursos del 1 y 2 de octubre. "
  "<b>ESMA</b>, dos publicaciones en la ventana y ninguna de resiliencia operativa digital, con el dato "
  "institucional de que su nueva presidencia tomó posesión el <b>1 de noviembre</b>. <b>Banco de España</b>, "
  "ninguna guía ni comunicación específica de resiliencia operativa, y ni memoria de supervisión ni informe de "
  "estabilidad financiera en la ventana. <b>DGSFP</b>, ninguna novedad: la última es del 13 de octubre."),
 ("CNMV, registros de comunicaciones al mercado", "<b>Barrido completado esta semana, y es la laguna de la "
  "edición pasada que se cierra.</b> Recorridos íntegramente los dos registros con el rango del 26 de octubre "
  "al 1 de noviembre y paginando hasta el final: <b>152 comunicaciones en el registro de otra información "
  "relevante, en sus dieciséis páginas, y 33 en el de información privilegiada, en sus cuatro</b>, <b>185 en "
  "total</b>. Barrido literal por ciber, ciberataque, brecha, incidente, indisponibilidad, interrupción, "
  "ransomware, intrusión, acceso no autorizado y fuga de datos: <b>cero coincidencias</b>. Lo comunicado son "
  "resultados trimestrales, programas de recompra, fondos de titulización, convocatorias de junta, operaciones "
  "corporativas, calificaciones crediticias e instrumentos financieros. Conclusión utilizable y ahora sí "
  "respaldada: <b>ninguna cotizada española comunicó al mercado un incidente de ciberseguridad en la "
  "ventana</b>. La sección de ciberseguridad de la CNMV, por su parte, no se ha tocado desde el 15 de octubre."),
 ("Normas, acreditación y NIST", "Comprobado apartado por apartado. <b>Familia ISO/IEC 27000</b>: ninguna "
  "publicación, retirada ni cambio de etapa en la ventana, verificado ficha por ficha sobre las 576 entradas "
  "del catálogo del comité de seguridad. <b>Familia 42000</b>: ningún cambio, sobre las 96 entradas del comité "
  "de inteligencia artificial, cuyo último movimiento es del 24 de octubre. <b>Comité europeo de IA</b>: "
  "ninguna norma publicada, enviada a encuesta ni aprobada, y ninguna entrada nueva en su propio sitio desde el "
  "14 de octubre. <b>Diario Oficial serie L</b>: la única decisión de ejecución sobre normas armonizadas "
  "publicada en la ventana es de <b>secadoras domésticas</b>, y ninguna referencia nueva del Reglamento de IA, "
  "del de Ciberresiliencia, de NIS2 ni del EUCC. <b>NIST</b>: nada más que el IR 8547, sin movimiento en el "
  "marco de ciberseguridad, el SP 800-53, el SP 800-171, el marco de gestión de riesgos de IA ni los FIPS 203, "
  "204 y 205. <b>ENAC</b>: nada desde el 14 de octubre. <b>CEN y CENELEC</b>: en su apartado de normas "
  "destacadas solo hay tres normas de aeronaves no tripuladas. <b>UNE</b> queda sin verificar en fuente "
  "primaria, porque su sitio rechaza el acceso automatizado, mitigado con que no hay ninguna resolución de "
  "normas UNE en el BOE de la ventana."),
 ("Microsoft, SAP, Fortinet, Broadcom, SonicWall y Atlassian", "Comprobados los seis y <b>sin boletín propio "
  "con fecha en la ventana</b>. <b>Microsoft</b>: su martes de parches fue el 13 de octubre y no hubo "
  "publicación fuera de ciclo de plataforma; lo que hay es el aviso de componente sobre Brotli del 25 de "
  "octubre, revisado el 26, el 30 y el 31, que está en la sección de amenaza, más actualizaciones rutinarias de "
  "navegador. <b>SAP</b>: nada, y su próximo día de parches es el <b>10 de noviembre</b>. <b>Fortinet</b>: su "
  "listado de 339 avisos tiene su publicación más reciente el <b>13 de octubre</b>. <b>Broadcom y VMware</b>: "
  "el aviso de la vulnerabilidad que entró en el catálogo el 28 tiene fecha de publicación inicial de <b>29 de "
  "julio</b> y última actualización de <b>19 de agosto</b>, de modo que no se tocó en la ventana aunque figure "
  "con estado abierto. <b>SonicWall</b>: su aviso más reciente es del 14 de octubre. <b>Atlassian</b>: en "
  "octubre solo su boletín mensual del día 20. Se declara que las notas de seguridad individuales de SAP y el "
  "portal de avisos de Siemens no son alcanzables, de modo que los dos boletines de Siemens sobre PHP están "
  "identificados por el relay del INCIBE y <b>no leídos en origen</b>."),
 ("Fuentes que no se han podido alcanzar, y se declaran", "Lista completa, porque no alcanzar una fuente no es "
  "lo mismo que que no haya nada. Bloqueadas por cortafuegos o captcha: el <b>portal del ENS</b> y con él la "
  "lista de Instrucciones Técnicas y el registro de certificaciones; el <b>catálogo CPSTIC</b> y la Guía "
  "CCN-STIC 105; el <b>repositorio de avisos del CCN-CERT</b> y el de guías CCN-STIC; las fichas individuales "
  "del <b>Congreso</b> y la <b>Diputación Permanente</b>, suplidas esta semana por el listado de proyectos de "
  "ley; el <b>Senado</b>; el <b>Supervisor Europeo de Protección de Datos</b>, cuyo apartado queda entero sin "
  "cubrir; el <b>comisionado federal alemán</b> y la conferencia de autoridades alemanas; el listado de "
  "resoluciones del <b>Garante</b> italiano más allá de su boletín; la autoridad británica, cuyo canal sirve "
  "contenido de 2024; el <b>equipo de respuesta belga</b> y el <b>centro nacional portugués</b>; las notas de "
  "prensa y el canal de avisos técnicos del <b>BSI</b>; el portal de <b>Siemens ProductCERT</b>; las páginas "
  "HTML de alertas de la agencia estadounidense, suplidas por el JSON del catálogo; <b>une.org</b>; la base de "
  "datos de comités de <b>CEN-CENELEC</b>; el repositorio de <b>OSCAL</b>; el buscador documental de "
  "<b>ENAC</b>; el <b>Plan Anual Normativo</b>, que no se ha localizado en ninguna página oficial vigente; las "
  "noticias institucionales de la <b>agencia catalana de ciberseguridad</b>, de la que sí se han leído sus dos "
  "alertas de la ventana, las dos de fraude a la ciudadanía; y el resto de <b>CSIRT autonómicos</b>, que no se "
  "han barrido. Y una limitación transversal que afecta a la datación: el archivo histórico de internet está "
  "bloqueado en este entorno, de modo que <b>no se puede datar de forma independiente la primera publicación</b> "
  "de ninguna página."),
 ("Prensa y agregadores, trampas de fecha", "Semana cargada en reciclaje, con <b>quince trampas comprobadas</b> "
  "contra la fuente propia y no contra el agregador, todas en la sección de correcciones. Los tres patrones que "
  "se han repetido y que conviene tener en la cabeza. Uno, <b>la replicación con tres días de retraso</b>: dos "
  "reguladores publicaron el 23 de octubre y la prensa especializada lo recogió el 26, justo en el primer día "
  "de la ventana. Dos, <b>el estado abierto que no es una actualización</b>: cuatro alertas de CERT y un aviso "
  "de fabricante figuran como vigentes o abiertos sin haberse tocado en semanas, y solo una de las cuatro "
  "alertas del CERT francés tuvo revisiones reales dentro de la ventana. Tres, <b>la fecha del intermediario "
  "tomada por la del fabricante</b>, que esta semana ha producido tres desplazamientos de hasta cinco días. "
  "Regla que ha funcionado las tres veces: ir al documento del emisor original y leer su propio historial de "
  "versiones, no el del que lo relaya."),
]

counts = {k: 0 for k in SEC}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1
