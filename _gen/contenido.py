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

NUM        = 12
FECHA_ISO  = "2026-11-09"
FECHA_TXT  = "9 de noviembre de 2026"
PERIODO    = "del 2 al 8 de noviembre de 2026"

TITULAR = ("La Unión activó su red de crisis por los ataques a la refrigeración y los llamó de gran escala, "
           "mientras el CERT del país donde empezó la campaña lleva veinticuatro días sin tocar su alerta y el "
           "fabricante del equipo que un CERT nacional nombra no tiene aviso porque lo retiró en 2016")

ENTRADA = ("Esta semana el caso de la refrigeración dejó de ser un expediente francés. El <b>4 de noviembre</b>, "
           "<b>ENISA</b>, la <b>Comisión</b>, el centro de ciberdelincuencia de <b>Europol</b>, la Red de CSIRT y, "
           "por primera vez, <b>EU-CyCLONe</b>, que es la red de enlace para crisis del artículo 16 de NIS2, "
           "firmaron una declaración conjunta que fecha el arranque el 11 de octubre, confirma <b>una nueva "
           "oleada el 1 y el 2 de noviembre</b> y califica los incidentes de <b>gran escala</b>. Y trae el gancho "
           "regulatorio que faltaba, porque recuerda que <b>desde el 11 de septiembre de 2026 los fabricantes "
           "deben notificar incidentes graves y vulnerabilidades explotadas por la plataforma única del "
           "Reglamento de Ciberresiliencia</b>: en esta campaña no hay ni un CVE, ni un aviso de fabricante que "
           "enlazar, y <b>Danfoss sigue sin publicar nada propio</b> sobre un producto que retiró del mercado en "
           "2016. En el extremo opuesto del rigor, la declaración conjunta <b>no da una sola cifra</b>, y la "
           "única que existe de una autoridad son los <b>más de 300 sistemas expuestos</b> que Grecia dice haber "
           "detectado el 14 de octubre. En España el movimiento real fue del <b>CCN</b>, que publicó el primer "
           "dato oficial de madurez frente a la IA ofensiva: <b>618 organismos evaluados, nota media de 47,5 "
           "sobre 100 y ninguno llega al nivel adecuado</b>. En la Unión, la Comisión aprobó su programa de "
           "trabajo para 2027 y <b>dejó fuera su propia propuesta de reforma de NIS2</b>. Y en infracciones hay "
           "un hallazgo que conviene tener a mano: <b>España acumula tres expedientes ciber</b>, porque al de "
           "NIS2 y al asunto de entidades críticas se suma una carta de emplazamiento por <b>DORA</b> que casi "
           "nadie ha contado.")

CLAVE_1 = ("La primera clave es la que un cliente de distribución alimentaria o de cadena de frío va a preguntar "
           "esta semana, y tiene una respuesta incómoda que conviene dar entera. Lo que ha cambiado no es la "
           "técnica, es <b>el nivel de interlocución</b>: con EU-CyCLONe firmando y con la calificación de gran "
           "escala, esto ya no se discute con el frigorista, se discute con la autoridad nacional. Y el "
           "argumentario que aguanta es el de <b>cadena de suministro</b>, porque está en el articulado y ahora "
           "tiene tres autoridades detrás. El <b>artículo 21.2.d) de NIS2</b> obliga a cubrir la seguridad de "
           "las relaciones con los proveedores directos, y el <b>21.3</b> añade algo que casi nadie cita: hay "
           "que tener en cuenta «las vulnerabilidades específicas de cada proveedor y <b>la calidad general de "
           "los productos</b> y las prácticas en materia de ciberseguridad de sus proveedores». Pues bien, la "
           "calidad general de los productos tiene aquí dos admisiones escritas y una fecha demoledora: "
           "<b>Copeland reconoce por escrito una vulnerabilidad en el XWEB EVO sin CVE y sin parche</b>, con la "
           "migración como única remediación, y <b>publica en el mismo documento las credenciales de fábrica "
           "Admin y Admin para toda la gama</b>, el modelo con soporte incluido; y Danfoss, en declaración a una "
           "revista sectorial y no en su propio canal de avisos, sitúa el <b>AK-SC355 retirado en 2016</b> y el "
           "<b>AK-SM800 en fin de vida en 2021</b>. Es decir: <b>un CERT nacional alerta en 2026 sobre un "
           "producto que el fabricante retiró hace diez años y para el que nunca publicó un aviso</b>. Eso es "
           "exactamente el supuesto del 21.3, y es un argumento que se defiende solo delante de un comité. La "
           "autoridad italiana ha ido un paso más allá y dirige sus medidas urgentes expresamente a «los "
           "servicios de mantenimiento conectados», es decir <b>nombra al frigorista como sujeto</b>. Y queda el "
           "nudo que el CERT francés señala dos veces en su propia alerta y que nadie ha resuelto: "
           "<b>comprobar las condiciones contractuales del seguro antes de cortar el envío de datos al "
           "frigorista</b>. La medida que respeta el contrato de mantenimiento no es la medida buena, y la "
           "medida buena puede romper la póliza.")

CLAVE_2 = ("La segunda clave es española y de calendario, y corrige al alza la lectura de la edición pasada sin "
           "contradecirla. La 011 estableció, barridos los 115 proyectos de ley de la legislatura, que <b>NIS2 "
           "nunca llegó a tener proyecto de ley</b> en el Congreso. Sigue siendo cierto, y esta semana se le "
           "añade el matiz que faltaba: el <b>Plan Anual Normativo de 2026</b>, leído íntegro, <b>sí tiene la "
           "transposición planificada</b>, con nombre y con dueño. Figura en el epígrafe de Seguridad Ciudadana "
           "como «<b>LEY DE COORDINACIÓN Y GOBERNANZA DE LA CIBERSEGURIDAD</b>», con el objetivo declarado de "
           "transponer la Directiva 2022/2555, y el dato accionable es de quién depende: <b>ministerio "
           "proponente, INTERIOR</b>, con Defensa y Transformación Digital como coproponentes. Eso anticipa qué "
           "autoridad competente va a salir de ahí, y conviene saberlo antes de aconsejar a un cliente con quién "
           "se va a entender. El mismo documento deja dos ausencias que también son datos: <b>ninguna mención a "
           "la Directiva de entidades críticas ni a entidades críticas</b> en todo el plan, coherente con que "
           "ese proyecto ya estaba en las Cortes y murió con la disolución; y el <b>régimen sancionador de "
           "DORA</b> no tiene norma propia, va dentro del anteproyecto de ley de digitalización y modernización "
           "del sector financiero, que no ha llegado nunca a las Cortes. Esa última laguna acaba de tener "
           "consecuencia: en el paquete de infracciones de julio la Comisión abrió a España <b>carta de "
           "emplazamiento por no notificar las medidas del artículo 53 de DORA</b>, cuyo plazo venció el 17 de "
           "enero de 2025. Con el contador de entidades críticas en {dias} días y {eur} euros y las Cámaras sin "
           "constituir hasta el 23 de diciembre, la frontera de lo posible está fijada: <b>nada con rango de ley "
           "se mueve este año</b>.").format(dias=CER_DIAS, eur=CER_EUR)

# (fecha texto, vivo, qué vence, a quién afecta)
PLAZOS = [
 ("10 nov 2026", True, "Vencen mañana <b>dos</b> plazos del catálogo estadounidense de vulnerabilidades "
  "explotadas, no uno: el de CVE-2026-111497, la escritura fuera de límites del descodificador Brotli, y el de "
  "CVE-2026-48356, en Adobe Commerce y Magento. Los dos entraron el 27 de octubre",
  "Cualquier organización con pila de Node.js o con la cadena de Brotli dentro de producto de terceros, que "
  "esta semana ya alcanza a software de red eléctrica y de gestión de edificios, y cualquiera con comercio "
  "electrónico sobre Magento"),
 ("10 nov 2026", True, "Martes de parches de Microsoft y día de parches de SAP, los dos el mismo día. En la "
  "ventana no hubo publicación de emergencia de ninguno de los dos para producto en local",
  "Todo el mundo. Conviene no planificar nada más para mañana"),
 ("10 nov 2026", True, "Se reúne el 125.º plenario del Comité Europeo de Protección de Datos, que es donde "
  "tocaría la versión final de las directrices sobre rastreo web en el contexto de la IA generativa, cuya "
  "consulta cerró el 30 de octubre",
  "Cualquiera que entrene modelos con datos rastreados de la web, y sus asesores"),
 ("10 nov 2026", True, "A las 18:00 está prevista la liberación de los avisos XSA-529 y XSA-530 del proyecto "
  "Xen, que figuran asignados y bajo embargo",
  "Proveedores de alojamiento y cualquier cliente con virtualización Xen o XenServer"),
 ("11 nov 2026", True, "Vence el plazo del catálogo de vulnerabilidades explotadas para CVE-2026-41709, en "
  "VMware ESX de Broadcom, que entró el 28 de octubre. Y es día de parches de Palo Alto Networks",
  "Centros de datos con VMware, que en España es casi cualquier gran empresa y administración"),
 ("11 nov 2026", True, "Cierra el periodo de aportaciones sobre la propuesta de Reglamento de desarrollo de "
  "nube e inteligencia artificial, abierto el 2 de julio de 2026, que incluye medidas sobre capacidad de "
  "procesamiento seguro de proveedores establecidos en la Unión",
  "Proveedores y usuarios de nube y de IA, y cualquiera con una posición sobre soberanía digital"),
 ("13 nov 2026", True, "Vence el plazo del catálogo de vulnerabilidades explotadas para CVE-2026-118527, en "
  "Ivanti Connect Secure, que entró el 30 de octubre. Curiosidad de secuencia: entró en el catálogo cuatro días "
  "antes de que existiera su registro CVE",
  "Cualquier organización con la pasarela Ivanti en el perímetro"),
 ("13 nov 2026", True, "Cierra a las 23:59 la consulta pública del Comité Europeo de Protección de Datos sobre "
  "las directrices 04/2026, de aplicación de la potestad de imponer multas administrativas en relación con "
  "otras medidas correctivas. Es la única consulta del Comité abierta hoy",
  "Responsables y encargados que negocien con autoridades, y despachos. Decide cuándo una autoridad multa en "
  "lugar de requerir"),
 ("13 nov 2026", True, "Arranca la campaña electoral, a las cero horas, y se cierra en la práctica la ventana "
  "de iniciativa administrativa",
  "Contexto: cualquier expediente normativo español que esperase movimiento antes de enero"),
 ("18 nov 2026", True, "Vence el plazo del catálogo de vulnerabilidades explotadas para CVE-2024-27834, en "
  "varios productos de Apple, que entró el 4 de noviembre. Es de 2024 y entra ahora",
  "Parque de dispositivos Apple corporativos, y en particular los de personas de perfil expuesto"),
 ("19 nov 2026", True, "Fecha límite de los tres dictámenes urgentes que el Consejo de Ministros pidió el 3 de "
  "noviembre a la Comisión Permanente del Consejo de Estado. Ninguno de los tres es el real decreto de centros "
  "de datos que esperábamos",
  "Nadie en ciberseguridad de forma directa. Se anota porque cierra la pregunta de si el expediente de centros "
  "de datos se movió"),
 ("20 nov 2026", True, "Vence el plazo del catálogo de vulnerabilidades explotadas para CVE-2026-19868, la "
  "elusión de SAML y de la autenticación multifactor en el servicio de red privada virtual de SonicWall, que "
  "entró el 6 de noviembre",
  "Mediana empresa española con SonicWall, que es una base instalada muy amplia, y solo si tiene SAML "
  "habilitado para esos inicios de sesión"),
 ("25 nov 2026", True, "Cierra la consulta EBA/CP/2026/17, sobre las normas técnicas de requisitos "
  "prudenciales de las empresas de servicios de inversión",
  "Empresas de servicios de inversión españolas"),
 ("29 nov 2026", True, "Elecciones a Cortes Generales, por el artículo 2 del Real Decreto 806/2026. "
  "Reverificado esta semana: el documento no tiene referencias posteriores ni nota de modificación",
  "Todo el calendario normativo español, y la respuesta a la pregunta de cuándo habrá ley de NIS2"),
 ("30 nov 2026", True, "Cierra el plazo de comentarios del NIST SP 800-82 Rev. 4, la guía de seguridad de "
  "tecnología operativa",
  "Quien audite entornos industriales, energía o agua. Esta semana, cualquiera con controladores de "
  "refrigeración en el inventario"),
 ("30 nov 2026", True, "Cierra el plazo de candidaturas de la XI edición de los premios de la Autoridad Vasca "
  "de Protección de Datos, con una categoría reservada a entidades públicas vascas y atención declarada a "
  "iniciativas de IA y de gestión de riesgos",
  "Clientes del sector público vasco que ya hayan hecho una evaluación de impacto sobre derechos fundamentales "
  "o un modelo de riesgos"),
 ("1 dic 2026", True, "Cierra la encuesta NIS360 de 2027 de ENISA, dirigida a autoridades nacionales y a "
  "entidades de los sectores de alta criticidad del anexo I de NIS2. Las entidades registradas reciben informe "
  "comparativo con sus pares",
  "Entidades esenciales del anexo I. Es la única comparativa europea gratuita que van a tener"),
 ("2 dic 2026", True, "<b>Reglamento de IA.</b> Se aplican el artículo 5.1, párrafo primero, letras ba) y bb), "
  "y los apartados 5.1 bis y 5.1 ter, es decir las dos prohibiciones nuevas de generación de contenido íntimo "
  "no consentido y de material de abuso sexual infantil, con sus dos párrafos de delimitación",
  "Cualquier proveedor de IA generativa de imagen o de vídeo, no solo los de aplicaciones de nudificación. Y "
  "con umbral distinto y más benigno para el responsable del despliegue"),
 ("2 dic 2026", True, "<b>Reglamento de IA, y es el plazo corto de verdad.</b> Vence el periodo de gracia del "
  "artículo 111.4, que es nuevo: los proveedores de sistemas que generan contenido sintético de audio, imagen, "
  "vídeo o texto <b>introducidos en el mercado antes del 2 de agosto de 2026</b> tienen que cumplir el artículo "
  "50.2, es decir marcado en formato legible por máquina y detectable como generado artificialmente",
  "Cualquier cliente que tuviera un asistente generativo en producción antes de agosto. Son tres semanas y "
  "media"),
 ("2 dic 2026", True, "Cierra la convocatoria de datos de la Comisión sobre las futuras directrices técnicas "
  "de los repositorios de anuncios del Reglamento de Servicios Digitales, abierta el 4 de noviembre dentro de "
  "la ventana. La Comisión dice que pretende dictar las directrices en 2028",
  "Plataformas en línea de muy gran tamaño y motores de búsqueda"),
 ("3 dic 2026", True, "Cierra la consulta de la propuesta de reglamento europeo de entornos digitales fiables "
  "para menores, abierta el 2 de octubre",
  "Plataformas, tiendas de aplicaciones, proveedores de IA conversacional y tecnología educativa"),
 ("4 dic 2026", True, "Cierra el plazo de comentarios del NIST SP 800-100 Rev. 1, el manual de seguridad de la "
  "información para la alta dirección",
  "Quien trabaje gobierno de seguridad con consejos y comités de dirección"),
 ("7 dic 2026", True, "Cierran dos plazos de comentarios del NIST el mismo día: el SP 800-221 Rev. 1, sobre el "
  "impacto empresarial del riesgo TIC en la cartera de riesgo corporativo, y el SP 800-185 Rev. 1, de funciones "
  "derivadas de SHA-3",
  "Cuantificación de riesgo integrada en el primer caso, y criptografía en alcance de certificación en el "
  "segundo"),
 ("11 dic 2026", True, "<b>Artículo 35.2 del Reglamento de Ciberresiliencia</b>: los Estados «se esforzarán "
  "por garantizar» un número suficiente de organismos notificados. Obliga a los Estados y no a las empresas, es "
  "obligación de medios y el umbral es agregado en la Unión. <b>Y el recuento no se ha podido reverificar esta "
  "semana</b>: el censo europeo no es consultable de forma automatizada sin clave",
  "Fabricantes de producto con elementos digitales. La última cifra verificada, del 26 de octubre, era cero "
  "organismos notificados en los veintisiete Estados"),
 ("16 dic 2026", True, "Se reúne el 126.º plenario del Comité Europeo de Protección de Datos",
  "Contexto de calendario para cualquier expediente pendiente del Comité"),
 ("18 dic 2026", True, "Cierra la llamada previa a comentarios del NIST SP 800-108 Rev. 2, de derivación de "
  "claves con funciones pseudoaleatorias, abierta el 4 de noviembre dentro de la ventana",
  "Quien esté en plan de migración poscuántica: la derivación de claves es una de las piezas que se reescribe "
  "aguas abajo de los FIPS 203, 204 y 205"),
 ("23 dic 2026", True, "A las diez horas, sesiones constitutivas del Congreso y del Senado, por el artículo 5 "
  "del Real Decreto 806/2026",
  "Es la primera fecha en la que se puede reintroducir cualquier iniciativa caducada, incluida la de entidades "
  "críticas, que sí tiene texto del que partir"),
 ("31 dic 2026", True, "Cierra a las 23:59 la consulta EBA/CP/2026/18, el proyecto de normas técnicas del "
  "marco de gestión del riesgo operacional, abierta el 26 de agosto. Es la pieza adyacente al riesgo TIC y "
  "cíber",
  "Bancos españoles, y la vía por la que las pérdidas por incidentes llegan al supervisor"),
 ("31 dic 2026", True, "Etapa siguiente y votación previstas de la EN ISO/IEC 42006:2026, la adopción europea "
  "de los requisitos para organismos que auditan y certifican sistemas de gestión de inteligencia artificial. "
  "Estado actual: en aprobación, con última etapa del 29 de octubre de 2026",
  "Organismos de certificación que quieran acreditarse para certificar en 42001, y clientes que esperen "
  "certificarse"),
 ("1 ene 2027", True, "La Especificación Ágil Europea pasa a ser entregable permanente del catálogo de CEN y "
  "CENELEC, con proceso simplificado y desarrollo por iteraciones sucesivas",
  "Cualquiera con cláusulas contractuales que fijen «la versión vigente» de una norma europea, y cualquier "
  "auditor que trabaje con referencias que cambien dentro del ciclo de certificación"),
 ("4 ene 2027", True, "Cierran dos consultas el mismo día: la EBA/CP/2026/19, de normas técnicas revisadas de "
  "decisiones conjuntas sobre requisitos prudenciales específicos de entidad, y la de EIOPA sobre el proyecto "
  "de declaración supervisora de procesos de venta de productos de inversión basados en seguros, a las 23:59",
  "Grupos españoles con colegio de supervisores en el primer caso, y aseguradoras y distribuidores en el "
  "segundo"),
 ("8 ene 2027", True, "Cierra la consulta del Consejo de Estabilidad Financiera sobre los principios de alto "
  "nivel de modernización regulatoria y supervisora, abierta el 14 de octubre. Un miembro del Consejo de "
  "Supervisión del BCE animó expresamente a responder el 6 de noviembre",
  "Entidades y asociaciones españolas del sector financiero"),
 ("15 ene 2027", False, "Cierra la convocatoria de datos de la ESMA sobre tokenización del colateral de las "
  "entidades de contrapartida central",
  "Entidades de contrapartida central y miembros compensadores"),
 ("30 ene 2027", False, "Entra en aplicación la documentación técnica actualizada del tipo libre de riesgo de "
  "EIOPA, publicada el 6 de noviembre",
  "Aseguradoras españolas bajo Solvencia II"),
 ("feb 2027", False, "Recogida anual del Cuestionario de Riesgo TI del Banco Central Europeo, aplazada desde "
  "septiembre de 2026 por la propia carta SSM-2026-0301",
  "Entidades significativas españolas"),
 ("1T 2027", False, "Entra en servicio el repositorio público de la EBA de peticiones de datos supervisores y "
  "de resolución",
  "Bancos españoles, y la medida de si el compromiso de reducir peticiones nacionales solapadas se cumple"),
 ("2 ago 2027", False, "Tres cosas del Reglamento de IA el mismo día: los areneros regulatorios nacionales "
  "deben estar operativos por el artículo 57.1, que se retrasó un año; los proveedores de modelos de IA de uso "
  "general introducidos antes del 2 de agosto de 2025 deben cumplir, por el 111.3; y la Comisión debe adoptar "
  "los actos delegados del artículo 2.13",
  "Proveedores de modelos de uso general, y quien esperase un arenero español en 2026"),
 ("2 sep 2027", False, "La Comisión debe dar orientaciones y plantilla del plan de vigilancia "
  "poscomercialización, por el artículo 72.3 del Reglamento de IA, que es nuevo",
  "Proveedores de sistemas de alto riesgo"),
 ("2 dic 2027", False, "<b>Alto riesgo del anexo III del Reglamento de IA</b>, capítulo III secciones 1, 2 y "
  "3. <b>Ya no es el 2 de agosto de 2026</b>: lo movió la modificación de 2026, por la nueva letra c)(i) del "
  "párrafo tercero del artículo 113",
  "Cualquier cliente con un plan de adecuación de alto riesgo construido sobre la fecha vieja, que está "
  "trabajando con una fecha derogada"),
 ("11 dic 2027", False, "Se aplican los requisitos principales de ciberseguridad del Reglamento de "
  "Ciberresiliencia, con seguridad desde el diseño y soporte de seguridad durante el ciclo de vida, incluida la "
  "remediación de vulnerabilidades sin demora",
  "Fabricantes de producto con elementos digitales, y cualquier cliente que compre equipo con software dentro. "
  "Es la fecha que convierte el caso de la refrigeración en un problema de producto"),
 ("28 ene 2028", False, "Los organismos notificados bajo la legislación del anexo I, sección A, del Reglamento "
  "de IA deben solicitar designación, por el artículo 43.3, que es nuevo",
  "Organismos notificados de máquinas, ascensores, juguetes y producto sanitario"),
 ("2 ago 2028", False, "<b>Alto riesgo del anexo I del Reglamento de IA.</b> Ya no es el 2 de agosto de 2027: "
  "lo movió la modificación de 2026, por la nueva letra c)(ii)",
  "Fabricantes de máquinas, ascensores, juguetes y producto sanitario con IA integrada como componente de "
  "seguridad"),
 ("dic 2028", False, "Fechas diferidas del nuevo marco de reporte supervisor de la EBA para liquidez, cargas "
  "de activos, benchmarking supervisor y reporte ESG",
  "Bancos españoles"),
 ("2 ago 2030", False, "Plazo del artículo 111.2 del Reglamento de IA para el alto riesgo heredado destinado a "
  "ser usado por autoridades públicas. Ojo, porque es fácil contarlo mal: <b>la fecha ya estaba en el texto de "
  "2024</b>; lo que cambió en 2026 es el disparador, que ya no es una fecha fija sino la fecha de aplicación "
  "del capítulo III",
  "Quien venda IA de alto riesgo al sector público: tiene techo absoluto aunque el sistema sea heredado"),
 ("31 dic 2030", False, "Plazo del artículo 111.1 del Reglamento de IA para los sistemas de IA que son "
  "componentes de los grandes sistemas de información del anexo X",
  "Administraciones con sistemas europeos de gran magnitud"),
]

TITS = {
 "es":  f"El CCN pone el primer número oficial a la preparación española frente a la IA ofensiva: 618 "
        f"organismos, 47,5 sobre 100 y ninguno llega al nivel adecuado",
 "eu":  "La Comisión activa su red de crisis por la refrigeración y, en el mismo programa de trabajo, deja "
        "fuera su propia reforma de NIS2",
 "fin": "La EBA mete la IA de frontera y las tecnologías cuánticas dentro del gobierno interno de la CRD, y "
        "España suma un tercer expediente ciber por DORA",
 "std": "SC 42 abre cuatro proyectos de IA en tres días y manda a revisión el informe de confiabilidad que "
        "media industria cita, mientras la 27028 sigue atascada en producción",
 "ai":  "El 2 de diciembre vencen dos obligaciones nuevas del Reglamento de IA, y una da tres semanas y media",
 "thr": "Mañana vencen dos plazos del catálogo de explotadas, y Cisco reeditó un parche de 9,8 sin cambiar el "
        "número de versión",
}

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = []

ITEMS += [

("es", f"Seguimiento del incumplimiento · a {FECHA_TXT}", True,
 f"El tanto alzado que la Comisión pide a España por entidades críticas llega a {CER_EUR} euros, y esta semana "
 f"aparece un tercer expediente ciber español que casi nadie ha contado",
 f"Este bloque va todas las semanas, se haya movido algo o no, porque la cifra sube sola y es el mejor "
 f"argumento disponible para explicar por qué un real decreto-ley es probable. A día de hoy han pasado "
 f"<b>{CER_DIAS} días</b> desde que venció el plazo de transposición de la <b>Directiva (UE) 2022/2557</b>, el "
 f"17 de octubre de 2024. Al importe diario de <b>{CER_DIARIO} euros</b> que la Comisión reclama en el asunto "
 f"<b>C-616/26</b>, eso da <b>{CER_EUR} euros</b>, muy por encima del mínimo de {CER_MINIMO} euros que el "
 f"escrito fija como suelo. El delta de esta semana son siete días, es decir <b>{CER_SEMANA} euros</b>. Las dos "
 f"comprobaciones obligatorias de cada lunes, hechas y con prueba de control superada: <b>no hay sentencia, ni "
 f"conclusiones, ni auto en el C-616/26</b>, barridos todos los tipos de documento del Tribunal para ese asunto "
 f"y para sus cinco hermanos, con la prueba de control de un asunto que sí tiene sentencia, que devuelve tres "
 f"documentos de tres tipos distintos; y <b>sigue sin haber número de asunto público del recurso por NIS2</b>, "
 f"con cero resultados por el grafo de citas y la prueba de control de entidades críticas devolviendo sus seis "
 f"asuntos.",
 f"Hay que decir dos cosas al dar esta cifra, y las dos protegen a quien la repite. La primera: es <b>lo pedido "
 f"por la Comisión, no lo impuesto</b>; solo el Tribunal fija el importe final y puede reducirlo, y la suma a "
 f"tanto alzado es <b>la mayor de las dos cantidades, no la suma de ambas</b>. La segunda, y es la que "
 f"convierte el dato en incentivo y no en anécdota: <b>el contador del tanto alzado se detiene al transponer, "
 f"no al dictarse sentencia</b>. Cada semana sin ley son {CER_SEMANA} euros más que ya no se recuperan "
 f"transponiendo después. Si llega sentencia condenatoria, el tanto alzado se congela en la fecha que fije el "
 f"Tribunal y arranca además la multa coercitiva de {CER_COERC} euros diarios, que es un régimen distinto y "
 f"peor. <b>La novedad de esta semana es que el recuento de expedientes españoles sube a tres.</b> Al de "
 f"<b>NIS2</b>, con decisión de demanda de 8 de julio de 2026 y expediente INFR(2024)0270, y al de entidades "
 f"críticas, ya en el Tribunal como C-616/26, se suma una <b>carta de emplazamiento por DORA</b>, expediente "
 f"<b>INFR(2026)2141</b>, por no notificar las medidas nacionales que aplican el capítulo VII del Reglamento "
 f"(UE) 2022/2554, de sanciones administrativas y medidas correctoras, cuyo plazo venció el <b>17 de enero de "
 f"2025</b>. Previsión, con horizontes y no con fechas inventadas: por ley ordinaria, no antes del <b>segundo "
 f"semestre de 2027</b> y con 2028 como caso central, porque las Cámaras no se constituyen hasta el 23 de "
 f"diciembre; por real decreto-ley, primer semestre de 2027 si hay gobierno en enero o febrero, y más probable "
 f"en entidades críticas que en NIS2 porque allí hay borrador caducado del que partir.",
 'El aviso del asunto en el <a href="http://data.europa.eu/eli/C/2026/3986/oj" @L>Diario Oficial, serie C, '
 'C/2026/3986 de 3 de agosto de 2026</a>, con las tres cifras leídas en su texto, y el '
 '<a href="https://ec.europa.eu/commission/presscorner/detail/en/inf_26_1376" @L>paquete de infracciones de 8 '
 'de julio de 2026</a>, donde están las tres cartas de emplazamiento por DORA a España, Francia y Letonia.',
 "Tres cautelas de método de esta semana, y dos corrigen al propio boletín. La primera: el desfase desde la "
 "decisión de demandar por NIS2 son <b>124 días</b>, no 125, frente a los <b>56 días</b> que tardó en "
 "publicarse el aviso del asunto español de entidades críticas. La segunda: <b>el paquete de infracciones de "
 "octubre se decidió y se comunicó el 1 de octubre de 2026</b>, no el 30 de septiembre; la fuente primaria no "
 "da esa fecha y usa la fórmula «hoy la Comisión ha decidido». Y la tercera, que importa para no volver a "
 "escribirlo mal: <b>no existe ningún paquete de infracciones de septiembre de 2026</b>; los de 2026 son seis, "
 "de enero, marzo, abril, junio, julio y octubre. Con cadencia de seis a ocho semanas, el siguiente toca entre "
 "mediados y finales de noviembre, y conviene vigilarlo el lunes que viene."),

("es", "CCN · 3 de noviembre de 2026", True,
 "El CCN publica el primer dato oficial español de madurez frente a la IA ofensiva, y es un cero útil: 618 "
 "organismos evaluados, nota media de 47,5 sobre 100 y ninguno alcanza el nivel adecuado",
 "El <b>Centro Criptológico Nacional</b> cerró el cuestionario de autoevaluación de IA ofensiva que mantenía "
 "abierto en su plataforma desde julio y publicó el informe de resultados. Las cifras, leídas en el propio "
 "documento: <b>618 organismos del sector público y privado</b> participaron, la nota media es de <b>47,5 "
 "puntos sobre 100</b>, que el CCN sitúa en nivel de <b>madurez inicial</b>, y <b>ninguna entidad alcanza los "
 "95 puntos</b> que corresponderían a un nivel adecuado de preparación. Las brechas se concentran en "
 "protección, gobernanza, identificación y gestión de riesgos, y cultura. El informe propone un plan de acción "
 "con <b>53 iniciativas priorizadas en cuatro bloques</b>, de las que <b>18 son de aplicación inmediata</b>, y "
 "lo que lo hace aprovechable es que las ancla una a una en medidas del <b>Anexo II del Esquema Nacional de "
 "Seguridad</b>: <b>op.exp.4</b> para parcheo, la familia <b>op.acc</b> para identidades con mención expresa a "
 "la <b>autenticación multifactor resistente al phishing</b>, <b>mp.sw.1</b> y <b>mp.sw.2</b> para desarrollo "
 "seguro y pruebas de aceptación, <b>op.ext.1</b>, <b>op.ext.3</b> y <b>op.pl.3</b> para cadena de suministro y "
 "adquisición, con <b>inventarios SBOM que permitan identificar dependencias de software, modelos, plugins y "
 "skills</b>, <b>op.mon.1</b> y <b>op.mon.3</b> para vigilancia, y la familia <b>op.cont</b> para continuidad y "
 "copias. La referencia metodológica es la guía de buenas prácticas CCN-CERT BP/36, de junio de este año.",
 "Porque es la primera línea base comparable que existe para un cliente español en ámbito ENS, y porque viene "
 "con el mapeo ya hecho. Delante de un órgano de dirección, el argumento se construye solo: <b>el regulador "
 "técnico nacional dice que nadie está preparado y que el marco válido para cerrarlo es el ENS que ya se "
 "aplica</b>. Dos consecuencias prácticas que conviene subrayar porque cambian evidencia concreta. Una, el "
 "<b>SBOM de componentes de IA</b>, y no solo de software, pasa a ser exigencia de op.ext.1: eso significa "
 "inventariar modelos, plugins y extensiones, que es justo lo que casi ningún inventario de proveedores "
 "recoge hoy. Dos, la <b>autenticación multifactor resistente al phishing</b> queda nombrada expresamente, de "
 "modo que el doble factor por mensaje de texto deja de servir como evidencia. Y hay un uso honesto de la nota "
 "media que conviene hacer bien: <b>son 618 participantes en una autoevaluación voluntaria, no 618 organismos "
 "auditados por el CCN</b>, y las autoevaluaciones voluntarias tienden a atraer a quien está mejor preparado, "
 "lo que hace el 47,5 todavía más incómodo.",
 'El informe de <a href="https://www.ccn.cni.es/es/actualidad-ccn/1402-estado-de-preparacion-de-las-entidades-'
 'frente-a-la-ia-ofrensiva" @L>estado de preparación de las entidades frente a la IA ofensiva</a>, en el índice '
 'de actualidad del CCN. El enlace lleva una errata tipográfica del propio organismo en la palabra ofensiva, y '
 'es la dirección válida.',
 "Es el único asunto del CCN en toda la ventana: su índice de actualidad declara <b>un solo elemento en "
 "noviembre de 2026</b>, frente a nueve en octubre. Y hay que declarar la laguna que lo acompaña, porque es "
 "grande: el <b>repositorio de avisos y alertas del CCN-CERT y el de guías CCN-STIC no se han podido "
 "alcanzar</b>, devuelven error con un reto anti robot, de modo que <b>no se puede afirmar nada sobre la "
 "actividad del CCN-CERT esta semana</b>. Dato indirecto y de fuente europea: en la tabla de avisos de la Red "
 "de CSIRT de la Unión sobre el caso de la refrigeración, la fila del CCN-CERT figura <b>sin aviso "
 "enlazado</b>."),

("es", "Plan Anual Normativo 2026", True,
 "NIS2 sí está planificada en España, se va a llamar Ley de Coordinación y Gobernanza de la Ciberseguridad y la "
 "propone Interior, no Transformación Digital",
 "Leído íntegro el <b>Plan Anual Normativo de 2026</b> de la Administración General del Estado, que es un "
 "documento anterior a la ventana y por tanto contexto verificado y no novedad de la semana, pero que matiza un "
 "hallazgo de la edición pasada. En el epígrafe <b>XIX, Seguridad Ciudadana</b>, apartado de leyes, figura la "
 "«<b>LEY DE COORDINACIÓN Y GOBERNANZA DE LA CIBERSEGURIDAD</b>», con el objetivo literal de transponer la "
 "<b>Directiva (UE) 2022/2555</b>, regular la seguridad de los sistemas y redes de las entidades de su ámbito, "
 "designar autoridades competentes, punto de contacto único y equipo de respuesta, y establecer las medidas de "
 "gestión de riesgos. <b>Ministerio proponente: INTERIOR. Coproponentes: DEFENSA y TRANSFORMACIÓN DIGITAL Y DE "
 "LA FUNCIÓN PÚBLICA.</b> El plan recoge <b>179 propuestas normativas</b>, de las que <b>61 incorporan Derecho "
 "de la Unión</b> y <b>36 transponen directivas</b>. Dos ausencias verificadas en todo el documento: <b>cero "
 "menciones a la Directiva 2022/2557 y a entidades críticas</b>, y cero entradas sobre centros de datos. Y una "
 "aparición que importa: el <b>régimen sancionador de DORA</b> no tiene norma propia, se desarrolla dentro del "
 "anteproyecto de «Ley por la que se modifican diversas leyes para la digitalización y modernización del sector "
 "financiero», que propone Economía.",
 "Porque cambia a quién llama un cliente y para qué se prepara. Que la ley la proponga <b>Interior</b> y no "
 "Transformación Digital anticipa de qué cultura administrativa va a salir la autoridad competente, y conviene "
 "decírselo a quien esté montando su interlocución. El contraste con la edición pasada es el dato: en "
 "<b>entidades críticas</b> hubo proyecto, llegó al Congreso y murió con la disolución, de modo que la "
 "legislatura siguiente tiene un texto del que partir; en <b>NIS2 nunca hubo texto en las Cortes</b>, pero sí "
 "hay iniciativa planificada con título y departamento, lo que es muy distinto de no existir. Pendiente y "
 "caducada no son lo mismo, y planificada y presentada tampoco. Y la tercera lectura es financiera: el régimen "
 "sancionador de DORA en España depende de un anteproyecto que <b>no ha llegado nunca a las Cortes</b>, y esa "
 "laguna acaba de costar una carta de emplazamiento de la Comisión.",
 'El <a href="https://transparencia.gob.es/content/dam/transparencia_home/publicidadactiva/normativa/pan2026/'
 'PAN%%202026.pdf" @L>Plan Anual Normativo 2026</a>, en el portal de transparencia, con el epígrafe de '
 'Seguridad Ciudadana y el reparto de ministerios leídos en el propio documento.',
 "Laguna declarada y relevante: el <b>dominio del Congreso devuelve error en las ocho rutas probadas</b>, de "
 "modo que el estado del expediente 121/000088 y la ausencia de proyecto de NIS2 <b>no se han podido "
 "reverificar esta semana</b>. Se arrastra lo verificado en la edición 011 sobre los 115 expedientes, y se dice "
 "que es arrastre y no reconfirmación. La fecha de aprobación del propio plan tampoco está verificada: el "
 "documento no la lleva en portada y el canal que la daría no responde."),
]

ITEMS += [

("es", "APDCAT · 3 de noviembre de 2026", False,
 "La autoridad catalana abre un plan de auditoría preventiva sobre 48 entidades, y entra por las diputaciones "
 "para alcanzar a los municipios que dependen de sus plataformas",
 "La <b>Autoritat Catalana de Protecció de Dades</b> puso en marcha un <b>Plan de Auditoría Preventiva</b> con "
 "alcance exacto declarado: <b>44 entes locales</b>, que son 14 municipios de la provincia de Barcelona y 10 de "
 "cada una de Girona, Lleida y Tarragona, <b>más las cuatro diputaciones</b>, es decir <b>48 entidades</b>, con "
 "un límite máximo de 50 fijado por los recursos disponibles. Dos objetos de control: la <b>designación formal "
 "del delegado de protección de datos</b>, su comunicación y actualización ante la autoridad y la publicación "
 "accesible de su contacto; y la <b>configuración de las galletas</b>, con información clara sobre finalidades, "
 "base jurídica, destinatarios y plazos de conservación, coherencia entre la política publicada y el "
 "tratamiento efectivo, mecanismos de consentimiento <b>sin patrones manipuladores</b> y ausencia de "
 "instalación de galletas antes del consentimiento. El método declarado es técnico y reproducible: carga y "
 "ejecución de galletas y comprobación del comportamiento <b>antes y después del consentimiento</b>.",
 "Por la vía de entrada, que es lo aprovechable y lo dice la propia autoridad: las diputaciones entran "
 "expresamente porque prestan los servicios tecnológicos, plataformas e infraestructuras de los municipios "
 "pequeños. Eso convierte al <b>prestador tecnológico en el punto donde se gana o se pierde el cumplimiento de "
 "decenas de entes</b>. Si un cliente presta servicios digitales a entes locales catalanes, su banner y su "
 "gestor de consentimiento están dentro del alcance de hecho, aunque no figure en la lista de 48. La segunda "
 "lectura es de prueba: el criterio de patrón oscuro queda ligado a una comprobación técnica reproducible, la "
 "carga de galletas antes del consentimiento, que es exactamente lo que se audita después y lo que un cliente "
 "puede verificar él mismo esta semana con el inspector del navegador. Y el control de delegado de protección "
 "de datos es el más barato de aprobar y el más común de fallar, porque no basta con designarlo: hay que "
 "haberlo comunicado y haber mantenido actualizados sus datos.",
 'La nota del <a href="https://www.apdcat.cat/ca/actualitat/noticies/2026/APDCAT-Pla-Auditoria-Preventiva" @L>'
 'Plan de Auditoría Preventiva de la APDCAT</a>, con el alcance y los criterios tomados de su propio texto.',
 "Dato de calendario que no se ha podido cerrar y que conviene no publicar a ciegas: la edición pasada situaba "
 "la <b>entrada en vigor de la Circular 1/2026 de la APDCAT sobre videovigilancia el 8 de noviembre</b>, es "
 "decir ayer. <b>No está reconfirmado</b>: la fecha vive en la disposición final publicada en el diario oficial "
 "catalán, cuyo documento se renderiza por guion y no entrega el texto, y existe además una <b>corrección de "
 "errores</b> de esa circular que tampoco se ha podido fechar ni leer y que podría afectar al cómputo. Lo que "
 "sí está verificado es la nota de la autoridad de 19 de octubre: la circular es <b>disposición de obligado "
 "cumplimiento</b> para administraciones, entidades públicas, universidades, colegios profesionales y entidades "
 "privadas cuando ejercen funciones públicas, y <b>deroga la Instrucción 1/2009</b>."),

("es", "INCIBE · 3 a 6 de noviembre de 2026", False,
 "El INCIBE coordina tres divulgaciones en producto de fabricantes españoles de nicho, dos marcadas como día "
 "cero, y una de ellas mezcla datos bancarios con códigos de acceso físico",
 "El <b>INCIBE</b> ejerció de autoridad de numeración de vulnerabilidades sobre tres proveedores que no "
 "aparecen en ningún boletín internacional. El <b>5 de noviembre</b>, aviso INCIBE-2026-841 sobre "
 "<b>MatchPoint, de TPC Software</b>, plataforma de gestión de centros deportivos, importancia crítica, con "
 "<b>siete vulnerabilidades</b> y hasta <b>9,9 en CVSS versión 4</b>. La que importa es un acceso directo a "
 "objeto por referencia insegura en la interfaz de programación, que <b>confía en una cabecera HTTP para "
 "decidir en nombre de quién actúa, sin comprobar autorización</b>: con identificadores secuenciales permite "
 "acceder a datos personales, bancarios, financieros, mensajes privados y <b>códigos QR de acceso físico</b>, y "
 "además modificar cuentas, cambiar contraseñas, suplantar identidades y transferir saldos. Acompañan una "
 "credencial estática embarcada en la aplicación móvil, credenciales en claro en el almacenamiento local, "
 "inyección de SQL por el canal de notificaciones, un punto final sin autenticación y un gestor de confianza "
 "que <b>acepta cualquier certificado</b> con tráfico sin cifrar permitido. El <b>6 de noviembre</b>, "
 "INCIBE-2026-843, <b>inyección de SQL en SIREC, de Atmira</b>, plataforma de gestión de cobros y recuperación "
 "de deudas, 8,7 en CVSS versión 4, marcada como día cero y con el fabricante declarando que lo corrigió el 16 "
 "de octubre. Y el <b>3 de noviembre</b>, múltiples vulnerabilidades en <b>ALO Suite, de AM System</b>.",
 "Porque es riesgo de tercero en estado puro y en proveedores que ningún feed internacional va a avisar. El "
 "caso de la plataforma deportiva es material de formación para el <b>artículo 21.2.d) de NIS2</b> y para "
 "<b>op.ext.1 del ENS</b>: una aplicación que mezcla datos financieros con control de acceso físico, con "
 "credencial embarcada y validación de certificado desactivada, es el ejemplo de por qué la evaluación de "
 "proveedores no puede quedarse en un cuestionario firmado. El de la plataforma de cobros entra por otra "
 "puerta, la de externalización de entidades financieras, y conviene cruzarlo con el inventario de encargados. "
 "Lo accionable esta semana es corto: si cualquiera de los tres está en el inventario de proveedores de un "
 "cliente, toca notificación al proveedor y revisión del acuerdo de niveles de servicio de seguridad.",
 'Los avisos de <a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos/multiples-vulnerabilidades-'
 'en-matchpoint-de-tpc-software" @L>MatchPoint</a> y de <a href="https://www.incibe.es/incibe-cert/alerta-'
 'temprana/avisos/inyeccion-sql-en-sirec-de-atmira" @L>SIREC</a> en el canal de alerta temprana del '
 'INCIBE-CERT.',
 "El aviso de <b>ALO Suite queda no confirmado</b>: su fecha se ha tomado del listado paginado y no se ha "
 "abierto su ficha individual, de modo que no se ha leído su fecha propia ni su historial de versiones. Y "
 "conviene registrar la intermitencia del sitio, porque es un riesgo de falso negativo documentado: en el "
 "barrido de esta semana, peticiones idénticas alternaron respuesta correcta y error, con casos de <b>hasta "
 "cinco errores seguidos antes de servir la página</b>. Ningún cero de esta sección se apoya en un primer "
 "fallo."),

("es", "Consejo de Ministros · 3 de noviembre de 2026", False,
 "El Gobierno no aprobó ninguna norma de ciberseguridad, pero sí autorizó un contrato de seguridad de los "
 "sistemas de la Seguridad Social por 22,9 millones de euros, y el real decreto de centros de datos no aparece",
 "Única reunión del Consejo de Ministros de la ventana, verificado en el índice de referencias. Leída la "
 "referencia íntegra, <b>cero disposiciones</b> sobre ciberseguridad, NIS2, entidades críticas, centros de "
 "datos, inteligencia artificial o gobernanza de datos. Los tres <b>dictámenes urgentes</b> pedidos a la "
 "Comisión Permanente del Consejo de Estado, con plazo el <b>19 de noviembre</b>, son el real decreto del Plan "
 "de Evaluaciones Estratégicas, la modificación del estatuto de la Agencia Estatal de Evaluación de Políticas "
 "Públicas y los estatutos del Instituto de Crédito Oficial: <b>ninguno es el real decreto de centros de "
 "datos</b> cuyo dictamen la edición pasada situaba venciendo el 5 de noviembre. Lo que sí hay, y conviene "
 "corregirlo respecto de un primer barrido, es contratación: el <b>acuerdo que autoriza el contrato de "
 "prestación de los servicios de seguridad de los sistemas de información</b> de la Gerencia de Informática de "
 "la Seguridad Social, con valor estimado de <b>22.925.795,06 euros</b>, más un contrato de desarrollo y "
 "mantenimiento de los sistemas de la misma gerencia por 130,4 millones, licencias de hiperautomatización para "
 "la Dirección General de la Policía y mantenimiento informático de la Guardia Civil.",
 "Por dos razones, y ninguna es la norma que no salió. La primera es de expectativas: con el ministerio de "
 "Transportes en despacho ordinario asumido por el vicepresidente primero desde el 4 de noviembre, con las "
 "Cortes disueltas y con elecciones el 29, <b>no va a salir nada normativo de ciberseguridad en lo que resta "
 "de 2026</b>, y conviene decírselo así a un cliente que esté esperando. La segunda es que el contrato de 22,9 "
 "millones es un dato de mercado útil: es la medida de lo que una administración central española considera "
 "que cuesta operar la seguridad de un sistema crítico de alcance estatal, y sirve de referencia cuando un "
 "cliente del sector público discute presupuesto.",
 'La <a href="https://www.lamoncloa.gob.es/consejodeministros/referencias/Paginas/2026/20261103-referencia-'
 'rueda-de-prensa-ministros.aspx" @L>referencia del Consejo de Ministros de 3 de noviembre de 2026</a>, leída '
 'íntegra.',
 "Dos avisos de método. Uno: el <b>patrón de dirección web de las referencias del Consejo de Ministros ha "
 "cambiado</b> y el formato antiguo ni redirige ni falla con claridad, deja la conexión caída, que es la forma "
 "más fácil de confundir fuente inalcanzable con reunión inexistente. Dos, y es el más importante: la "
 "referencia <b>está truncada en origen</b>, se corta a mitad de palabra en el último asunto publicado, de modo "
 "que lo que hay es todo lo que La Moncloa sirve. Y sobre el real decreto de centros de datos: no llegó al BOE "
 "y no pasó por Consejo de Ministros, pero <b>el cero de la base de dictámenes del Consejo de Estado no es "
 "concluyente</b>, porque esa base lleva un mes y un día de retraso, comprobado con consulta propia: su "
 "dictamen más reciente tiene fecha de aprobación de 8 de octubre de 2026."),

("es", "Refrigeración · España", False,
 "La campaña del frío llega a España como alerta y no como víctima, y la mejor pieza no está en ningún CERT "
 "sino en prensa generalista a partir de una patronal",
 "Dos movimientos españoles, y <b>ninguno de los dos es un incidente</b>. El primero: la <b>Agència de "
 "Ciberseguretat de Catalunya ordenó desconectar la conexión centralizada de los equipos que controlan la "
 "temperatura del Banc de Sang i Teixits</b>, a raíz del ataque al operador francés de la sangre. Lo confirma "
 "su director clínico, que precisa que es provisional y que no alteró mucho la forma de trabajar porque ya hay "
 "<b>tres comprobaciones independientes</b> y, simplificando, ninguna cámara está conectada directamente a "
 "Internet. El segundo: el centro de ciberseguridad de la Comunitat Valenciana avisó de forma <b>preventiva a "
 "21 empresas</b> no nombradas de la distribución alimentaria, contactadas a través de su patronal, que usan la "
 "misma tecnología y el mismo fabricante de refrigeración que supermercados europeos ya atacados, con "
 "<b>ningún ataque confirmado y ninguna petición de rescate</b> en la Comunitat.",
 "Porque es exactamente el momento en el que un cliente llama, y la respuesta correcta no es técnica sino de "
 "diseño. Lo que hay que llevarse del banco de sangre catalán es la frase del director clínico: la desconexión "
 "<b>no alteró mucho el trabajo porque ya había tres comprobaciones independientes</b>. Eso es redundancia de "
 "verificación, y es lo que separa un susto de una pérdida. La pregunta para cualquier cliente con cadena de "
 "frío crítica no es si el controlador está parcheado, es <b>quién puede cambiar una consigna de temperatura "
 "por telemetría, con qué credencial, y si la alarma de umbral la vigila alguien ajeno al que puede "
 "moverla</b>. Si la misma persona o el mismo sistema puede mover la consigna y silenciar la alarma, no hay "
 "control. Y del aviso valenciano hay que quedarse con el canal y no con el contenido: fue una <b>patronal "
 "sectorial</b> la que puso en contacto al centro de ciberseguridad con 21 empresas en un día. Eso funciona "
 "mejor que cualquier boletín, y conviene saber qué patronal cubre a cada cliente antes de necesitarla.",
 'La nota de la <a href="https://www.apdcat.cat/ca/actualitat/noticies/2026/APDCAT-Pla-Auditoria-Preventiva" '
 '@L>autoridad catalana</a> para su contexto institucional y la declaración conjunta de la Unión del 4 de '
 'noviembre, en <a href="https://www.enisa.europa.eu/news/joint-statement-on-cyber-incidents-in-refrigeration-'
 'systems-across-the-eu" @L>ENISA</a>, que es el documento que enmarca las dos medidas.',
 "Se etiquetan como lo que son y no se inflan: <b>desconexión preventiva</b> y <b>aviso preventivo</b>, no "
 "incidentes, y así están en el registro, fuera del recuento. Ninguna de las piezas que recogen la orden "
 "catalana la fecha, de modo que <b>no se puede datar la medida, solo su publicación</b>. El fabricante del "
 "aviso valenciano no se identifica, y la atribución de una vulnerabilidad conocida que hace un auditor en esa "
 "misma pieza es <b>opinión de un tercero, no vector publicado</b>. Y la cifra de 300 supermercados franceses y "
 "los 50 grados que circulan en la misma cobertura son de prensa que <b>no cuadra sus propias cifras</b>."),
]

ITEMS += [

("eu", "ENISA, Comisión, Europol, Red de CSIRT y EU-CyCLONe · 4 de noviembre de 2026", True,
 "La Unión activa su red de enlace para crisis por los ataques a la refrigeración, los califica de gran escala "
 "y pone el Reglamento de Ciberresiliencia encima de la mesa",
 "Declaración conjunta de <b>ENISA, la Comisión por su dirección general de redes de comunicación, el Centro "
 "Europeo de Ciberdelincuencia de Europol, la Red de CSIRT de la Unión y EU-CyCLONe</b>. Literales que "
 "conviene citar tal cual: «<b>desde el 11 de octubre de 2026</b>, varios sistemas de refrigeración comercial y "
 "dispositivos similares se han visto afectados por incidentes de ciberseguridad en un número de Estados "
 "miembros»; «<b>tras una nueva oleada de incidentes ocurrida el 1 y el 2 de noviembre</b>» se aconseja actuar "
 "de inmediato para reducir la exposición; y «<b>dada la naturaleza de gran escala de estos incidentes</b>», la "
 "cooperación, el intercambio rápido de información y la respuesta coordinada a escala europea son esenciales. "
 "El hallazgo de gobernanza es la firma: <b>EU-CyCLONe no estaba en la declaración conjunta del 21 de octubre "
 "sobre PHP</b>, que firmaron la Comisión, ENISA, el CERT de las instituciones europeas, Europol y la Red de "
 "CSIRT. EU-CyCLONe es la red de organizaciones de enlace para crisis del <b>artículo 16 de NIS2</b>, y además "
 "el CERT institucional deja de ser firmante separado. Y el cierre regulatorio lo da el propio documento: "
 "<b>desde el 11 de septiembre de 2026 los fabricantes de productos de hardware y software deben notificar "
 "incidentes graves y vulnerabilidades explotadas activamente por la plataforma única de notificación del "
 "Reglamento (UE) 2024/2847</b>, y los requisitos principales de ciberseguridad se aplican desde el 11 de "
 "diciembre de 2027.",
 "Porque cambia el nivel de la conversación y porque da el argumento que faltaba. Un cliente de distribución "
 "alimentaria ya no está ante un incidente francés, está ante un expediente europeo con la red de crisis de "
 "NIS2 movilizada y con la calificación oficial de gran escala, y eso condiciona cómo se cuenta al consejo y "
 "cómo se enfoca la notificación del artículo 23. El gancho del <b>Reglamento de Ciberresiliencia</b> es el "
 "mejor disponible, y conviene usarlo con precisión: la obligación de notificar de los fabricantes <b>ya estaba "
 "en vigor un mes antes de que empezara la campaña</b>, y lo que tenemos verificado es que Copeland admite una "
 "vulnerabilidad <b>sin CVE</b>, que Danfoss <b>no ha publicado ningún aviso</b> sobre esto y no tiene ninguno "
 "para la serie que un CERT nacional nombra, que la alerta francesa no tiene ni un aviso de fabricante que "
 "enlazar y que la Red de CSIRT pone un guion en el campo de CVE. <b>La pregunta correcta no es si lo han "
 "incumplido, es si se ha notificado algo por esa plataforma y cómo se sabría.</b> Y es la segunda vez en tres "
 "semanas que el artículo 14 del Reglamento de Ciberresiliencia se invoca en una declaración conjunta por una "
 "campaña activa, después de la de PHP: eso es un patrón y merece contarse como tal.",
 'La <a href="https://www.enisa.europa.eu/news/joint-statement-on-cyber-incidents-in-refrigeration-systems-'
 'across-the-eu" @L>declaración conjunta de 4 de noviembre de 2026</a> en ENISA, replicada por la Comisión, y '
 'el aviso <a href="https://raw.githubusercontent.com/enisaeu/CNW/main/advisories/2026/CNW-2026-05_retail-'
 'incidents.md" @L>CNW-2026-05 de la Red de CSIRT</a>, de 3 de noviembre, con la tabla de avisos país por país.',
 "Lo que la declaración <b>no dice</b> es tan importante como lo que dice, y hay que decirlo: <b>no nombra "
 "ningún Estado miembro, ninguna cadena, ningún fabricante, ningún CVE y no da una sola cifra</b>. Quien quiera "
 "atribuir a un fabricante concreto no puede hacerlo con este documento. El aviso de la Red de CSIRT cierra de "
 "paso dos lagunas que arrastrábamos: su tabla acredita que <b>doce de los treinta miembros han publicado "
 "aviso</b>, que el <b>INCIBE-CERT sí publicó</b>, aunque su pieza es del 20 de octubre y trata de la ola "
 "francesa y no de la nueva, y que <b>el CCN-CERT sigue sin publicar nada</b>, con la fila en blanco. La "
 "afirmación de que es la primera firma de EU-CyCLONe se sostiene frente a los dos comparables leídos, el de "
 "PHP y el anterior de SharePoint, pero <b>no se afirma que sea la primera de la historia</b>, porque no se ha "
 "recorrido todo el archivo de declaraciones conjuntas."),

("eu", "Programa de trabajo de la Comisión para 2027 · COM(2026) 710, de 4 de noviembre de 2026", True,
 "La Comisión prioriza para 2027 la refundación del marco de certificación y la seguridad de la cadena de "
 "suministro, y deja fuera su propia propuesta de reforma de NIS2",
 "El programa de trabajo adoptado el <b>4 de noviembre de 2026</b> incluye en su <b>anexo II de propuestas "
 "pendientes prioritarias</b>, punto 10, «EU Cybersecurity Act», una sola entrada: la <b>COM(2026) 11 final, "
 "procedimiento 2026/0011</b>, de 20 de enero de 2026, propuesta de reglamento sobre ENISA, el marco europeo de "
 "certificación de la ciberseguridad y <b>la seguridad de la cadena de suministro de TIC</b>, que derogaría el "
 "Reglamento (UE) 2019/881. En el punto 5 figura el <b>Digital Omnibus</b>, COM(2025) 837, que modifica entre "
 "otros los Reglamentos 2016/679 y 2023/2854 y <b>las Directivas 2022/2555 y 2022/2557</b>. Y el hallazgo es "
 "una ausencia verificada a conciencia: la <b>COM(2026) 13, propuesta de Directiva que modifica NIS2 por "
 "medidas de simplificación y alineación con el nuevo Reglamento de Ciberseguridad, NO aparece en el anexo "
 "II</b>. Barridas las referencias del documento, las propuestas de 2026 presentes son veintiuna y la 13 no "
 "está, y los procedimientos 2026 presentes no incluyen el 2026/0012. Trampa evitada: el procedimiento "
 "2026/0013 sí aparece, pero corresponde a otra propuesta, la de redes digitales. El <b>anexo I de nuevas "
 "iniciativas no contiene ninguna de ciberseguridad</b>, y las cuatro apariciones de la palabra en los anexos "
 "están todas en el punto 10 del anexo II.",
 "Porque es la respuesta a la pregunta de qué va a cambiar y qué no en 2027, y la respuesta tiene dos mitades "
 "con consecuencias opuestas. La primera: <b>el texto de NIS2 que hay es el que va a seguir habiendo un "
 "tiempo</b>, de modo que quien esté en plan de adecuación puede trabajar sobre el articulado vigente sin temor "
 "a que la simplificación se lo reescriba en 2027. Eso es una buena noticia operativa que conviene dar. La "
 "segunda es donde sí hay movimiento, y es el flanco que casi nadie está mirando: <b>certificación y cadena de "
 "suministro TIC</b>. El nuevo Reglamento de Ciberseguridad derogaría el actual y es el que gobierna los "
 "esquemas de certificación, en un momento en el que el censo europeo de organismos notificados del Reglamento "
 "de Ciberresiliencia estaba a cero. Y la simplificación de la notificación de incidentes no va por la reforma "
 "de NIS2, va por el <b>Digital Omnibus</b>, cuyo mandato de negociación del Consejo se adoptó el 21 de octubre "
 "de 2026.",
 'El <a href="https://commission.europa.eu/publications/2027-commission-work-programme-and-annexes_en" @L>'
 'programa de trabajo de la Comisión para 2027 y sus anexos</a>, con el anexo II leído entrada por entrada.',
 "La propuesta ausente existe y está localizada, lo que hace la lectura sólida y no un error de referencia: la "
 "COM(2026) 13 lleva por título «propuesta de Directiva que modifica la Directiva (UE) 2022/2555 en lo relativo "
 "a medidas de simplificación y alineación con el nuevo Reglamento de Ciberseguridad», con fecha de documento "
 "de <b>20 de enero de 2026</b>, la misma que la propuesta que sí está priorizada. Dato de contexto del propio "
 "programa, útil para situar los expedientes españoles: en 2026 la Comisión abrió <b>874 procedimientos de "
 "infracción, el máximo en diez años</b>, remitió 61 asuntos al Tribunal, pidió sanciones económicas en 25 y "
 "archivó 499 por cumplimiento."),

("eu", "Recomendación (UE) 2026/2394, publicada en el DOUE el 6 de noviembre de 2026", True,
 "La Comisión publica las cláusulas contractuales tipo de nube del Reglamento de Datos, y el anexo de seguridad "
 "y continuidad se solapa con el artículo 30 de DORA y con el 21.2.d) de NIS2",
 "Adoptada el <b>29 de octubre</b> y <b>publicada en el Diario Oficial serie L el 6 de noviembre de 2026</b>, "
 "dentro de la ventana, al amparo del <b>artículo 41 del Reglamento (UE) 2023/2854</b>, el Reglamento de Datos. "
 "El título oficial dice <b>no vinculantes</b> dos veces, y conviene no perderlo. Doce anexos: el I es la "
 "introducción general; los <b>II a V</b> son cláusulas contractuales tipo de acceso y uso de datos, con los "
 "cuatro supuestos de titular frente a usuario, usuario frente a destinatario, titular frente a destinatario a "
 "petición del usuario e intercambio voluntario; y los <b>VI a XII</b> son cláusulas contractuales estándar "
 "para contratos de computación en nube, en este orden: <b>VI cambio y salida, VII terminación, VIII seguridad "
 "y continuidad de las actividades</b>, IX no dispersión documental, X responsabilidad, XI no modificación "
 "unilateral y XII definiciones. La parte dispositiva recomienda su uso y, en su punto 3, que <b>los Estados "
 "fomenten su uso en particular por medio de los órganos de resolución de litigios designados y de las "
 "autoridades competentes</b> del propio Reglamento de Datos.",
 "Porque es el entregable contractual más utilizable del año y porque es el patrón frente al que un órgano de "
 "resolución de litigios va a medir el contrato de un cliente. Los anexos <b>VIII, de seguridad y continuidad, "
 "y VI, de cambio y salida</b>, se solapan materialmente con el <b>artículo 30 de DORA</b> sobre cláusulas "
 "obligatorias con proveedores de TIC y con el <b>artículo 21.2.d) de NIS2</b> sobre seguridad de la cadena de "
 "suministro. Dicho de otro modo: por primera vez hay un texto de referencia de la Comisión para negociar "
 "salida, continuidad y responsabilidad con un hiperescalar, que es exactamente donde los clientes pierden las "
 "negociaciones. El ejercicio inmediato para quien tenga contratos de nube vivos es medir la brecha entre su "
 "contrato actual y los anexos VI a XII, y llevar esa brecha al comité con un texto europeo detrás en lugar de "
 "con una opinión. Y hay que decir con la misma claridad que <b>no son vinculantes</b> y son adaptables: quien "
 "las presente como obligatorias perderá credibilidad en la primera reunión.",
 'La <a href="https://eur-lex.europa.eu/eli/reco/2026/2394/oj" @L>Recomendación (UE) 2026/2394</a>, Diario '
 'Oficial serie L de 6 de noviembre de 2026, con sus doce anexos.',
 "Dos precisiones de cita, por si alguien va al texto. La primera es una <b>errata del propio Diario "
 "Oficial</b>, y aparece <b>dos veces</b>, no una: el primer párrafo del anexo VIII y un párrafo del anexo IX "
 "remiten al «Reglamento (UE) 2023/285» en lugar de al 2023/2854, en las dos versiones idiomáticas "
 "comprobadas. Es errata del texto publicado, no un acto distinto, y el número correcto aparece bien "
 "cuarenta y tres veces en cada versión. La segunda: la parte dispositiva remite a «los anexos I a V» y a «los "
 "anexos I y VI a XII», incluyendo el anexo I en las dos remisiones, de modo que si se cita la parte "
 "dispositiva hay que citarla así y no como II a V y VI a XII."),

("eu", "ENISA · 4 de noviembre de 2026", False,
 "ENISA publica su criterio técnico sobre mecanismos de actualización segura, dirigido a fabricantes del "
 "Reglamento de Ciberresiliencia, y es el contrapunto exacto del caso de la refrigeración",
 "Aviso técnico de ENISA sobre <b>mecanismos de actualización segura</b>, orientado a los equipos que diseñan, "
 "implantan u operan la entrega de actualizaciones en productos con elementos digitales, con el foco declarado "
 "en fabricantes micro, pequeños y medianos, aunque el propio documento dice que sirve a organizaciones "
 "mayores. Da el criterio de la agencia sobre un requisito del <b>anexo I del Reglamento de "
 "Ciberresiliencia</b>, cuyas obligaciones principales se aplican desde el 11 de diciembre de 2027.",
 "Porque es el documento con el que se mide a un proveedor de equipo, y llega la misma semana en la que la "
 "campaña del frío demuestra para qué sirve. El problema de fondo de esa campaña no es un fallo exótico, es "
 "<b>equipo en fin de vida sin ruta de actualización</b>: un supervisor que el fabricante declaró en fin de "
 "servicio y cuya única remediación es migrar, y otro retirado del mercado en 2016 para el que nunca hubo "
 "aviso. Un cliente que compre equipo con software dentro tiene aquí la lista de preguntas de "
 "aprovisionamiento: cómo se firma la actualización, cómo se verifica, cuánto tiempo se compromete el soporte y "
 "qué pasa cuando se acaba. Y para un consultor es la pieza que convierte el artículo 21.3 de NIS2, el de la "
 "calidad general de los productos del proveedor, en una cláusula que se puede escribir.",
 'El <a href="https://www.enisa.europa.eu/publications/enisa-technical-advisory-on-secure-update-mechanisms" '
 '@L>aviso técnico de ENISA sobre mecanismos de actualización segura</a>, de 4 de noviembre de 2026.',
 "Trampa de fecha detectada y evitada en la propia fuente, y conviene registrarla: en el listado de "
 "publicaciones de ENISA <b>las fechas de este aviso y del aviso sobre inventarios de software están "
 "cruzadas</b>, la página de uno lleva el marcador temporal del otro. La fuente buena es el campo de fecha de "
 "publicación del cuerpo, y además cada página confirma la fecha de la otra en su bloque de contenido "
 "relacionado. Resultado correcto: <b>actualizaciones seguras el 4 de noviembre, inventarios de software el 22 "
 "de octubre</b>, el segundo fuera de ventana. La regla que ha funcionado tres veces esta semana en tres sitios "
 "distintos: <b>la fecha del listado no es la fecha del documento</b>."),

("eu", "Recomendación (UE) 2026/5593, publicada en el DOUE el 6 de noviembre de 2026", False,
 "La Comisión pide a los Estados planes de continuidad y pruebas de resistencia de sus puntos de contacto de "
 "protección civil, y cita el apagón ibérico como caso",
 "Adoptada el 29 de octubre y publicada en el Diario Oficial serie C el <b>6 de noviembre de 2026</b>, al "
 "amparo del artículo 7 de la Decisión 1313/2013. Recomienda, sin vincular, <b>planes de continuidad operativa "
 "y pruebas periódicas</b> de los puntos de contacto nacionales que deben estar disponibles de forma permanente "
 "ante el centro europeo de coordinación de respuesta a emergencias. Sus considerandos invocan expresamente "
 "<b>la gran perturbación informática de 2024</b>, una tormenta en Irlanda en enero de 2025 y <b>el apagón de "
 "la península ibérica de 2025</b>, y ejecuta la acción 51 de la Estrategia de la Unión de Preparación. Se "
 "presentó el 3 de noviembre en el Foro Europeo de Protección Civil, junto a las directrices de preparación de "
 "la población, con la autosuficiencia de 72 horas, y al anuncio de un Día Europeo de la Preparación cada 23 de "
 "octubre desde 2027.",
 "No crea obligaciones empresariales, va dirigida a los Estados, y hay que decirlo para no sobrevenderla. "
 "Importa como argumento, y como argumento es bueno: <b>la Comisión está normalizando la prueba de resistencia "
 "de la continuidad y cita el apagón ibérico por su nombre</b> en un acto publicado en el Diario Oficial. Es el "
 "marco en el que encajan las pruebas de continuidad que la Directiva de entidades críticas exige a las "
 "entidades críticas y las pruebas de resiliencia operativa digital de DORA, y da cobertura política para pedir "
 "presupuesto de ejercicios a un consejo que vivió el apagón. Para un cliente español es el mejor gancho "
 "disponible este trimestre para convertir un ejercicio de mesa en una línea presupuestaria.",
 'La <a href="https://eur-lex.europa.eu/eli/reco/2026/5593/oj" @L>Recomendación (UE) 2026/5593</a>, Diario '
 'Oficial serie C de 6 de noviembre de 2026.',
 "Es una recomendación, no un reglamento, y no obliga a ninguna empresa a nada: cualquiera que la venda como "
 "obligación nueva se equivoca. Lo que sí es verificable y utilizable es la cita del apagón en los "
 "considerandos de un acto de la Comisión, porque eleva una anécdota nacional a precedente europeo."),

("eu", "Medidas nacionales de transposición · a 8 de noviembre de 2026", False,
 "Cero notificaciones nuevas de NIS2 y de entidades críticas en la ventana, y España sigue siendo el único "
 "Estado con cero en las dos directivas a la vez",
 "Barrido del repositorio europeo con los predicados correctos y con prueba de control superada. Entre el 2 y "
 "el 8 de noviembre de 2026, <b>cero medidas notificadas</b> de NIS2 y de la Directiva de entidades críticas. "
 "La última notificación de <b>NIS2 es del 21 de octubre de 2026</b> y es húngara, un reglamento de su "
 "autoridad supervisora de actividades reguladas; la última de <b>entidades críticas es del 1 de octubre de "
 "2026</b> y son dos medidas danesas. Totales: <b>NIS2, 305 medidas de 25 Estados</b>, faltan <b>España e "
 "Irlanda</b>; <b>entidades críticas, 221 medidas de 24 Estados</b>, faltan <b>España, Bulgaria y Suecia</b>. "
 "La intersección da un solo Estado: <b>España es el único con cero medidas notificadas en las dos directivas a "
 "la vez</b>. Y un hallazgo colateral de la prueba de control que vale por sí mismo: la misma consulta sobre la "
 "primera Directiva de seguridad de las redes, la de 2016, devuelve 225 medidas de 28 Estados <b>e incluye a "
 "España con una</b>. España sí notificó bajo la norma anterior.",
 "Porque es el dato que sostiene toda la previsión de calendario y porque la prueba de control lo blinda. El "
 "cero español no es un artefacto de la consulta: la misma consulta encuentra la medida española de la norma de "
 "2016 y encuentra 305 y 221 medidas en las dos actuales. Y hay un patrón de palanca que conviene conocer antes "
 "de aconsejar: de los <b>seis Estados demandados por entidades críticas</b>, tres notificaron medidas "
 "<b>después</b> de que se interpusiera la demanda, Francia el 19 de julio, Países Bajos el 17 de julio y "
 "Polonia el 22 de junio de 2026. Lo mismo en NIS2: la Comisión decidió demandar el 7 de julio y Francia "
 "notificó el 19 y Países Bajos el 16 de julio. <b>La decisión de demandar funciona como palanca de "
 "cumplimiento, y España es el único Estado que no ha reaccionado ni en una ni en otra.</b> La inferencia de "
 "que esos tres asuntos acabarán archivándose o desistiéndose es nuestra y va sin confirmar.",
 'El repositorio de la Oficina de Publicaciones, consultado por su punto de acceso de datos enlazados, con el '
 'predicado de medidas nacionales de ejecución y la fecha de notificación. El aviso del asunto español está en '
 'el <a href="http://data.europa.eu/eli/C/2026/3986/oj" @L>Diario Oficial, serie C, C/2026/3986</a>.',
 "Tres avisos de método que conviene guardar, porque los tres producen ceros falsos. Uno: hay que usar el "
 "predicado de <b>fecha de notificación</b> y nunca el de fecha de documento, que no coincide y que en las dos "
 "medidas danesas devuelve enero de 2026 y diciembre de 2025, fechas del diario oficial danés y no de la "
 "notificación. Dos: la colección arrastra <b>medidas heredadas con fechas imposibles de 2004</b> para "
 "directivas de 2022, de modo que hay que usar el máximo y nunca el mínimo. Y tres, el más traicionero: un "
 "identificador escrito como literal llano devuelve <b>cero incluso para la directiva de control</b>; hay que "
 "filtrarlo como cadena. Y para <b>DORA, el Reglamento de IA y el Reglamento de Ciberresiliencia esta vía no "
 "sirve y hay que decirlo así</b>: son reglamentos y esa colección no los recoge como transposición, de modo "
 "que la ausencia de filas <b>no significa ausencia de medidas nacionales</b> de régimen sancionador o de "
 "designación de autoridades."),

("eu", "Censo europeo del Reglamento de Ciberresiliencia", False,
 "A treinta y dos días del hito del 11 de diciembre, el recuento de organismos notificados no se ha podido "
 "reverificar, y se dice así",
 "El <b>artículo 35.2 del Reglamento (UE) 2024/2847</b> fija el 11 de diciembre de 2026 como fecha en la que "
 "los Estados «se esforzarán por garantizar» un número suficiente de organismos notificados. Lo último "
 "verificado, el 26 de octubre de 2026, era: <b>catorce Estados con autoridad notificante</b>, Finlandia "
 "completa, <b>España sin ninguna por ausencia verificada</b>, once sin dato público y <b>cero organismos "
 "notificados en toda la Unión</b>. Esta semana <b>ese recuento no se ha reverificado</b>. El motivo es "
 "concreto y no es que el método falle: el buscador del censo europeo exige una clave de interfaz de "
 "programación que la propia aplicación pública incrusta en el navegador, y usarla desde aquí quedó bloqueada "
 "por la política de seguridad de este entorno. No se ha eludido y no se va a eludir. La interfaz pública es "
 "una aplicación de página única que no entrega la lista en el código servido, y las rutas antiguas de la base "
 "devuelven error o redirección.",
 "Porque este bloque existe para que un cliente no repita una cifra que no se ha comprobado. La diferencia "
 "entre «hay cero organismos notificados» y «la última vez que se pudo comprobar había cero y hace dos semanas "
 "que no se puede comprobar» es exactamente la diferencia entre un dato y una afirmación prestada. Lo que sí se "
 "mantiene verificado y es lo utilizable de este hito: obliga a <b>los Estados miembros y no a las "
 "empresas</b>, es obligación <b>de medios</b> y el umbral es <b>agregado en la Unión</b>, no un cupo por "
 "Estado. Quien lo venda a un fabricante como una obligación propia que vence el 11 de diciembre está "
 "sobrevendiendo. Y el dato que sí sostiene la conversación es el otro: los requisitos sustantivos llegan el "
 "<b>11 de diciembre de 2027</b>, y la obligación de notificación de los fabricantes ya está en vigor desde el "
 "11 de septiembre de 2026.",
 'El articulado del <a href="https://eur-lex.europa.eu/eli/reg/2024/2847/oj" @L>Reglamento (UE) 2024/2847</a>, '
 'artículos 14, 35.2, 69.3 y 71, que es la parte que sí se puede leer sin depender del censo.',
 "<b>No reconfirmado en fuente primaria esta semana.</b> El cero de organismos notificados del 26 de octubre "
 "<b>no está desmentido, está sin reverificar</b>, y se arrastra con su fecha. Queda como encargo expreso para "
 "David, porque es una decisión suya y no nuestra: o se autoriza expresamente a consultar el buscador público "
 "del censo con la clave que la propia aplicación de la Comisión sirve a cualquier navegador, o este dato se "
 "arrastra con fecha del 26 de octubre hasta que haya otra vía. No se ha encontrado una tercera."),
]

ITEMS += [

("fin", "EBA · 5 de noviembre de 2026", True,
 "La EBA mete la IA de frontera y las tecnologías cuánticas dentro del gobierno interno de la CRD, y la fecha "
 "de aplicación todavía está entre corchetes",
 "Informe final de las <b>Directrices revisadas de gobierno interno</b> bajo la Directiva de requisitos de "
 "capital, publicado el 5 de noviembre de 2026 y dictado al amparo de su artículo 74. El literal que lo "
 "convierte en noticia, leído en el párrafo 21 del informe: «el gobierno interno abarca también unas "
 "tecnologías de la información y la comunicación sólidas, <b>incluido el uso de IA de frontera y de "
 "tecnologías cuánticas</b>, la gestión del riesgo de terceros, incluidos los acuerdos de externalización, y la "
 "gestión de la continuidad de negocio». Y una nota general extiende el concepto: toda referencia a riesgos en "
 "las Directrices incluye «riesgos en el contexto del uso de inteligencia artificial y de tecnologías "
 "cuánticas». La articulación con DORA es explícita y citada por artículo: <b>5(2)(e)</b> y <b>11</b> para el "
 "marco de gestión del riesgo de TIC, <b>6(4)</b> para la función de control del riesgo de TIC en el esquema de "
 "tres líneas, <b>11(7)</b> para que la función de gestión de crisis de TIC pueda integrarse en el control "
 "interno, y el <b>artículo 48g de la CRD</b> junto con DORA para las <b>sucursales de terceros países</b>. "
 "Recoge además los cambios de la revisión de la Directiva: mapa de deberes y responsabilidades del órgano de "
 "administración y de los titulares de funciones clave, y marco de gobierno propio para sucursales de terceros "
 "países.",
 "Porque sube la inteligencia artificial de la capa técnica a la capa de gobierno, y eso cambia a quién se le "
 "pregunta. A partir de estas Directrices, el <b>consejo de administración de una entidad significativa "
 "española tiene expectativa supervisora explícita sobre IA de frontera y tecnologías cuánticas</b>, no el "
 "director de sistemas. Y llega con dos piezas que encajan como un guante: el Banco Central Europeo pidió en "
 "julio planes de acción frente a la ciberamenaza potenciada por IA con plazo el 31 de octubre, y anunció en la "
 "misma carta que tratará la criptografía poscuántica <b>en una carta separada</b> que todavía no ha llegado. "
 "Quien esté preparando la respuesta a esa carta tiene aquí el marco de gobierno en el que colgarla. Y afecta "
 "también a las <b>sucursales de terceros países establecidas en España</b>, que suelen quedarse fuera de este "
 "tipo de análisis.",
 'La <a href="https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-revised-guidelines-'
 'internal-governance-delivering-greater-proportionality-and" @L>nota de la EBA de 5 de noviembre de 2026</a> y '
 'el informe final, con los literales en los párrafos 21, 35, 105 y 238.',
 "<b>No hay fecha de aplicación, y hay que decirlo literalmente porque es inusual.</b> El informe final dice "
 "«estas directrices se aplican desde [dos meses después de la publicación en todas las lenguas oficiales de la "
 "Unión]», con los corchetes puestos, y la derogación de las Directrices de gobierno interno de 2021 figura "
 "como «xx/xx/xxxx». El estado declarado por la EBA es «final y pendiente de traducción». Consecuencia "
 "práctica: se puede empezar a trabajar con el contenido, pero <b>no se puede dar una fecha a un comité</b>, y "
 "cualquiera que la dé se la está inventando. Frente al texto de consulta se rebaja el detalle del mapa de "
 "deberes y de las declaraciones individuales y se simplifican conflictos de interés y seguimiento de "
 "diversidad."),

("fin", "BCE · plazo vencido el 31 de octubre de 2026", True,
 "Venció el plazo de los planes de acción frente a la ciberamenaza potenciada por IA y el supervisor no ha "
 "dicho nada formal, con tres compromisos propios pendientes",
 "La carta <b>SSM-2026-0301</b>, de 7 de julio de 2026, firmada por la presidenta del Consejo de Supervisión y "
 "dirigida al consejero delegado de cada entidad significativa, pedía un plan de acción frente a la "
 "ciberamenaza potenciada por IA «a remitir al respectivo equipo conjunto de supervisión <b>a más tardar el 31 "
 "de octubre de 2026</b>». Ese plazo venció hace nueve días. En toda la ventana, barridos los tres índices "
 "primarios del Mecanismo Único de Supervisión, <b>cero notas de prensa, cero publicaciones y ninguna carta "
 "nueva al sector</b>: la más reciente de 2026 sigue siendo la de julio. Hubo <b>tres discursos</b> del Consejo "
 "de Supervisión en la ventana, los días 3, 5 y 6 de noviembre, y los tres se han leído íntegros. <b>Una sola "
 "mención</b>, en el del 5 de noviembre en Helsinki, y está formulada en gerundio, como actividad en curso: el "
 "BCE ha venido fijando expectativas sobre externalización en la nube y «<b>pidiendo a los bancos que elaboren "
 "planes de acción para defenderse de las ciberamenazas potenciadas por IA</b>», con nota al pie a la carta de "
 "julio. <b>No dice que el plazo venciera, no da cifras de cumplimiento y no anuncia fecha del análisis "
 "horizontal.</b> El del 6 de noviembre convierte el argumento en tesis de estabilidad financiera, con el "
 "literal de que «los modelos de IA de frontera pueden también acortar el intervalo entre el descubrimiento de "
 "una vulnerabilidad y su explotación, dejando menos tiempo para responder», pero <b>no menciona los planes</b>.",
 "Porque el expediente sigue vivo y bilateral, en manos del equipo conjunto de supervisión, y porque el "
 "supervisor no ha abierto ninguna fase pública. Para una entidad significativa española eso significa dos "
 "cosas. Una, que la conversación de las próximas semanas no es con una guía publicada sino con su equipo "
 "conjunto, y que conviene tener el plan presentado y su trazabilidad ordenada. Dos, que hay <b>tres "
 "compromisos de la propia carta pendientes</b>, y conviene saber qué esperar: un <b>análisis horizontal de los "
 "planes remitidos</b> para identificar tendencias, retos y áreas de mejora, cuyas conclusiones el BCE promete "
 "compartir con las entidades significativas y que <b>todavía no se ha producido ni tiene fecha</b>; el "
 "aplazamiento de la recogida anual del <b>Cuestionario de Riesgo TI de septiembre de 2026 a febrero de "
 "2027</b>, que es un plazo real y próximo; y una <b>carta separada sobre el riesgo que la computación cuántica "
 "supone para los métodos de cifrado tradicionales</b>, que sigue sin publicarse. Ese último encaja "
 "directamente con las Directrices de la EBA de esta misma semana.",
 'La carta <a href="https://www.bankingsupervision.europa.eu/press/letterstobanks/shared/pdf/2026/ssm.2026_'
 'letter_on_AI_enabled_cybersecurity_threats.en.pdf" @L>SSM-2026-0301, de 7 de julio de 2026</a>, con el plazo '
 'y los tres compromisos leídos en su texto, y el <a href="https://www.bankingsupervision.europa.eu/press/'
 'speeches/date/2026/html/ssm.sp261105~717ce34d36.en.html" @L>discurso de 5 de noviembre de 2026</a>, que es la '
 'única mención de la ventana.',
 "La base macroprudencial del expediente conviene citarla con precisión, porque es fácil pasarse: el aviso de "
 "la Junta Europea de Riesgo Sistémico <b>ESRB/2026/3, de 25 de junio de 2026</b>, sobre riesgos cíber "
 "sistémicos derivados de los modelos de IA de frontera, publicado en el Diario Oficial el 16 de julio, <b>no "
 "impone plazos propios</b>: su única fecha operativa es la referencia al 31 de octubre del BCE, en su "
 "considerando 13, y allí se describe expresamente como iniciativa del BCE en su papel de supervisor bancario, "
 "<b>no como obligación para todo el sector financiero</b>. Lo que sí promete la Junta es reevaluar la cuestión "
 "en cada valoración trimestral de riesgos de su Consejo General, cuya próxima reunión no tiene fecha "
 "publicada. Y las prioridades supervisoras vigentes siguen siendo las de 2026 a 2028: <b>las de 2027 a 2029 no "
 "se han publicado ni anunciado</b>."),

("fin", "EBA · 6 de noviembre de 2026", False,
 "La EBA aplaza el nuevo marco de reporte supervisor y simplifica justo el canal por el que las pérdidas por "
 "incidentes llegan al supervisor",
 "Anuncio de los próximos pasos en simplificación del reporte supervisor, con fechas propias: informe final del "
 "paquete de normas técnicas de ejecución <b>en diciembre de 2026</b>; <b>primera fecha de referencia de los "
 "nuevos requisitos aplazada a diciembre de 2027</b>; liquidez, cargas de activos, benchmarking supervisor y "
 "reporte de sostenibilidad <b>diferidos a diciembre de 2028</b>; y <b>reporte granular de pérdidas por riesgo "
 "operacional simplificado</b>, con menos campos e instrucciones más claras. Añade un módulo específico de "
 "pruebas de resistencia con plazos y frecuencias separados, directrices sobre diseño de peticiones de datos "
 "antes de final de 2026, un <b>repositorio público de peticiones de datos</b> operativo en el primer trimestre "
 "de 2027, propuestas de gestión del cambio en el primer semestre de 2027 y un periodo mínimo de implantación "
 "de un año. Y los miembros de su Consejo de Supervisores se comprometen a <b>reducir las peticiones nacionales "
 "solapadas</b> cuando la información equivalente ya se recoge por el marco de la EBA.",
 "Porque el reporte granular de pérdidas por riesgo operacional es <b>el canal por el que las pérdidas por "
 "incidentes de TIC y cíber llegan al supervisor</b>, y se simplifica y se retrasa a la vez. Para un cliente "
 "bancario eso tiene una lectura inmediata y otra de fondo. La inmediata: hay más margen de calendario del que "
 "se había planificado, y conviene reasignarlo en lugar de celebrarlo. La de fondo: menos campos significa "
 "menos granularidad en la serie histórica de pérdidas, y esa serie es precisamente la que sostiene cualquier "
 "cuantificación de riesgo cíber en euros ante un consejo. Si el supervisor pide menos detalle, el detalle hay "
 "que seguir guardándolo igual, pero por interés propio y no por obligación, y eso es una conversación que "
 "conviene tener antes de que alguien decida simplificar también el modelo interno. El compromiso sobre "
 "peticiones nacionales solapadas acota además lo que el Banco de España puede pedir en paralelo, y es un "
 "argumento utilizable.",
 'La <a href="https://www.eba.europa.eu/publications-and-media/press-releases/eba-outlines-next-steps-'
 'supervisory-reporting-simplification-and-extends-implementation-timelines" @L>nota de la EBA de 6 de '
 'noviembre de 2026</a>, con las cinco fechas en su propio texto.',
 "La EBA etiqueta esta pieza como <b>elemento de noticias y no como nota de prensa</b>, al contrario que la del "
 "día anterior. Es un matiz de peso institucional y conviene escribir «anunció» y no «publicó una nota de "
 "prensa». En la misma ventana se cerró además la consulta EBA/CP/2026/16, sobre el reporte para la validación "
 "y el seguimiento del modelo estándar inicial del sector de derivados, abierta el 5 de agosto y <b>cerrada el "
 "2 de noviembre</b>, primer día de la ventana. No es de DORA."),

("fin", "DORA · vigilancia de proveedores terceros críticos", False,
 "La lista anual de proveedores críticos de TIC sigue siendo la de noviembre de 2025, con la actualización ya "
 "en calendario y sin publicar",
 "El <b>artículo 31(9) del Reglamento (UE) 2022/2554</b> obliga a las autoridades europeas de supervisión, a "
 "través de su Comité Mixto, a establecer, publicar y <b>actualizar anualmente</b> la lista de proveedores "
 "terceros críticos de TIC a escala de la Unión. La lista que hoy sirven las autoridades es la de <b>noviembre "
 "de 2025</b>, con <b>19 proveedores</b>, y está alojada en la carpeta de esa fecha. Verificado en dos de las "
 "tres autoridades: la nota de designación de la segunda está fechada el 18 de noviembre de 2025 y su único "
 "documento asociado es esa misma lista. <b>No hay designaciones nuevas, ni retiradas, ni nombramientos nuevos "
 "de equipos conjuntos de examen publicados</b>, ni en la ventana ni después. Las cuatro piezas de nivel dos "
 "del marco de vigilancia siguen vigentes y sin cambios, incluida la tasa fija de 50.000 euros para la "
 "adhesión voluntaria, y la composición del Foro de Vigilancia no se ha tocado desde el 16 de junio de 2026.",
 "Porque el registro de información y las cláusulas contractuales de una entidad española se apoyan en ese "
 "perímetro, y una segunda tanda de designaciones movería obligaciones contractuales y de salida de golpe. "
 "Mientras no llegue, la pregunta útil para un cliente no es quién está en la lista, es <b>quién debería estar "
 "y no está</b>: un proveedor que concentre servicio crítico de varias entidades financieras y que no figure "
 "designado no está fuera del riesgo, está fuera de la vigilancia directa, y por tanto toda la carga de control "
 "recae en el contrato y en el registro de información de la entidad. Conviene revisar ahora las cláusulas de "
 "salida de los proveedores candidatos, antes de que la designación llegue y el proveedor tenga menos incentivo "
 "para negociar.",
 'La <a href="https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-'
 'resilience-act/dora-oversight" @L>página de vigilancia DORA de la EBA</a>, que es la que sigue sirviendo la '
 'lista de noviembre de 2025.',
 "Corrección de cita que conviene no heredar, porque dice justo lo contrario de lo que se quiere decir: la "
 "obligación de publicar y actualizar anualmente es del <b>artículo 31(9)</b>, no del 31(8). El apartado 8 es "
 "la <b>lista de exclusiones</b> de la designación: entidades financieras que prestan servicios de TIC a otras, "
 "proveedores sujetos a los marcos del artículo 127(2) del Tratado, proveedores intragrupo y proveedores que "
 "operan en un solo Estado miembro. Y el incumplimiento de la periodicidad anual, una vez corregida la cita, es "
 "un hallazgo legítimo: la lista cumple un año la semana que viene."),
]

ITEMS += [

("std", "ISO/IEC JTC 1/SC 42 · 5 y 6 de noviembre de 2026", True,
 "El comité de inteligencia artificial abre cuatro proyectos en tres días y manda a revisión el informe de "
 "confiabilidad que media industria cita en sus memorias",
 "Leídas ficha a ficha las 100 entradas del catálogo del comité. Movimientos con fecha en la ventana. El <b>5 "
 "de noviembre</b>, el <b>ISO/IEC TR 24028:2020</b> pasa a etapa <b>90.92, norma internacional a revisar</b>, y "
 "el mismo día se aprueba y se registra su sucesor, el <b>ISO/IEC AWI TR 24028</b>, segunda edición, "
 "«Características de confiabilidad de los sistemas de IA». El <b>6 de noviembre</b>, tres informes técnicos "
 "nuevos aprobados y registrados el mismo día: <b>ISO/IEC AWI TR 27258</b>, sobre interacciones en sistemas de "
 "IA multiagente; <b>ISO/IEC AWI TR 27259</b>, taxonomía de patrones de uso indebido en aplicaciones de IA; y "
 "<b>ISO/IEC AWI TR 27260</b>, panorama de normalización de la IA física. El <b>7 de noviembre</b>, las dos "
 "partes del ISO/IEC CD TS 22440, de seguridad funcional y sistemas de IA, se <b>devuelven al grupo de "
 "trabajo</b> y se reabren como proyecto. Y el <b>5 de noviembre</b> se <b>borra del programa</b> la enmienda 2 "
 "de la ISO/IEC 23053, la de terminología de aprendizaje automático, mientras la enmienda 1 sigue viva.",
 "Por el primero, que es el que afecta a documentos que ya están firmados. El <b>informe técnico 24028</b> es "
 "la referencia de confiabilidad que se usa como apoyo interpretativo en implantaciones de la <b>ISO/IEC "
 "42001</b> y en expedientes de gestión de riesgos de IA. Pasar a 90.92 significa que <b>el texto que se está "
 "citando hoy va a cambiar</b>, y la consecuencia práctica es concreta: no conviene anclar una declaración de "
 "aplicabilidad ni un informe de auditoría a su redacción actual, y conviene revisar los que ya lo hacen. El "
 "segundo que merece atención es el <b>27259</b>, la taxonomía de patrones de uso indebido: tiene toda la pinta "
 "de acabar convertido en controles de IA que se auditen en 2028, y leerlo ahora es la forma más barata de "
 "anticiparlos. Y hay un dato de arquitectura que conviene registrar: <b>la serie 272xx aparece por primera vez "
 "asignada al comité de inteligencia artificial</b> y no al de seguridad de la información, lo que dice algo "
 "sobre dónde se va a normalizar la seguridad de la IA.",
 'Las fichas de <a href="https://committee.iso.org/standard/77608.html" @L>ISO/IEC TR 24028:2020</a>, de su '
 '<a href="https://committee.iso.org/standard/95686.html" @L>sucesor</a> y de los tres informes técnicos '
 'nuevos, en el espejo del catálogo por comité, con el ciclo de vida abierto en cada una.',
 "Aviso de método que casi produce un dato falso y conviene dejar escrito: iso.org devuelve error a cualquier "
 "acceso automatizado, pero el espejo del catálogo por comité sirve la misma ficha con el ciclo de vida "
 "completo. Y el canal de novedades por comité <b>no funciona como canal</b>: devuelve el catálogo en código de "
 "página con las etapas actuales pero <b>sin fechas</b>, de modo que la única vía con fechas es abrir el bloque "
 "de ciclo de vida de cada ficha, una por una. El aviso heredado sobre enlaces de normas muy vendidas que "
 "devolvían una ficha ajena <b>no se ha podido reproducir esta semana</b>: hoy sirven la ficha correcta."),

("std", "ISO/IEC 27028 · corrección de arrastre", False,
 "La guía sobre los atributos de los controles sigue sin publicarse, pero ahora la ISO anuncia noviembre, y eso "
 "es lo nuevo",
 "Recomprobado abriendo la ficha y leyendo el bloque de ciclo de vida íntegro. La <b>ISO/IEC 27028</b>, guía "
 "sobre el uso de los atributos de los controles de seguridad de la información, sigue en estado «en "
 "desarrollo» y en etapa <b>60.00, norma internacional en producción, desde el 20 de octubre de 2026</b>, y la "
 "línea «60.60, norma internacional publicada» <b>sigue sin fecha</b>. El dato nuevo respecto del arrastre es "
 "que la ficha muestra ahora <b>fecha de publicación 2026-11</b> y su cabecera dice «en producción, primera "
 "edición de 2026, pasos finales de producción, hasta siete semanas». Es decir: <b>la ISO anuncia publicación "
 "en noviembre de 2026, pero a 9 de noviembre no se ha materializado</b>.",
 "Porque es la tercera edición consecutiva en la que hay que corregir lo mismo, y porque la distinción importa "
 "para quien esté planificando una revisión del sistema de gestión. Los atributos de los controles del anexo A "
 "de la 27002 son la herramienta con la que se construyen vistas de controles por tipo, por propiedad de "
 "seguridad o por capacidad operativa, y la guía es lo que va a fijar cómo se usan de forma consistente entre "
 "auditor y auditado. Mientras esté en 60.00, <b>cualquier metodología propia de atributos es legítima pero no "
 "tiene respaldo normativo</b>, y conviene no prometerlo. La etapa 60.00 suele resolverse en semanas, así que "
 "es razonable esperarla entre noviembre y enero, pero la ISO no publica fecha comprometida y <b>no debe darse "
 "por hecha</b>.",
 'La <a href="https://committee.iso.org/standard/61007.html" @L>ficha de la ISO/IEC 27028</a>, con el ciclo de '
 'vida completo y la línea 60.60 vacía.',
 "<b>Corrección a este boletín, edición 010</b>, que se publicó diciendo que la norma estaba publicada, "
 "corregida ya en la 011 y que se mantiene aquí por tercera semana porque la ficha no se ha movido. Si vuelve a "
 "aparecer como publicada, es que se copió de un titular de portada y no de la ficha. Ciclo de vida reciente, "
 "por si hace falta: 40.99 y 50.00 el 11 de junio de 2026, 50.20 el 24 de agosto, 50.60 y 60.00 el 20 de "
 "octubre, y 60.60 sin fecha."),

("std", "NIST · 2 y 4 de noviembre de 2026", False,
 "El NIST deroga de un golpe su referencia de diez años para pequeña empresa y publica el primer documento que "
 "trata la gestión de incidentes de IA de frontera como categoría propia",
 "Tres publicaciones con fecha en la ventana, sobre un catálogo de 1.744 registros de los que se han revisado "
 "los cien más recientes. El <b>2 de noviembre de 2026</b>, el <b>CSWP 50</b>, «Ciberseguridad para pequeña "
 "empresa: empresas sin empleados», que <b>deroga íntegramente el IR 7621 revisión 1</b>, de noviembre de 2016, "
 "que llevaba diez años siendo la referencia del NIST para pequeña empresa. El mismo <b>2 de noviembre</b>, el "
 "<b>IR 8621</b>, conclusiones del taller de gestión de incidentes de superinteligencia celebrado el 14 de mayo "
 "de 2026 con más de cuatrocientos expertos, que cubre tanto ataques dirigidos a esos sistemas como daños por "
 "uso indebido, fallo o acciones no intencionadas. Y el <b>4 de noviembre</b>, la llamada previa a comentarios "
 "del <b>SP 800-108 revisión 2</b>, de derivación de claves con funciones pseudoaleatorias, con plazo el 18 de "
 "diciembre de 2026. Sin cambios en el marco de ciberseguridad, en el SP 800-53, en el SP 800-171, en el marco "
 "de gestión de riesgos de IA ni en los FIPS 203, 204 y 205.",
 "Por la derogación, que es la que puede dejar a alguien citando un documento muerto. <b>Si un cliente, un "
 "material de formación o un pliego cita el IR 7621 revisión 1, está citando un documento derogado desde el 2 "
 "de noviembre</b>, y conviene revisarlo esta semana porque es una referencia muy extendida en guías de pequeña "
 "y mediana empresa en español. El informe de incidentes de superinteligencia es útil por otra razón: es el "
 "primer documento del NIST que trata la gestión de incidentes de IA de frontera como categoría propia, y sirve "
 "de apoyo externo para quien esté respondiendo a la carta del Banco Central Europeo sobre ciberamenaza "
 "potenciada por IA. Y la revisión de la derivación de claves importa a cualquiera con criptografía en el "
 "alcance de una certificación o en plan de migración poscuántica, porque es una de las piezas que se reescribe "
 "aguas abajo de los nuevos estándares.",
 'Las fichas del <a href="https://csrc.nist.gov/pubs/cswp/50/small-business-cybersecurity-non-employer-firms/'
 'final" @L>CSWP 50</a>, del <a href="https://csrc.nist.gov/pubs/ir/8621/final" @L>IR 8621</a> y de la '
 '<a href="https://csrc.nist.gov/pubs/sp/800/108/r2/iprd" @L>llamada previa a comentarios del SP 800-108 Rev. '
 '2</a>.',
 "Precisión de datación que conviene conocer para no equivocarse al citar: para los dos primeros, <b>el campo "
 "de fecha de publicación de la ficha solo dice «noviembre de 2026»</b>, sin día. El día sale del historial del "
 "documento de la propia ficha y, en el caso del derogado, de la nota de retirada del IR 7621 revisión 1, que "
 "dice «retirado el 2 de noviembre de 2026, sustituido por el CSWP 50». Para el tercero, el día sí está "
 "explícito. Y una trampa de dirección: la ruta corta de la ficha del CSWP 50 devuelve error, hay que usar la "
 "completa con el nombre del documento."),

("std", "CEN y CENELEC · 6 de noviembre de 2026", False,
 "Aparece un tipo de norma europea nueva, iterativa y de ciclo corto, y en ciberseguridad y en IA es donde van "
 "a salir las primeras",
 "CEN y CENELEC anunciaron que la <b>Especificación Ágil Europea</b> pasa a ser <b>parte permanente de su "
 "catálogo de entregables a partir del 1 de enero de 2027</b>. Es una vía rápida para áreas donde la "
 "tecnología, el mercado o la regulación se mueven más rápido que el ciclo normal: se publica el contenido ya "
 "maduro y se desarrolla por iteraciones sucesivas, en lugar de esperar al texto completo. Los pilotos salieron "
 "en menos de un año. Seguirá los principios de redacción de los reglamentos internos de los dos organismos, "
 "con un proceso simplificado, y la nota lo enmarca expresamente en la propuesta de nuevo Reglamento de "
 "Normalización de la Comisión. En la misma ventana <b>no hubo ningún movimiento de etapa en el comité europeo "
 "de inteligencia artificial</b>, cuyo último movimiento real sigue siendo del 29 de octubre de 2026, y su "
 "última norma publicada es del 5 de agosto.",
 "Por una consecuencia contractual que se ve poco y que llega pronto. Si aparece un entregable europeo que "
 "cambia de versión por iteraciones, <b>las cláusulas que fijan «la versión vigente» de una norma dejan de ser "
 "neutrales</b>: pueden obligar a un proveedor a seguir un texto que cambie dentro del propio ciclo del "
 "contrato. Y para un auditor significa referencias normativas que se mueven dentro del ciclo de "
 "certificación, con el problema práctico de decidir contra qué versión se audita. En ciberseguridad y en IA, "
 "donde la demanda regulatoria va muy por delante del catálogo, es previsible que las primeras especificaciones "
 "ágiles salgan justo en estos ámbitos, y conviene empezar a redactar las cláusulas de versión con eso en "
 "mente.",
 'La <a href="https://www.cencenelec.eu/news-events/news/2026/brief-news/2026-11-06-eas/" @L>nota de CEN y '
 'CENELEC de 6 de noviembre de 2026</a> sobre la Especificación Ágil Europea.',
 "Laguna declarada del lado español: <b>une.org devuelve error a cualquier acceso automatizado</b> en las tres "
 "rutas probadas, de modo que no se puede afirmar nada sobre el catálogo de UNE ni sobre sus comités técnicos. "
 "Mitigado por la vía que sí es concluyente para lo que importa: barridas las siete ediciones del BOE de la "
 "ventana, <b>cero resoluciones de publicación o anulación de normas UNE</b>. Y no se ha podido obtener el "
 "listado de encuestas públicas abiertas de CEN y CENELEC con sus fechas de cierre, porque su portal carga el "
 "informe por guion: las fechas del comité de IA que se dan en la tabla de plazos son <b>etapas previstas del "
 "programa de trabajo, no cierres de encuesta confirmados</b>, y así se marcan."),
]

ITEMS += [

("ai", "Reglamento de IA · 2 de diciembre de 2026", True,
 "El 2 de diciembre vencen dos obligaciones nuevas, y la segunda da tres semanas y media a cualquiera que "
 "tuviera un asistente generativo en producción antes de agosto",
 "Verificado en el texto consolidado del Reglamento (UE) 2024/1689 a 27 de julio de 2026, comparado con el "
 "original y con el acto modificativo. Ese día vencen <b>dos cosas distintas, y ninguna existía en el texto de "
 "2024</b>. La primera: se aplican el <b>artículo 5.1, párrafo primero, letras ba) y bb)</b>, y los apartados "
 "<b>5.1 bis y 5.1 ter</b>, por la letra a) del párrafo tercero del artículo 113 en su versión sustituida. La "
 "letra ba) prohíbe los sistemas que generen o manipulen imágenes, vídeo o audio realistas de las partes "
 "íntimas de una persona identificable o de una persona identificable en actividades sexualmente explícitas "
 "<b>sin su consentimiento libre, específico, informado, inequívoco y explícito</b>; la bb) hace lo mismo "
 "respecto del material de abuso sexual infantil de la Directiva 2011/93. Y los dos apartados nuevos son los "
 "que deciden si un sistema cae dentro: la introducción en el mercado solo está prohibida si esa generación es "
 "<b>la finalidad prevista</b> del sistema, <b>o</b> si su diseño, entrenamiento, arquitectura, capacidades o "
 "funcionalidades expuestas al usuario hacen de ese resultado algo <b>razonablemente previsible y reproducible "
 "sin modificación técnica significativa</b> y el sistema <b>no tiene medidas técnicas de seguridad razonables "
 "y adecuadas para impedirlo de forma fiable</b>. La segunda obligación es el <b>artículo 111.4, nuevo</b>: los "
 "proveedores de sistemas que generan contenido sintético de audio, imagen, vídeo o texto, <b>incluidos los de "
 "uso general, introducidos en el mercado antes del 2 de agosto de 2026</b>, deben cumplir el <b>artículo "
 "50.2</b> para esa fecha, es decir marcar las salidas <b>en formato legible por máquina y detectables como "
 "generadas o manipuladas artificialmente</b>, con soluciones eficaces, interoperables, robustas y fiables en "
 "la medida de lo técnicamente viable.",
 "Porque la primera alcanza a mucho más de lo que parece y la segunda es el plazo corto de verdad. La "
 "prohibición <b>no es solo para fabricantes de aplicaciones de nudificación</b>: alcanza a cualquier proveedor "
 "de IA generativa de imagen o de vídeo cuyo sistema permita ese resultado de forma razonablemente previsible y "
 "reproducible sin modificación técnica significativa y que no tenga salvaguardas fiables. Lo que hay que poder "
 "documentar antes del 2 de diciembre es concreto: filtros de entrada y de salida, medidas que impidan de forma "
 "fiable el resultado, y capacidad de corregir el uso indebido observado o notificado. Para el <b>responsable "
 "del despliegue el umbral es distinto y más benigno</b>: solo infringe si usa el sistema con esa finalidad. Y "
 "el artículo 111.4 es el que va a pillar a gente: cualquier cliente que tuviera un asistente generativo en "
 "producción antes de agosto tiene <b>tres semanas y media</b> para acreditar marcado legible por máquina. La "
 "vía de demostración reconocida a escala europea es el código de buenas prácticas sobre transparencia de los "
 "contenidos generados por IA, y quien no lo firme tendrá que demostrar que sus medidas son adecuadas, evaluado "
 "individualmente por cada autoridad de vigilancia del mercado.",
 'El <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%%3A02024R1689-20260727" @L>texto '
 'consolidado del Reglamento de IA a 27 de julio de 2026</a>, artículos 5, 50.2, 111.4 y 113, y el '
 '<a href="https://eur-lex.europa.eu/eli/reg/2026/1744/oj" @L>Reglamento (UE) 2026/1744</a> que lo modificó.',
 "Discrepancia con la propia Comisión que conviene no heredar: su página del marco regulatorio dice que el "
 "Reglamento prohíbe <b>nueve prácticas</b> y que la novena entra en vigor en diciembre de 2026, contando las "
 "dos letras como una sola práctica y <b>sin mencionar los apartados 1 bis y 1 ter</b>, que son los que "
 "delimitan el alcance. El articulado añade <b>dos letras y dos párrafos</b>. Y el apartado 5.1 ter excluye del "
 "concepto de manipulación la que no incrementa la exposición de partes íntimas ni altera la naturaleza de las "
 "actividades representadas, que es un matiz con consecuencias para herramientas de edición."),

("ai", "Reglamento de IA · corrección de calendario", True,
 "El alto riesgo del anexo III ya no es el 2 de agosto de 2026 sino el 2 de diciembre de 2027, y el 2 de "
 "febrero de 2027 no es ningún hito",
 "Dos correcciones de calendario verificadas con recuento literal sobre los tres textos completos, anexos "
 "incluidos. La primera: el <b>Reglamento (UE) 2026/1744</b>, de 8 de julio de 2026, publicado el 24 de julio y "
 "en vigor el 27 de julio, introdujo <b>43 modificaciones</b> al Reglamento de IA, y la letra c) sustituida del "
 "párrafo tercero del artículo 113 dice ahora que el capítulo III, secciones 1, 2 y 3, salvo el artículo 6.5, "
 "se aplica «<b>desde el 2 de diciembre de 2027</b> para los sistemas clasificados de alto riesgo conforme al "
 "artículo 6.2 y al anexo III» y «<b>desde el 2 de agosto de 2028</b> para los del artículo 6.1 y el anexo I». "
 "La letra original decía solo que el artículo 6.1 y sus obligaciones se aplicaban desde el 2 de agosto de 2027, "
 "y todo lo demás caía en la fecha general del 2 de agosto de 2026. La segunda corrección: <b>la cadena «2 de "
 "febrero de 2027» aparece cero veces</b> en el texto original, cero en el acto modificativo y cero en el "
 "consolidado, también en su versión española. Las fechas próximas que sí existen son tres: 2 de febrero de "
 "2025 para los capítulos I y II, <b>2 de febrero de 2026</b> para las directrices de la Comisión sobre "
 "clasificación de alto riesgo del artículo 6.5, que está <b>expresamente excluido</b> del aplazamiento, y 2 de "
 "diciembre de 2027.",
 "Porque hay planes de adecuación trabajando con fechas derogadas, y eso cuesta dinero en las dos "
 "direcciones. Quien construyó su plan de alto riesgo del anexo III sobre el 2 de agosto de 2026 tiene "
 "dieciséis meses más de los que creía, y quien asumió que el nuevo hito era agosto de 2027 tiene cuatro meses "
 "más: la fecha es <b>diciembre</b>. Lo que no cambia, y conviene decirlo para que nadie se relaje del todo, es "
 "la obligación del artículo 111.2 para el alto riesgo heredado destinado a autoridades públicas, con techo en "
 "el 2 de agosto de 2030. Y hay un detalle que se cuenta mal con frecuencia: <b>ese techo de 2030 ya estaba en "
 "el texto de 2024</b>; lo que la modificación cambió es el disparador, que ya no es una fecha fija sino la "
 "fecha de aplicación del capítulo III. Los areneros regulatorios nacionales también se movieron, del 2 de "
 "agosto de 2026 al 2 de agosto de 2027, de modo que quien esperase un arenero español este año ya tiene "
 "respuesta.",
 'El <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%%3A02024R1689-20260727" @L>consolidado '
 'a 27 de julio de 2026</a>, con los marcadores de consolidación visibles en el articulado, y los artículos '
 '113, 111, 57.1 y 6.5.',
 "<b>Corrección a este boletín</b> si el 2 de febrero de 2027 ha aparecido en alguna edición anterior: no "
 "existe como hito y hay que dejar de citarlo. Y una precisión sobre el inventario de fechas de 2027 en el "
 "consolidado, por si sirve de control: solo hay cuatro apariciones del 2 de agosto de 2027, una del 2 de "
 "diciembre de 2027, una del 2 de septiembre de 2027 y una del 1 de agosto de 2027. Ninguna otra."),

("ai", "AEPD y autoridad helénica · 5 de noviembre de 2026", False,
 "La AEPD publica con la autoridad griega la guía de entornos de tratamiento seguro, y el mensaje central es "
 "que las certificaciones por sí solas no bastan",
 "Guía conjunta de la <b>Agencia Española de Protección de Datos</b> y la autoridad helénica, con colaboración "
 "declarada de expertos de la oficina estadística europea, de la dirección general del dato del ministerio "
 "español, del Garante italiano y de la autoridad británica. Contiene una metodología de análisis de riesgos "
 "que <b>combina las diez categorías de amenazas de un marco de riesgos de datos con el marco de los cinco "
 "aspectos seguros</b>, un análisis de técnicas de ingeniería de protección de datos y un caso práctico de "
 "investigación sanitaria en seis fases. La tesis central, literal de la nota: la entidad que proporciona el "
 "entorno «<b>debe tener un control real y efectivo sobre la infraestructura y los tratamientos, incluso si la "
 "infraestructura la proporciona un tercero. Las garantías contractuales o las certificaciones, por sí solas, "
 "no bastan: deben respaldarse con medidas técnicas, supervisión y capacidad real de auditoría</b>». Recomienda "
 "evitar la dependencia de un único proveedor y la concentración del control técnico, extiende la gestión de "
 "riesgos más allá de la ciberseguridad convencional a propiedad intelectual, secretos comerciales y seguridad "
 "nacional, y afirma que la evaluación de impacto es, con carácter general, <b>obligatoria</b> en estos "
 "tratamientos.",
 "Porque es munición directa contra la postura más extendida en las negociaciones de encargo: «tengo la "
 "certificación del proveedor, estoy cubierto». La autoridad española dice por escrito que no, y añade la "
 "prueba que hay que poder ensenar: medidas técnicas, supervisión y <b>capacidad real de auditoría</b>. Esa "
 "última es la que casi nunca está en el contrato, y la que conviene negociar ahora. Es además la pieza de "
 "ejecución del Reglamento de Gobernanza de Datos y del Reglamento del Espacio Europeo de Datos de Salud, que "
 "exige que el acceso a datos de salud para uso secundario se haga obligatoriamente a través de un entorno de "
 "tratamiento seguro: cualquier cliente del ámbito sanitario o de investigación con datos secundarios tiene "
 "aquí el estándar frente al que se le va a medir. Y la recomendación de evitar la concentración del control "
 "técnico en un solo proveedor es la misma conversación que el artículo 31(9) de DORA desde otro ángulo.",
 'La <a href="https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-y-la-autoridad-helenica-de-'
 'proteccion-de-datos" @L>nota de la AEPD de 5 de noviembre de 2026</a> y la '
 '<a href="https://www.aepd.es/guias/entornos-tratamiento-seguro-es.pdf" @L>guía de entornos de tratamiento '
 'seguro</a>.',
 "Ganancia de método que corrige un aviso heredado, y conviene fijarla: <b>la AEPD es alcanzable</b>. Lo que "
 "falla son tres direcciones de canal de novedades heredadas, que devuelven error de servidor, y <b>cualquier "
 "parámetro de consulta en sus vistas</b>, que devuelve denegación. Los canales que funcionan son los de "
 "noticias, blog y resoluciones enlazados en el pie de cada listado, su mapa del sitio acepta parámetros, y los "
 "listados de resoluciones y de blog se sirven ya montados. Lo que sí se carga por guion es el listado de notas "
 "de prensa. Y hay retraso de caché demostrado: el canal del blog omite una entrada del 3 de noviembre que sí "
 "aparece en el listado."),

("ai", "Dinamarca y Suecia · 4 y 5 de noviembre de 2026", False,
 "Las autoridades de protección de datos entran en la IA del sector público por la puerta del RGPD, y una de "
 "ellas mete ya el artículo 5 del Reglamento de IA en una inspección en curso",
 "Tres actuaciones en dos días. El <b>4 de noviembre</b>, la autoridad danesa abrió <b>dos inspecciones</b>: "
 "una sobre la <b>Administración tributaria</b>, por una solución de IA que <b>selecciona empleados</b> del "
 "grupo del ministerio de Hacienda para control interno de cumplimiento de la legislación fiscal, iniciada "
 "entre otras cosas por una reclamación; y otra sobre una <b>región sanitaria</b> y su solución de apoyo a la "
 "decisión en psiquiatría para identificar pacientes con riesgo elevado de sujeción mecánica. En las dos "
 "examina las evaluaciones de impacto y el reparto de papeles y responsabilidades. Y añade, literal, que en la "
 "inspección de la Administración tributaria <b>investiga también cuestiones relativas a práctica de IA "
 "prohibida conforme al Reglamento de IA</b>. El <b>5 de noviembre</b>, la misma autoridad formuló <b>crítica "
 "grave</b> a un municipio por un sistema de monitorización con cámara e IA usado con <b>18 residentes durante "
 "un periodo de prueba de seis meses</b> en una residencia de mayores: su análisis de riesgos «enumeraba solo "
 "amenazas genéricas» y las valoró todas como riesgo bajo sin motivación, debió hacerse evaluación de impacto "
 "<b>antes de la puesta en uso</b> por tratarse de tecnología nueva y datos sensibles de personas vulnerables, "
 "y <b>el hecho de ser un periodo de prueba no altera la obligación</b>. El mismo 5 de noviembre, la autoridad "
 "sueca abrió inspección al servicio público de empleo por el sistema de IA que valora qué medidas recibe un "
 "demandante, y examinará <b>si existe decisión automatizada</b>.",
 "Porque dibuja el patrón del trimestre y es trasladable tal cual a cualquier cliente. Las autoridades de "
 "protección de datos están entrando en la IA del sector público <b>por la puerta del RGPD</b>, es decir "
 "licitud, necesidad, información y artículo 22, <b>antes de que el Reglamento de IA tenga aplicables sus "
 "obligaciones de alto riesgo</b>, que ahora son de diciembre de 2027. Dicho de otro modo: el plazo de "
 "adecuación del Reglamento de IA se ha alargado, pero el escrutinio no ha esperado. El caso de la "
 "Administración tributaria danesa es el precedente de cómo se va a construir un expediente de <b>IA que "
 "puntúa a empleados</b>: evaluación de impacto, reparto de responsabilidades y, encima, test de prohibición. Y "
 "la crítica al municipio cierra la puerta a la excusa más común, «es solo un piloto»: seis meses y dieciocho "
 "personas no son un piloto a efectos de obligación. El defecto que señala, catálogo de amenazas genéricas todo "
 "clasificado como riesgo bajo sin motivación, es el mismo que acaba de multar el regulador polaco.",
 'Las notas de la autoridad danesa sobre sus '
 '<a href="https://www.datatilsynet.dk/presse-og-nyheder/nyhedsarkiv/2026/nov/datatilsynet-undersoeger-'
 'offentlige-myndigheders-brug-af-ai" @L>dos inspecciones de IA en el sector público</a> y sobre la '
 '<a href="https://www.datatilsynet.dk/presse-og-nyheder/nyhedsarkiv/2026/nov/alvorlig-kritik-af-kommunes-brug-'
 'af-ai-i-aeldreplejen" @L>crítica grave al municipio</a>, y la de la autoridad sueca sobre su '
 '<a href="https://www.imy.se/nyheter/imy-granskar-arbetsformedlingens-ai-system-for-arbetssokande/" @L>'
 'inspección al servicio de empleo</a>.',
 "Las resoluciones danesas <b>no llevan multa</b>, y no porque el caso sea menor: la autoridad danesa no impone "
 "sanciones pecuniarias por vía administrativa. Quien compare importes entre Estados sin saberlo concluirá que "
 "Dinamarca es laxa, y es lo contrario. Y una laguna de calendario: la fecha de deliberación no se publica en "
 "ninguna de las tres actuaciones, solo la de publicación, de modo que no se pueden usar para medir plazos de "
 "tramitación."),

("ai", "Sanciones · 2 y 3 de noviembre de 2026", False,
 "Una sola multa nueva con componente de seguridad de los datos en toda la Unión, y el motivo no es el error "
 "humano sino el análisis de riesgos que no se actualizó después del incidente",
 "La autoridad polaca publicó el <b>2 de noviembre de 2026</b> una sanción de <b>64.652 zlotys</b>, unos quince "
 "mil euros al cambio corriente, a una <b>escuela superior de logística</b>, expediente DKN.5131.15.2022, por "
 "los <b>artículos 24.1, 25.1 y 32.1 y 32.2</b> del RGPD. Los hechos: una empleada de secretaría adjuntó por "
 "error un fichero con datos de <b>964 estudiantes</b> a un comunicado sobre asignación a grupos, y el fichero "
 "quedó disponible en la plataforma en línea; según las propias averiguaciones de la entidad, fue <b>abierto "
 "por 125 de las 388 personas con acceso y descargado 361 veces</b>. El motivo de la multa es lo aprovechable: "
 "el análisis de riesgos previo contemplaba fallo de hardware, daño del sistema, virus y acceso no autorizado, "
 "<b>pero no contemplaba la revelación de datos por error</b>, y el agravante decisivo es que <b>ni después de "
 "notificar el incidente, al repetir el análisis, actualizó el catálogo de amenazas</b>. Tercer reproche: la "
 "entidad alegó haber hecho controles selectivos sin encontrar irregularidades, pero <b>no documentó ni la "
 "realización de la prueba ni el método</b>. La autoridad sueca, el <b>3 de noviembre</b>, resolvió cuatro "
 "expedientes contra servicios de búsqueda de personas <b>sin multa</b>, con reprimenda y requerimiento, por "
 "los artículos 10 y 17, y lo hizo inaplicando la excepción constitucional nacional de los certificados "
 "voluntarios de publicación por <b>primacía del Derecho de la Unión</b>, sobre unas 3.800 reclamaciones.",
 "Por las tres preguntas que la resolución polaca pone en manos de cualquier consultor, y que se pueden hacer "
 "en una reunión de media hora. Una: <b>su catálogo de amenazas, contempla el envío erróneo</b>, o solo virus, "
 "hardware e intrusión. Dos: <b>lo actualizó después de su último incidente</b>, o repitió el mismo catálogo. "
 "Tres: <b>puede ensenar la evidencia de los controles que dice hacer</b>, con método documentado. Las tres son "
 "fallos de documentación, no de tecnología, y las tres se arreglan sin presupuesto. La métrica de exposición "
 "efectiva que publica el regulador, 125 aperturas de 388 accesos y 361 descargas, es además rarísima y vale "
 "para explicar a un comité por qué «el fichero estuvo poco tiempo» no es una atenuante. Y el caso sueco "
 "importa por otra razón: es una autoridad administrativa <b>inaplicando una norma nacional de rango "
 "constitucional por primacía</b>, lo que conviene tener fichado para cualquier discusión sobre excepciones "
 "nacionales al RGPD.",
 'La <a href="https://uodo.gov.pl/pl/138/4648" @L>sanción de la autoridad polaca de 2 de noviembre de 2026</a>, '
 'con el expediente y los hechos en su propia nota.',
 "Lo que no hay, porque también es dato: <b>ninguna sanción española publicada en la ventana</b>, confirmado "
 "por dos vías independientes, el canal de resoluciones ordenado por fecha de publicación, cuyo elemento más "
 "reciente es del 29 de octubre, y el listado servido, cuya fecha de publicación más reciente es del 27 de "
 "octubre. Se califica como confirmado <b>con reserva de caché</b>, porque los canales de la AEPD presentan "
 "retraso demostrado. Consecuencia: <b>no hay ninguna reducción del 20 por ciento por reconocimiento de "
 "responsabilidad ni del 20 por ciento por pago voluntario que calcular esta semana</b>, de modo que la "
 "distinción entre importe nominal e importe pagado no se activa en ningún caso español. Y la autoridad polaca "
 "<b>no publica la fecha de la deliberación</b>, solo la de publicación, con las dos rutas de su base de "
 "resoluciones devolviendo error."),

("ai", "CNIL · 9 de noviembre de 2026", False,
 "Hoy, un día fuera de ventana, la autoridad francesa ha dictado diez sanciones de ciberseguridad a entidades "
 "locales, y lo enmarca en la preparación de NIS2",
 "Se adelanta porque es de hoy y porque es el asunto más directamente aprovechable para clientes del sector "
 "público. La autoridad francesa ha publicado <b>diez sanciones simplificadas</b> contra entidades locales y un "
 "organismo público por incumplimientos de ciberseguridad, expresamente por el <b>artículo 32 del RGPD</b>. Los "
 "incumplimientos descritos: <b>sistemas operativos de servidores obsoletos y sin mantenimiento del editor</b>; "
 "sistemas de información usados para la relación en línea con los administrados <b>sin homologación de "
 "seguridad previa a su puesta en servicio pese a exigirlo el marco general de seguridad</b>; y <b>ausencia de "
 "análisis de riesgos</b>. La autoridad afirma que en 2026 dedica <b>la mitad de sus controles y acciones "
 "represivas a la seguridad de los datos</b>, que hay otros procedimientos en curso, y enmarca esta doble "
 "acción en la preparación de la entrada en aplicación de <b>NIS2, en curso de transposición</b>, que impone "
 "nuevas exigencias a las entidades locales.",
 "Porque es el espejo exacto de lo que va a pasar en España cuando haya autoridad y régimen sancionador, y "
 "porque los tres incumplimientos descritos son los tres que se encuentran en cualquier diagnóstico de un "
 "ayuntamiento mediano. El más reutilizable es el segundo: <b>sistema de relación en línea con los "
 "administrados puesto en servicio sin homologación de seguridad previa pese a exigirlo el marco nacional</b>. "
 "En España el equivalente es la conformidad con el <b>Esquema Nacional de Seguridad antes de la puesta en "
 "producción</b>, y la cantidad de sedes electrónicas y de aplicaciones de gestión que están en servicio sin "
 "ella es el agujero que esta semana se ha visto en La Laguna. El encuadre en NIS2 que hace la propia autoridad "
 "es además el argumento de oportunidad: la supervisión de entidades locales se está endureciendo <b>antes</b> "
 "de que la directiva sea exigible, no después.",
 'La nota de la autoridad francesa sobre <a href="https://www.cnil.fr/fr/sanctions-cybersecurite-collectivites-'
 'territoriales" @L>ciberseguridad de las entidades territoriales y diez sanciones</a>, de 9 de noviembre de '
 '2026.',
 "<b>Es de hoy, fuera de la ventana del 2 al 8 de noviembre</b>, y se marca como tal. Y la nota <b>no publica "
 "los importes ni la identidad de las entidades sancionadas</b>, de modo que no hay cifra que dar y no se "
 "inventa. Aviso de método sobre esta autoridad, porque produce falsos negativos: su <b>registro público de "
 "sanciones va muy por detrás</b>, su tabla de 2026 termina en una sanción de abril y no contiene ni la de una "
 "gran cadena de distribución del 22 de octubre ni estas diez. El listado utilizable es el de actualidad, no el "
 "registro."),
]

ITEMS += [

("thr", "Catálogo de vulnerabilidades explotadas · versión de 6 de noviembre de 2026", True,
 "Mañana vencen dos plazos, no uno, y el catálogo ya no tiene plazos lejanos: la nueva directiva los ha dejado "
 "entre tres y catorce días",
 "Descargado el catálogo, versión <b>2026.11.06</b>, publicada el 6 de noviembre a las 19:44:45 UTC con "
 "<b>1.769 entradas</b>. Entre el 2 y el 8 de noviembre se añadieron <b>exactamente tres</b>, y las tres con "
 "ransomware declarado como desconocido: <b>CVE-2026-119977</b>, condición de carrera en la ventana de "
 "actualización del núcleo de WordPress con ejecución de código sin autenticar, añadida el 3 con plazo el 6, "
 "<b>ya vencido</b>; <b>CVE-2024-27834</b>, elusión de autenticación de punteros en varios productos de Apple, "
 "añadida el 4 con plazo el 18; y <b>CVE-2026-19868</b>, elusión de SAML y de la autenticación multifactor "
 "impuesta por SAML en el servicio de red privada virtual de SonicWall, añadida el 6 con plazo el 20. Y lo que "
 "vence antes no es ninguna de ellas: <b>mañana, 10 de noviembre, vencen dos plazos empatados</b>, el de "
 "<b>CVE-2026-111497</b>, la escritura fuera de límites del descodificador Brotli, y el de "
 "<b>CVE-2026-48356</b>, en Adobe Commerce y Magento, los dos añadidos el 27 de octubre. Después, el 11 vence "
 "el de VMware ESX y el 13 el de Ivanti Connect Secure.",
 "Por un cambio estructural que afecta a cualquier cliente que use este catálogo como referencia contractual, y "
 "muchos lo hacen. Las tres entradas de la ventana llevan la obligación conforme a la nueva directiva "
 "estadounidense de priorización basada en riesgo, con requisitos de triaje forense, y de ahí salen <b>plazos "
 "de entre tres y catorce días</b>, desiguales y mucho más cortos que los quince o veintiún días de antes. "
 "<b>En la práctica, la categoría de plazo lejano ha desaparecido del catálogo reciente</b>, y eso obliga a "
 "replantear las ventanas de parcheo: un acuerdo de niveles de servicio que prometa parchear lo del catálogo en "
 "quince días ya no cumple. Y la entrada de WordPress ilustra el otro problema: <b>plazo de tres días y ya "
 "incumplido</b>, con lo que un cliente que mire el catálogo hoy encontrará un plazo vencido sin haber tenido "
 "margen material de reacción.",
 'El <a href="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json" @L>catálogo '
 'de vulnerabilidades explotadas conocidas</a>, en su canal de datos, que es la vía que responde.',
 "Dos cautelas de cobertura y una trampa de fecha. La primera: el catálogo se publicó el <b>6 de noviembre a "
 "las 19:44 UTC</b>, de modo que <b>estructuralmente no puede reflejar los días 7 y 8</b>, sábado y domingo. No "
 "se afirma que no haya nada esos dos días, se afirma que el catálogo publicado no los cubre. La segunda: el "
 "barrido masivo por puntuación no se ha podido hacer, porque la interfaz de programación de la base nacional "
 "de vulnerabilidades devuelve un recurso provisional y no sirve consultas, de modo que el inventario de "
 "puntuaciones de 9,0 o más <b>se ha construido fabricante a fabricante y puede no ser exhaustivo</b> fuera de "
 "los fabricantes barridos. Y la trampa: la entrada de WordPress se añadió el 3 de noviembre, pero <b>la "
 "versión corregida se publicó el 28 de octubre</b> y su puntuación según la autoridad de numeración es 8,1, es "
 "decir por debajo de 9,0. La fecha del catálogo no es la fecha del parche."),

("thr", "Cisco · 3 de noviembre de 2026", True,
 "Cisco reeditó el parche de una vulnerabilidad de 9,8 explotada activamente sin cambiar el número de versión, "
 "y quien lo instaló antes del 31 de octubre tiene una corrección insuficiente",
 "Leído el historial de versiones completo en el documento estructurado del propio fabricante. La "
 "vulnerabilidad es <b>CVE-2026-76461</b>, inyección de SQL en el análisis de correo de Cisco Secure Email "
 "Gateway que lleva a <b>ejecución de comandos como superusuario sin autenticar</b>, puntuación <b>9,8</b>, sin "
 "soluciones temporales, y en el catálogo de explotadas desde el 14 de septiembre. Las fechas, que hay que "
 "mantener separadas: publicación inicial el <b>14 de septiembre de 2026</b>, con Cisco declarando que su "
 "equipo de respuesta tuvo conocimiento de explotación activa en septiembre; el <b>31 de octubre</b>, literal "
 "del aviso, «a la luz de información nueva relacionada con código de explotación disponible en línea, el 31 de "
 "octubre Cisco publicó una <b>versión actualizada de la corrección contenida en la versión 15.5.5-014</b>»; y "
 "la revisión <b>1.2.0 del 3 de noviembre</b>, que es la que cae en la ventana y que actualiza la información "
 "sobre esa misma versión en la tabla de versiones corregidas.",
 "Porque es un parche silenciosamente reeditado bajo el mismo identificador, y eso rompe el control más básico "
 "de cualquier gestión de vulnerabilidades: comprobar la versión instalada. <b>Quien instaló la 15.5.5-014 "
 "antes del 31 de octubre tiene una corrección insuficiente y su inventario le dice que está parcheado.</b> "
 "Cisco da el procedimiento de comprobación, que es lo accionable esta semana: ejecutar el comando de estado "
 "del motor de remediación retroactiva y confirmar que está en marcha. Y da un indicador de compromiso "
 "concreto, buscar la cadena de copia a programa en los registros de correo, con una advertencia que conviene "
 "trasladar al cliente: <b>con privilegios de superusuario el atacante puede borrar las huellas</b>, de modo "
 "que hay que cruzar con registros de red y de cortafuegos externos al equipo y no dar por bueno un registro "
 "limpio en la propia máquina.",
 'El <a href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-'
 '2bLVGmhX" @L>aviso de Cisco sobre CVE-2026-76461</a>, con su historial de versiones completo.',
 "Es el ejemplo didáctico de la segunda trampa de método de esta sección, la de tomar la fecha del "
 "intermediario por la del fabricante. Desplazamientos medidos esta semana, todos resueltos yendo al documento "
 "del emisor original y leyendo su propio historial: un aviso del CERT francés del 6 de noviembre cita un "
 "boletín de un fabricante de virtualización del 27 y 28 de octubre, <b>nueve días</b>; otro del 2 de noviembre "
 "cita un aviso de Ivanti del 13 de octubre, <b>veinte días</b>; y otro del 5 de noviembre cita un aviso de "
 "Siemens publicado el <b>11 de agosto</b>, es decir <b>ochenta y seis días</b>. Quien fecha por el relé "
 "desplaza el hallazgo hasta casi tres meses."),

("thr", "Siemens · 3 a 6 de noviembre de 2026", False,
 "La vulnerabilidad de Brotli entra en software de red eléctrica y de gestión técnica de edificios, y su plazo "
 "del catálogo vence mañana",
 "<b>Ninguna publicación inicial nueva en la ventana</b>, pero <b>seis revisiones sobre avisos ya existentes</b> "
 "entre el 3 y el 6 de noviembre, leídas en el historial propio de Siemens. Las dos que importan: el aviso "
 "<b>SSA-045512</b>, publicado el 30 de octubre con puntuación 9,8 en la versión 3.1 y 9,2 en la versión 4, "
 "pasó a <b>V1.1 el 4 de noviembre añadiendo Desigo CC</b>, que es gestión técnica de edificios, y a <b>V1.2 el "
 "6 de noviembre añadiendo Gridscale X DSA y PSS(R)E</b>, que es software de red eléctrica; para la primera la "
 "remediación es instalar las actualizaciones de seguridad de la plataforma por el canal del sistema operativo, "
 "y las otras dos van a versión corregida. Y el <b>SSA-443410</b> pasó a V1.1 el 6 de noviembre añadiendo "
 "correcciones para cinco configuradores de su plataforma industrial y un producto afectado nuevo. Las otras "
 "cuatro revisiones son del 4 y el 5 de noviembre, e incluyen la <b>revisión 1.3 del SSA-166980</b>, que es la "
 "que el INCIBE-CERT relayó el 3 y actualizó el 6, incorporando un producto de monitorización local entre los "
 "afectados por los dos CVE de PHP, con los tres CVE de ese aviso marcados con <b>explotación confirmada</b>. "
 "El CVE de fondo, <b>CVE-2026-111497</b>, es del 22 de octubre y no de la ventana.",
 "Porque es el hilo que recorre toda la semana y porque su plazo vence mañana. Lo que hay que contar como "
 "novedad <b>no es el CVE, son las ampliaciones de producto</b>, con la fecha del historial propio de cada "
 "fabricante. Y la ampliación de esta semana cambia el sector: <b>Spectrum Power y Gridscale X son gestión de "
 "red eléctrica</b>, es decir sector energía, entidad esencial del anexo I de NIS2 y sector estratégico de la "
 "Directiva de entidades críticas, y Desigo CC es gestión técnica de edificios. Para un cliente industrial o "
 "energético esto es un disparador de revisión de inventario de tecnología operativa y de la evidencia de "
 "op.exp.4 del ENS. Y hay un dato operativo incómodo: para una parte del perímetro <b>no hay parche</b> y la "
 "indicación del fabricante es desinstalar las aplicaciones afectadas y proteger con cortafuegos o cortafuegos "
 "de aplicación, es decir <b>medida compensatoria documentada y no parcheo</b>, que es lo que hay que poder "
 "justificar en una auditoría.",
 'Los avisos <a href="https://cert-portal.siemens.com/productcert/html/ssa-045512.html" @L>SSA-045512</a> y '
 '<a href="https://cert-portal.siemens.com/productcert/html/ssa-443410.html" @L>SSA-443410</a> en el portal de '
 'Siemens, con sus historiales, y el <a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos-sci/'
 'multiples-vulnerabilidades-en-productos-de-siemens-1" @L>aviso INCIBE-2026-818</a>, publicado el 3 y '
 'actualizado el 6 de noviembre.',
 "El aviso del INCIBE es el ejemplo didáctico perfecto de la primera trampa de método, la del estado abierto "
 "que no es una actualización: <b>publicado el 3, ampliado de alcance el 6, y el listado sigue mostrando la "
 "fecha de publicación del 3</b>. Quien comprobó su exposición el día 4 contra la lista de entonces tiene un "
 "activo nuevo sin revisar. Solo abriendo la ficha se ve que el alcance cambió. Y dos revisiones de Siemens de "
 "esta semana son engañosas en el otro sentido y conviene no contarlas como exposición nueva: una cuyo cambio "
 "es literalmente «ajustada la entrada de historial de la versión anterior», es decir cosmética, y otra que "
 "solo añade productos a la lista de <b>no afectados</b>, que es buena noticia."),

("thr", "SonicWall · 3 y 6 de noviembre de 2026", False,
 "Dos avisos nuevos en la ventana, uno con explotación reconocida por el propio fabricante y otro de 9,1 sin "
 "parche porque el producto está en fin de vida",
 "Leídos en la interfaz de programación del propio equipo de respuesta del fabricante, porque su página se "
 "carga por guion. El <b>6 de noviembre a las 10:40 UTC</b>, aviso <b>SNWLID-2026-0014</b>, versión 1.0, con "
 "<b>siete vulnerabilidades</b> y máximo 8,8: política de dominios cruzados permisiva y validación de sesión "
 "contra la interfaz de gestión por atacante remoto no autenticado, un desbordamiento de montículo antes de "
 "autenticación en el servicio de red privada virtual, y la que ha entrado en el catálogo de explotadas, "
 "<b>CVE-2026-19868</b>, de 7,1, <b>elusión de los controles de autenticación SAML y, con ella, de la "
 "autenticación multifactor impuesta por SAML</b>, con el literal del fabricante de que su equipo de respuesta "
 "«ha investigado un informe que indica explotación potencial de esta vulnerabilidad». Solo afecta si SAML está "
 "habilitado para los inicios de sesión de ese servicio. El <b>3 de noviembre</b>, aviso "
 "<b>SNWLID-2026-0019</b>, versión 1.0, <b>9,1 crítico</b>: <b>CVE-2026-109593</b>, lectura de ficheros "
 "internos sin autenticar en su sistema de gestión global, versiones 9.5.2 y anteriores, con el literal "
 "«<b>no hay versión corregida disponible porque el producto ha llegado a fin de vida</b>» y sin solución "
 "temporal. Lleva además un segundo CVE, una inyección de SQL autenticada de 6,8.",
 "Porque SonicWall pesa mucho en la mediana empresa española y porque los dos avisos son directamente "
 "accionables, cada uno por una razón distinta. El de la elusión de SAML es el más urgente en términos de "
 "plazo, vence el 20 de noviembre, y tiene una comprobación de cinco minutos: <b>si SAML no está habilitado "
 "para los inicios de sesión de la red privada virtual, no aplica</b>, y si lo está, hay que ir a la versión "
 "corregida. Lo grave es lo que significa: una elusión que <b>anula la autenticación multifactor impuesta por "
 "el proveedor de identidad</b>, que es justo el control que un cliente presenta en una auditoría como "
 "mitigación de credenciales robadas. El segundo caso repite exactamente el patrón del expediente de la "
 "refrigeración, y conviene decirlo junto: <b>interfaz de gestión, producto en fin de vida, sin parche, y la "
 "remediación es migrar</b>. Es el mismo defecto de clase, en un activo de gestión de red.",
 'Los avisos <a href="https://psirtapi.global.sonicwall.com/api/v1/vulndetail/?advisory_id=SNWLID-2026-0014" '
 '@L>SNWLID-2026-0014</a> y <a href="https://psirtapi.global.sonicwall.com/api/v1/vulndetail/?advisory_id='
 'SNWLID-2026-0019" @L>SNWLID-2026-0019</a>, leídos en la interfaz del propio equipo de respuesta, que es la '
 'que devuelve el historial de revisiones.',
 "Comprobados uno a uno los avisos vecinos por numeración para confirmar que solo dos caen en la ventana: los "
 "anteriores son de agosto, septiembre y octubre, y los dos siguientes todavía no existen. La página en código "
 "de cada aviso es una cáscara de guion de menos de un kilobyte, de modo que cualquiera que raspe el código "
 "servido concluirá que no hay avisos: la vía buena es la interfaz de programación."),

("thr", "HPE y Proyecto Xen · 3 de noviembre de 2026", False,
 "Contraseñas embebidas con acceso administrativo remoto no autenticado en un gestor de centro de datos, y una "
 "ruptura de aislamiento entre máquinas virtuales que su propio proyecto declara sin mitigación",
 "Dos avisos del mismo día. El primero, <b>HPESBNW05172</b>, publicado el 3 de noviembre de 2026 con estado "
 "final y severidad crítica, sobre el gestor de tejido de centro de datos de HPE: <b>CVE-2026-95731</b>, "
 "contraseñas embebidas en la interfaz de línea de comandos con <b>acceso administrativo remoto no "
 "autenticado</b>, puntuación <b>9,8</b>; <b>CVE-2026-95732</b>, elusión de autenticación en el sistema "
 "operativo subyacente que lleva a ejecución de código, 9,6; y <b>CVE-2026-95733</b>, credenciales embebidas con "
 "ejecución de código desde red adyacente, 9,6. Afecta a las ramas 7.4.0 y anteriores y 7.3.4 y anteriores, "
 "corregido en 7.4.1 y 7.3.5. El segundo, aviso <b>XSA-523</b> del Proyecto Xen, publicado el 3 de noviembre a "
 "las 12:00: <b>CVE-2026-102703 y CVE-2026-102704</b>, validación incorrecta de la caché de operaciones de "
 "copia concedida, con impacto literal de que «<b>un huésped malicioso puede leer y escribir memoria arbitraria "
 "perteneciente a otros dominios, incluido el dominio de control</b>». Vulnerables todas las versiones desde la "
 "4.6; las 4.5 y anteriores no. Y la mitigación, literal: «<b>no se conoce mitigación</b>». Solo parches. El "
 "6 de noviembre se publicaron además tres avisos más del mismo proyecto, por uso después de liberar en sus "
 "controladores de red y de bloque provocable por el huésped.",
 "Porque los dos son conversaciones de riesgo distintas a la de un parche más. Las <b>credenciales de fábrica "
 "en un plano de gestión de centro de datos</b> son el mismo defecto de clase que el usuario y contraseña de "
 "fábrica que el fabricante de supervisores de frío publica en su propio boletín, pero en un activo mucho más "
 "crítico: quien alcanza el gestor de tejido alcanza la red del centro de datos. Y una ruptura de aislamiento "
 "entre máquinas virtuales que llega al dominio de control y que el proyecto declara <b>sin mitigación "
 "conocida</b> no se gestiona con una ventana de parcheo, se gestiona decidiendo si se sigue operando "
 "multiinquilino mientras no esté parcheado. Afecta a cualquier cliente con virtualización Xen y, sobre todo, a "
 "los proveedores de alojamiento europeos, que es una dependencia que muchos clientes tienen sin saberlo.",
 'El aviso <a href="https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05172.txt" @L>'
 'HPESBNW05172</a>, firmado por el fabricante, y el <a href="https://xenbits.xenproject.org/xsa/advisory-523.'
 'html" @L>aviso XSA-523 del Proyecto Xen</a>.',
 "Aviso de calendario del mismo proyecto, por si alguien planifica la semana: los avisos <b>XSA-529 y XSA-530 "
 "figuran asignados y bajo embargo, con liberación prevista el 10 de noviembre de 2026 a las 18:00</b>, fuera "
 "de la ventana. Y conviene saber que Xen <b>no asigna puntuación</b> a sus avisos, de modo que cualquier "
 "puntuación que se vea asociada a un XSA viene de un tercero."),

("thr", "Microsoft · 5 de noviembre de 2026", False,
 "Un 10,0 en el registro de dispositivos de Entra que no genera ni una tarea de parcheo, y ningún parche fuera "
 "de ciclo para producto en local",
 "Verificado en el documento estructurado del centro de respuesta de Microsoft. <b>No hubo publicación de "
 "emergencia para producto en local</b> en la ventana: existe un documento de actualizaciones tempranas de "
 "noviembre, con fecha inicial del <b>4 de noviembre</b> y revisión 138 del <b>7 de noviembre</b>, con 93 "
 "vulnerabilidades, pero <b>su árbol de productos solo contiene navegador, software de código abierto y "
 "nube</b>: ni Windows, ni Exchange, ni SharePoint, ni Office. Es la publicación mensual rutinaria previa al "
 "martes de parches, que es mañana. Lo que sí hay es <b>CVE-2026-109469</b>, elevación de privilegios en el "
 "registro de dispositivos de Entra, con puntuación <b>10,0</b>, revisión 1.0 del 5 de noviembre, declarada "
 "<b>no divulgada públicamente y no explotada</b>, y con el literal de Microsoft de que «<b>esta vulnerabilidad "
 "ya ha sido completamente mitigada por Microsoft. No hay acción que deban tomar los usuarios de este "
 "servicio</b>», publicada por transparencia.",
 "Porque es un 10,0 en el plano de identidad de casi cualquier cliente europeo y <b>no genera ninguna tarea de "
 "parcheo</b>, y saber distinguir eso ahorra una reunión de pánico. Sirve para la conversación de dependencia "
 "del proveedor en la nube, no para el calendario de parches: el cliente no puede hacer nada, no tiene que "
 "hacer nada y tampoco puede verificar nada por sí mismo. Eso, dicho en un comité, es exactamente el argumento "
 "de riesgo de concentración que la guía de la AEPD de esta misma semana pide documentar, y la pregunta que "
 "deja encima de la mesa es la de siempre: <b>qué capacidad real de auditoría tiene el cliente sobre el plano "
 "de identidad que usa</b>. Conviene además guardarlo como ejemplo de buena práctica del proveedor: publicar "
 "por transparencia un fallo ya mitigado es lo que permite tener esta conversación.",
 'El documento de <a href="https://api.msrc.microsoft.com/cvrf/v3.0/cvrf/2026-Nov" @L>actualizaciones de '
 'seguridad de noviembre de 2026</a> del centro de respuesta de Microsoft, con el árbol de productos y el '
 'historial de revisiones.',
 "Revisado también el documento de octubre: <b>619 identificadores con revisión dentro de la ventana y ninguno "
 "con estado de explotación afirmativo</b>, todos de núcleo de Linux y componentes de código abierto, sin "
 "cambios de estado de explotación. Y una precisión sobre el único producto no de nube del documento de "
 "noviembre: es el navegador, que se actualiza solo, de modo que la conclusión de que no hubo parche fuera de "
 "ciclo para producto en local es firme."),

("thr", "Fabricantes y CERT · comprobado fabricante por fabricante", False,
 "Veinticuatro días sin que el CERT del país donde empezó la campaña del frío toque su alerta, mientras "
 "publicaba y revisaba otras tres en la misma ventana",
 "Lo más instructivo de la ventana es un negativo, y está ahora blindado. La alerta <b>CERTFR-2026-ALE-012</b> "
 "sobre los controladores de refrigeración sigue con <b>exactamente tres entradas en su historial</b>, la "
 "última del <b>16 de octubre de 2026</b>, su marca de cierre sigue vacía, sus campos de identificadores de "
 "vulnerabilidad y de avisos de fabricante siguen vacíos y su riesgo sigue siendo «no especificado por el "
 "editor». Veinticuatro días sin tocarse. Y lo que convierte eso en hallazgo y no en sospecha de caché es que "
 "<b>el mismo CERT sí publicó y revisó dentro de la ventana</b>: la alerta de OpenSSH el 5 de noviembre, con "
 "una actualización fechada el 6 dentro de su resumen, y la de Ivanti con revisión registrada el <b>2 de "
 "noviembre</b> que añade dos identificadores de vulnerabilidad. En la misma ventana publicó además <b>39 "
 "avisos</b>. El negativo es real.",
 "Porque es el argumento más fuerte que hay esta semana para explicar a un cliente por qué no puede delegar su "
 "vigilancia en un solo canal. <b>El caso avanzó, pero no avanzó donde se estaba mirando</b>: lo movieron "
 "ENISA el 4 de noviembre, el centro nacional irlandés el 3, el croata el 4, el sueco el 2 y el 6, el "
 "neerlandés el 2, la autoridad griega el 3 y la italiana el 3 y el 4. Quien seguía la alerta francesa, que es "
 "la que todo el mundo citaba, no vio nada en nueve días. La regla operativa que se lleva un cliente es "
 "concreta: <b>una alerta marcada como en curso no es una alerta actualizada</b>, y hay que leer la fecha de su "
 "última versión, no su estado.",
 'La alerta <a href="https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/" @L>CERTFR-2026-ALE-012</a>, con su '
 'gestión detallada del documento, y su versión en datos estructurados, que es la que permite contar las '
 'revisiones sin interpretar.',
 "Comprobado y sin novedad, fabricante por fabricante y con la fecha de su último boletín: <b>SAP</b>, nada, "
 "su día de parches es mañana y por diseño no podía haber nada en la ventana, aunque <b>solo se ha verificado "
 "la cadencia y no la fecha de su último día de parches</b>, porque su lista de notas se carga por guion y su "
 "bitácora devuelve un reto anti robot. <b>Ivanti</b>, sin aviso nuevo: el último es del 13 de octubre y su "
 "página no es legible. <b>Schneider Electric</b>, dos avisos del 13 de octubre y nada en la ventana. "
 "<b>Broadcom y VMware</b>, su aviso figura con estado abierto pero sus fechas propias son del 27 y el 28 de "
 "octubre. <b>Atlassian</b>, nada: su índice de 2026 no tiene sección de noviembre y su boletín mensual sale el "
 "tercer martes. <b>Palo Alto Networks</b>, nada en la ventana, su última actualización es del 31 de octubre. "
 "<b>Fortinet</b> sí publicó, el 2 de noviembre, un aviso con puntuación 9,8 de un uso después de liberar en el "
 "núcleo de Linux, pero <b>el detalle de productos afectados no se ha podido leer</b>, porque la página del "
 "aviso devuelve error de servidor, y hay una discrepancia sin reconciliar entre su documento estructurado, que "
 "sigue en versión 1 del 2 de noviembre, y su propio canal, que dice revisado el 7. Y el <b>CCN-CERT no se ha "
 "alcanzado en absoluto</b>: su listado de alertas y el de avisos devuelven denegación con un reto anti robot, "
 "de modo que no se puede afirmar nada sobre su actividad esta semana. Alcanzados y sin coincidencias: el "
 "<b>CERT de las instituciones europeas</b>, cuyo último aviso es del 27 de septiembre, y el canal del "
 "<b>centro alemán de respuesta</b>, muy activo los días 5 y 6, que corrobora el caso de fin de vida de "
 "SonicWall como no parcheado."),
]

BULOS = [
 ("«El 2 de febrero de 2027 es un hito del Reglamento de IA.»",
  "<b>No existe.</b> Recuento literal sobre los tres textos completos, anexos incluidos: la cadena aparece "
  "<b>cero veces</b> en el Reglamento (UE) 2024/1689 original, cero en el Reglamento (UE) 2026/1744 que lo "
  "modificó y cero en el consolidado a 27 de julio de 2026, también en su versión española. Las tres fechas "
  "próximas que sí están en el articulado y con las que es fácil confundirla son el <b>2 de febrero de 2025</b>, "
  "aplicación de los capítulos I y II; el <b>2 de febrero de 2026</b>, fecha en la que la Comisión debía dar "
  "directrices sobre la aplicación práctica de la clasificación de alto riesgo, artículo 6.5, que además está "
  "<b>expresamente excluido</b> del aplazamiento; y el <b>2 de diciembre de 2027</b>, que es probablemente la "
  "que se estaba buscando. Si aparece en alguna edición anterior de este boletín, hay que corregirlo."),
 ("«El alto riesgo del anexo III del Reglamento de IA se aplica desde el 2 de agosto de 2026.»",
  "<b>Ya no.</b> La letra c) del párrafo tercero del artículo 113 fue <b>sustituida</b> por el Reglamento (UE) "
  "2026/1744 y dice ahora <b>2 de diciembre de 2027</b> para el alto riesgo del artículo 6.2 y del anexo III, y "
  "<b>2 de agosto de 2028</b> para el del artículo 6.1 y el anexo I. Cualquier plan de adecuación construido "
  "sobre agosto de 2026 está trabajando con una fecha derogada, y quien asumió que el nuevo hito era agosto de "
  "2027 también se equivoca por cuatro meses. Precisión adicional, porque se cuenta mal: el techo del <b>2 de "
  "agosto de 2030</b> del artículo 111.2 para el alto riesgo heredado destinado a autoridades públicas <b>ya "
  "estaba en el texto de 2024</b>; lo que cambió en 2026 es el disparador, que ya no es una fecha fija sino la "
  "fecha de aplicación del capítulo III."),
 ("«La ISO publicó la norma 27028 sobre los atributos de los controles.»",
  "<b>Corrección a este boletín, edición 010, y sigue sin publicarse por tercera semana.</b> La ficha dice "
  "«norma internacional en producción, etapa 60.00» desde el <b>20 de octubre de 2026</b>, y la línea «60.60, "
  "norma internacional publicada» <b>aparece sin fecha</b>. Lo nuevo de esta semana es que la ficha muestra "
  "<b>fecha de publicación prevista 2026-11</b> y su cabecera habla de pasos finales de producción de hasta "
  "siete semanas: la ISO <b>anuncia</b> noviembre, pero a 9 de noviembre no se ha materializado y no debe darse "
  "por hecho."),
 ("«El paquete de infracciones de octubre de la Comisión se decidió el 30 de septiembre de 2026, y antes hubo "
  "otro en septiembre.»",
  "<b>Corrección a este boletín y a su propio método.</b> Las dos cosas están mal. La fuente primaria fecha "
  "<b>decisión y comunicación el 1 de octubre de 2026</b>, con publicación en el repositorio el 2, y usa la "
  "fórmula «hoy la Comisión ha decidido»: el 30 de septiembre no aparece ni en los metadatos ni en el texto, de "
  "modo que no se atribuye la decisión a esa fecha salvo que aparezca un acta del Colegio que lo diga. Y <b>no "
  "existe ningún paquete de infracciones de septiembre de 2026</b>: los de 2026 son seis, de enero, marzo, "
  "abril, junio, julio y octubre."),
 ("«La lista de proveedores terceros críticos de TIC se publica conforme al artículo 31(8) de DORA.»",
  "<b>Es el artículo 31(9), y citar el 8 dice justo lo contrario de lo que se quiere decir.</b> El apartado 9 es "
  "el que obliga a las autoridades europeas de supervisión, a través de su Comité Mixto, a establecer, publicar "
  "y <b>actualizar anualmente</b> la lista. El apartado 8 es la <b>lista de exclusiones</b> de la designación: "
  "entidades financieras que prestan servicios de TIC a otras, proveedores sujetos a los marcos del artículo "
  "127(2) del Tratado, proveedores intragrupo y proveedores que operan en un solo Estado miembro."),
 ("«El considerando 29 de la Directiva de entidades críticas es el que limita el sector alimentario.»",
  "<b>Es el considerando 5.</b> Verificado por posición entre los marcadores de considerandos del texto "
  "español. Y su literal añade un requisito que conviene no perder: las entidades críticas «<b>únicamente</b> "
  "deben incluir las empresas alimentarias [...] que se dediquen <b>exclusivamente</b> a la logística y "
  "distribución al por mayor y la producción y transformación industrial a gran escala <b>que registren una "
  "cuota de mercado importante a escala nacional</b>». La palabra «exclusivamente» está también en el anexo, "
  "sector 11, de modo que una cadena de supermercados no será entidad crítica."),
 ("«El artículo 2.2.c) de NIS2 habla de repercusiones sobre la protección pública.»",
  "<b>Dice «el orden público».</b> El literal español es «repercusiones significativas sobre la <b>seguridad "
  "pública, el orden público o la salud pública</b>». La confusión tiene origen identificado y conviene "
  "conocerlo para no contaminar la cita: la expresión «la seguridad y la protección públicas» sí existe en NIS2, "
  "pero en el considerando 69, hablando de incidentes a gran escala, no en el artículo 2."),
 ("«Una cadena de alimentación en el ámbito de NIS2 es entidad importante y no esencial.»",
  "<b>Por defecto sí, pero la afirmación tal cual está incompleta de una forma que invierte la conclusión en "
  "este caso.</b> El artículo 3.2 hace importantes a las entidades de los anexos I o II que no sean esenciales "
  "por el apartado 1, y la alimentación está en el anexo II. Pero el <b>artículo 3.1.e)</b> dice que es esencial "
  "«cualquier otra entidad de uno de los tipos mencionados en los anexos I o II que un Estado miembro "
  "identifique como entidad esencial en virtud del artículo 2, apartado 2, <b>letras b) a e)</b>», y esas letras "
  "incluyen la c), que es la de salud pública. Es decir: cuando un Estado designa una cadena por repercusiones "
  "sobre la salud pública, <b>ese mismo Estado puede clasificarla como esencial</b>, con el régimen de multas "
  "del artículo 34.4, diez millones de euros o el 2 por ciento, en lugar del 34.5, siete millones o el 1,4 por "
  "ciento. La elección es del Estado miembro. Y la palanca técnica del caso, la inocuidad alimentaria, es la "
  "misma palanca que puede convertirla en esencial."),
 ("«El artículo 23.11 de NIS2 obliga a la Comisión a adoptar actos de ejecución también para los proveedores de "
  "servicios de confianza.»",
  "<b>No los cubre.</b> El listado obligatorio del artículo 23.11 es de infraestructura y servicios digitales: "
  "proveedores de servicios de sistema de nombres de dominio, registros de nombres de dominio de primer nivel, "
  "proveedores de servicios de computación en nube, de centros de datos, de redes de distribución de contenidos, "
  "de servicios gestionados y de servicios de seguridad gestionados, y proveedores de mercados en línea, motores "
  "de búsqueda y plataformas de redes sociales. Para los demás, incluida la alimentación, el acto de ejecución "
  "es <b>facultativo</b>, y por eso la calificación del incidente depende de la transposición nacional."),
 ("«La primera norma armonizada del Reglamento de IA tiene decisión de ejecución publicada en el Diario Oficial "
  "y la fecha está cerrada.»",
  "<b>Dato con reserva, y conviene decirlo.</b> La página de la Comisión fecha la publicación el <b>19 de "
  "octubre de 2026</b>, y por otra vía consta una decisión de ejecución de 12 de octubre de 2026 sobre las "
  "normas armonizadas para sistemas de IA de alto riesgo, publicada en la serie L el 14 de octubre, que cita la "
  "<b>EN 18286:2026</b>, de sistema de gestión de la calidad. Las dos fechas no concuerdan y una consulta "
  "estructurada por actos basados en el Reglamento de IA desde septiembre <b>no devuelve esa decisión</b>, de "
  "modo que puede estar en la serie C sin relación de base jurídica en sus metadatos. Se publica como "
  "<b>pendiente de localizar en el Diario Oficial</b> y no como hecho cerrado."),
 ("«Las sanciones anónimas de la autoridad francesa suman 6,5 millones de euros y se pueden dar de alta.»",
  "<b>Corrección de una premisa de este boletín, y queda cerrada.</b> No existen como tales. De las 83 "
  "sanciones francesas de 2025 <b>solo diez se hicieron públicas</b>; las 73 restantes del procedimiento "
  "simplificado <b>no se publican en absoluto</b>, ni con nombre ni anonimizadas. Lo único que consta es que "
  "<b>catorce organismos</b> fueron sancionados por un incumplimiento relativo a la seguridad de los datos, sin "
  "importe desglosado y sin lista, con un tope legal de 20.000 euros por sanción. La cifra de 6,5 millones no "
  "está sostenida por ninguna publicación del regulador."),
]

SILENCIO = [
 ("BOE", "Revisados íntegramente por la interfaz de datos abiertos, con recorrido recursivo del árbol, los "
  "sumarios del 2 al 7 de noviembre: <b>siete diarios, números 272 a 278, y 1.306 asuntos en todas las "
  "secciones</b>, repartidos en 132 el día 2, 240 el 3, 234 el 4 sumando sus dos diarios, 205 el 5, 191 el 6 y "
  "304 el 7. El <b>8 de noviembre no hubo edición</b>, domingo, confirmado porque la interfaz devuelve "
  "inexistencia y no un error de acceso. <b>23 disposiciones generales</b> en la Sección I de toda la ventana, "
  "leídas una por una. <b>Cero disposiciones sobre ciberseguridad</b>, y cero coincidencias con límite de "
  "palabra de NIS2, Directiva 2022/2555, entidades críticas, infraestructuras críticas, Directiva 2022/2557, "
  "DORA, Esquema Nacional de Seguridad, Real Decreto 311/2022, Instrucción Técnica de Seguridad, INCIBE, "
  "Centro Criptológico, criptología, cifrado, centros de datos ni seguridad de las redes. Ocho asuntos con "
  "alguna coincidencia, ninguno normativo: resoluciones de personal de la AEPD y de la AESIA, un plan de "
  "estudios de máster, dos anuncios universitarios de modificación de datos personales en títulos, un contrato "
  "de tarjetas de identidad militar y una formalización de contrato de adquisición de licencias de antivirus "
  "para ciberdefensa. Las dos normas de la ventana que por título podían tener contenido de resiliencia no lo "
  "tienen: leído el texto consolidado del real decreto-ley del 3 de noviembre, su parte de accesibilidad "
  "equitativa a bienes y servicios en situaciones de emergencia se resuelve en límites de precios en servicios "
  "de transporte, sin obligaciones de continuidad ni digitales. Matiz de etiqueta, por precisión: <b>el segundo "
  "diario del día 4 no está etiquetado como extraordinario</b> por la fuente, solo es un segundo diario con dos "
  "asuntos, el cese del ministro de Transportes y el encargo del despacho ordinario al vicepresidente primero."),
 ("Consejo de Ministros, Congreso y Consejo de Estado", "<b>Una sola reunión del Consejo de Ministros en la "
  "ventana</b>, la del 3 de noviembre, verificado en el índice de referencias. Cero asuntos normativos de "
  "ciberseguridad, NIS2, entidades críticas, centros de datos, inteligencia artificial o gobernanza de datos, y "
  "tres dictámenes urgentes pedidos al Consejo de Estado que no son ninguno de esas materias. Sí hay "
  "contratación, y es lo que corrige un primer barrido: el contrato de servicios de seguridad de los sistemas "
  "de información de la Gerencia de Informática de la Seguridad Social, <b>22.925.795,06 euros</b> de valor "
  "estimado. La referencia publicada <b>está truncada en origen</b>, se corta a mitad de palabra en su último "
  "asunto, de modo que lo leído es todo lo que se sirve. <b>El dominio del Congreso devuelve denegación en las "
  "ocho rutas probadas</b>, incluidas las de datos abiertos y los boletines oficiales, y el del Senado "
  "también: el estado del expediente de entidades críticas y la ausencia de proyecto de NIS2 <b>no se han "
  "podido reverificar esta semana</b> y se arrastran de la edición 011 declarándolo. Y la base de dictámenes "
  "del Consejo de Estado del BOE <b>lleva un mes y un día de retraso</b>, comprobado con consulta propia por "
  "fecha de aprobación: 26 dictámenes desde el 1 de septiembre y el más reciente del 8 de octubre de 2026, "
  "expediente 949/2026. Su cero sobre el real decreto de centros de datos <b>no es concluyente</b> y no se "
  "publica como ausencia."),
 ("CCN, portal del ENS y catálogo de producto certificado", "El índice de actualidad del CCN declara <b>un solo "
  "asunto en noviembre de 2026</b>, el informe de IA ofensiva, frente a nueve en octubre. Su página sobre la "
  "Directiva NIS2 sigue publicada desde agosto de 2024 con fecha de contenido más reciente de abril de 2025, "
  "<b>sin cambios</b>. El portal del ENS <b>no publica ningún elemento fechado</b>, de modo que no se atribuye "
  "ningún cambio a la ventana, y su sección de normativa sigue listando <b>las mismas cuatro Instrucciones "
  "Técnicas de Seguridad</b>, lo que concuerda con que no haya ninguna resolución nueva entre los 1.306 asuntos "
  "del BOE. Sus contadores de certificación se recogen como dato sin fecha y <b>no deben atribuirse a esta "
  "semana</b>. El catálogo de producto y servicios certificados tiene <b>474 filas</b> y <b>no publica fecha de "
  "alta por entrada</b>, de modo que no sirve para datar movimientos; combinado con el índice de actualidad, no "
  "hay ninguna incorporación anunciada en la ventana. Y la laguna grande: <b>el repositorio de avisos y alertas "
  "del CCN-CERT y el de guías CCN-STIC devuelven denegación con reto anti robot</b>, de modo que es muy posible "
  "que haya guías nuevas o actualizadas y no se sabría."),
 ("INCIBE e INCIBE-CERT", "<b>16 avisos generales en la ventana</b>, cinco el 3, siete el 4, dos el 5 y dos el "
  "6, y cero el 2, el 7 y el 8; y <b>11 avisos de sistemas de control industrial</b>, seis el 3, dos el 4 y "
  "tres el 5, de Siemens, Festo, WAGO con dos, Phoenix Contact, ABB con dos, Dräger, Johnson Controls, Subnet "
  "Solutions y Welotec, <b>dos de ellos con actualización del 6 de noviembre</b>. <b>Dos entradas de bitácora "
  "en la ventana</b>, las dos leídas: la del octubre negro, del 3, que consolida PHP, el fallo crítico de "
  "GitLab sin autenticación, el de Brotli en Node.js, el bloqueo de ocho certificados intermedios de una "
  "autoridad de certificación por compromiso de claves, la retirada de un paquete de IA con código malicioso y "
  "dos accesos no autorizados confirmados; y la del 5, sobre el acceso no autorizado a un proveedor japonés de "
  "servidores en la nube, con <b>26.739 servidores</b> de alcance potencial que la propia compañía aclara que "
  "no son casos confirmados, suspensión progresiva desde las 04:00 del 21 de octubre, extracción confirmada de "
  "información de clientes incluidas credenciales de cuentas de negociación, compensación de 5.000 yenes por "
  "cliente más pérdidas confirmadas, y última actualización oficial del 4 de noviembre diciendo que la "
  "investigación sigue abierta y sin fecha de reanudación. <b>Cero guías y estudios</b> en la ventana: la "
  "publicación más reciente es de julio de 2026. <b>Cero notas de prensa</b>: la más reciente es del 27 de "
  "octubre. Una entrada de blog de empresas el 5 de noviembre, sobre protección de cuentas de creadores de "
  "contenido, <b>no confirmada</b> porque la fecha se tomó del listado. Intermitencia confirmada y documentada: "
  "en el barrido de avisos, páginas idénticas alternaron respuesta y error, con un caso de <b>cinco errores "
  "seguidos antes de servir</b>, y ningún cero de esta edición se apoya en un primer fallo."),
 ("Autoridades autonómicas", "<b>Dos noticias de la autoridad catalana de protección de datos en la ventana</b>, "
  "las dos leídas con su fecha propia: el Plan de Auditoría Preventiva del 3 y una jornada del 6 sobre "
  "Reglamento de IA y protección de datos, en la que confirma que <b>ya está disponible su nuevo modelo "
  "conjunto de evaluación de impacto de protección de datos y de derechos fundamentales</b>, que integra en un "
  "solo instrumento las dos evaluaciones. Eso último es lo aprovechable y conviene recoger el instrumento y no "
  "la jornada. <b>Una sola noticia de la autoridad vasca</b>, del 5 de noviembre, la convocatoria de sus "
  "premios, con plazo vivo. <b>Cero alertas de la agencia catalana de ciberseguridad</b> en la ventana: la más "
  "reciente es del 29 de octubre, y su sección de noticias <b>no se puede leer sin navegador</b> y queda sin "
  "barrer. <b>Cero noticias de la autoridad andaluza</b>: la más reciente es del 26 de octubre. Usados en todos "
  "los casos los dominios nuevos de la autoridad catalana y de la vasca, porque los antiguos sirven la misma "
  "cáscara para cualquier ruta y producen falsos positivos de fecha."),
 ("Diario Oficial de la Unión Europea", "<b>155 actos publicados en la ventana</b>, 45 en la serie L y 110 en "
  "la serie C, revisados uno a uno por título: 92 el día 3, 25 el 4, 16 el 5 y 22 el 6, y <b>cero actos con "
  "fecha de 2, 7 y 8 de noviembre</b>, con el cero del lunes verificado con consulta aislada y con prueba de "
  "control del día 3 devolviendo 92. Prueba de control de la ventana entera: la ventana anterior devuelve 271 "
  "actos, cifra distinta y no nula. <b>Cero actos de la ventana citan NIS2, la Directiva de entidades críticas, "
  "DORA, el Reglamento de IA, el Reglamento de Ciberresiliencia ni el Reglamento de Ciberseguridad</b>, con "
  "prueba de control de septiembre a hoy devolviendo 28 pares acto-norma. <b>Cero decisiones de ejecución sobre "
  "normas armonizadas</b> de esas normas: cribados los títulos por norma armonizada, petición de normalización "
  "y organismo notificado, cero coincidencias, y lo más próximo es una corrección de errores de una decisión de "
  "identificación remota de aeronaves no tripuladas. De los 45 actos de la serie L, <b>17 son correcciones de "
  "errores</b>, todas ajenas al ámbito. Otros actos revisados y descartados por no ser del ámbito: la decisión "
  "de un consorcio europeo de infraestructura digital en educación, una decisión de una institución europea "
  "sobre uso de decisiones individuales automatizadas en sus procesos de selección, el paquete de defensa del 3 "
  "de noviembre y una posición del Consejo en primera lectura sobre la nueva directiva de servicios de pago, que "
  "sustituirá a la actual y que conviene tener en el radar por su vecindad con DORA."),
 ("Comisión, ENISA y organismos europeos", "<b>54 documentos de prensa de la Comisión en la ventana</b>, "
  "revisados uno a uno por título y entradilla. <b>Ningún paquete de infracción nuevo</b> desde el de octubre: "
  "verificado por dos vías, el buscador de su sala de prensa y el sondeo directo de seis referencias "
  "posteriores, que devuelven cuerpo vacío, es decir inexistencia. Con la cadencia verificada de seis a ocho "
  "semanas, <b>el siguiente toca entre mediados y finales de noviembre</b> y conviene vigilarlo el lunes que "
  "viene. El propio seguimiento de hitos de la Comisión para noviembre, leído íntegro, <b>no contiene ni un "
  "solo hito de NIS2, entidades críticas, DORA, Ciberresiliencia, Reglamento de IA ni ciberseguridad</b>: son "
  "tasa aduanera de paquetes, cuotas de pesca, indicaciones geográficas, aditivos alimentarios, trazabilidad de "
  "lentes de contacto, normas de sostenibilidad, crédito al consumo, traslado de residuos y emisiones. En "
  "ENISA, <b>siete direcciones con fecha en la ventana</b> sobre un total de 2.943 fechadas, de las que dos son "
  "los hallazgos de esta edición y el resto son eventos y páginas institucionales. <b>Ninguna página de "
  "ciberseguridad de la dirección general de redes se modificó en la ventana</b>, con las fechas de última "
  "modificación verificadas una a una, y hay un aviso de método que conviene registrar: su mapa del sitio "
  "muestra 98 direcciones con fecha de la ventana, pero es una <b>regeneración masiva del sitio</b> los días 5 "
  "y 6, no cambios de fondo, y no se ha tratado como prueba de cambio en ningún caso. <b>Cero designaciones "
  "nuevas de autoridades nacionales</b> de las cinco normas, comprobado por tres vías, con la cautela de que "
  "las listas autoritativas de la Comisión para NIS2 por países y para el Reglamento de IA devuelven página no "
  "encontrada, de modo que es «no se ha encontrado nada» y no «no hay nada»."),
 ("Supervisores financieros", "<b>BCE y Mecanismo Único de Supervisión:</b> cero notas de prensa y cero "
  "publicaciones de supervisión en la ventana, con el feed de prensa cubriendo sin lagunas del 30 de septiembre "
  "al 6 de noviembre y la publicación más reciente de supervisión del 23 de octubre. Ninguna carta nueva al "
  "sector. <b>Tres discursos</b> del Consejo de Supervisión, los días 3, 5 y 6, los tres leídos íntegros, con "
  "una sola mención a los planes de acción. Prioridades supervisoras: vigentes las de 2026 a 2028, <b>sin "
  "publicación ni anuncio de las de 2027 a 2029</b>. Boletín de supervisión: el último es de agosto de 2026, y "
  "las tres direcciones probables de noviembre devuelven inexistencia. <b>ESMA:</b> cero noticias en la "
  "ventana, la más reciente del 29 de octubre, y ninguna consulta abierta ni cerrada dentro de ella. "
  "<b>EIOPA:</b> una sola publicación, la de documentación técnica del tipo libre de riesgo del 6 de noviembre, "
  "sin contenido de ciber ni de DORA; su cuadro de riesgos del 29 de octubre sitúa el riesgo cíber como "
  "preocupación principal, pero es anterior a la ventana. <b>Comité Mixto:</b> sin actos nuevos, su programa de "
  "trabajo para 2027 es del 13 de octubre. <b>Junta Europea de Riesgo Sistémico:</b> sin publicaciones, lo más "
  "reciente es un dictamen del 27 de octubre, con la cautela de que sus listados paginados se cargan por guion "
  "y sus cinco canales de novedades devuelven inexistencia, de modo que la conclusión se apoya en su portada. "
  "<b>Banco de España:</b> cuatro entradas en la ventana, dos intervenciones del Gobernador, el euríbor de "
  "octubre y una encuesta de financiación, <b>ninguna de ciber, TIC ni DORA</b>, y nada publicado del 5 al 8; "
  "cero circulares entre los 1.306 asuntos del BOE; consultas públicas, la más reciente de septiembre. De las "
  "dos intervenciones del Gobernador <b>se ha verificado título y fecha pero no el contenido</b>, porque sus "
  "páginas no sirven texto ni PDF, de modo que queda no confirmado que no traten de ciberseguridad. "
  "<b>TIBER-EU y TIBER-ES:</b> sin cambios y sin aviso de actualización; la guía española no lleva número de "
  "versión ni fecha. <b>DGSFP: no verificable</b>, su dominio con el prefijo habitual rechaza la conexión y el "
  "otro sirve una aplicación que carga por guion sin una sola fecha extraíble, de modo que <b>queda no "
  "confirmado</b> que no publicara nada, mitigado solo por que no hay ninguna disposición suya en el BOE de la "
  "ventana."),
 ("Normas, acreditación y NIST", "Comprobado apartado por apartado y ficha por ficha. <b>Comité de seguridad de "
  "la información:</b> <b>573 entradas de catálogo</b> revisadas con el ciclo de vida abierto en todas, último "
  "movimiento el 6 de noviembre, y <b>sin novedad en ninguna de las piezas de certificación</b>, con la 27001 "
  "en norma publicada desde octubre de 2022, su enmienda desde febrero de 2024, la 27002, la 27006-1, la 27005 "
  "y la 27701 sin movimiento en la ventana. <b>Comité de inteligencia artificial:</b> 100 entradas revisadas, "
  "último movimiento el 7 de noviembre, con la <b>42001 en norma publicada y último movimiento el 18 de "
  "diciembre de 2023, sin revisión en marcha</b>, y la <b>42006 publicada con último movimiento el 7 de julio "
  "de 2025</b>. <b>Retiradas:</b> 241 fichas comprobadas, <b>cero retiradas con fecha en la ventana</b>, la "
  "última es de julio de 2026. <b>Comité europeo de inteligencia artificial:</b> 35 entradas de programa de "
  "trabajo y 19 normas publicadas revisadas, <b>cero movimientos de etapa en la ventana</b>, último movimiento "
  "real del 29 de octubre y última norma publicada del 5 de agosto. <b>NIST:</b> catálogo de 1.744 registros, "
  "revisados los 100 más recientes, tres en la ventana, y sin cambios en el marco de ciberseguridad, el SP "
  "800-53, el SP 800-171, el marco de gestión de riesgos de IA ni los FIPS 203, 204 y 205. <b>ENAC:</b> 574 "
  "noticias revisadas, una en la ventana y es de acreditación de ensayos de aguas residuales, nada de ciber ni "
  "de certificación de ciberseguridad; sus documentos nuevos <b>no publican fecha por documento</b>, de modo "
  "que no se puede situar ninguno en la ventana, y lo más reciente datado es de septiembre. <b>Global ACI</b>, "
  "que es la organización que sustituye desde el 1 de enero de 2026 a las dos antiguas de acreditación y "
  "laboratorios: 58 documentos y 58 resoluciones revisadas, <b>cero en la ventana</b>, último documento del 20 "
  "de octubre y última resolución del 26 de octubre, una de ellas la transferencia de la base de datos de "
  "verificación de certificados, que interesa a quien compruebe certificados de proveedores. <b>UNE</b> queda "
  "sin verificar en fuente primaria, porque su sitio rechaza el acceso automatizado en las tres rutas "
  "probadas, mitigado con que no hay ninguna resolución de normas UNE en el BOE de la ventana."),
 ("Reglamento de IA, datos y autoridades de protección de datos", "<b>Cero actos de ejecución, actos delegados, "
  "directrices o códigos nuevos</b> basados en el Reglamento de IA con fecha o publicación en la ventana, "
  "verificado con dos consultas estructuradas, la segunda con prueba de control que devuelve una sola fila y es "
  "la Recomendación de cláusulas contractuales de esta edición. Páginas institucionales sin cambio, con sus "
  "fechas verificadas: marco regulatorio de IA del 19 de octubre, Oficina de IA del 29 de octubre, código de "
  "buenas prácticas de contenidos generados por IA del 19 de octubre. <b>Cero consultas de IA abiertas o "
  "cerradas en la ventana</b>; la única abierta es la de repositorios de anuncios del Reglamento de Servicios "
  "Digitales. <b>AESIA: cero elementos en la ventana</b>, su actualidad más reciente es del 20 de octubre, y su "
  "única aparición en el BOE es una resolución de personal; sus secciones internas de publicaciones, guías y "
  "estudios <b>devuelven páginas vacías</b> porque se renderizan en cliente. <b>Comité Europeo de Protección de "
  "Datos: cero documentos adoptados</b> con fecha en la ventana, el más reciente del 13 de octubre; una sola "
  "noticia, del 4 de noviembre, el lanzamiento de su centro de privacidad para menores; ningún plenario en la "
  "ventana; y una sola consulta abierta, barridas sus cinco páginas de listado. Corrección a un aviso de método "
  "heredado: <b>su listado de consultas sí separa ahora las abiertas en cabecera</b>; lo que sigue siendo cierto "
  "es que la paginación solo recorre las cerradas. Las directrices sobre rastreo web <b>siguen en versión 1 y "
  "sin texto final</b>, y no podía haberlo porque no hubo plenario. <b>Reglamento de Gobernanza de Datos:</b> "
  "cero actos nuevos. <b>Digital Omnibus:</b> cero movimiento en la ventana; su estado verificado es mandato de "
  "negociación del Consejo adoptado el 21 de octubre de 2026. <b>Parlamento Europeo:</b> ninguna sesión "
  "plenaria en la ventana y cinco comunicados, ninguno del ámbito. Y queda sin cubrir, por segunda edición "
  "consecutiva, el <b>Supervisor Europeo de Protección de Datos</b>, cuyo dominio devuelve denegación en las "
  "cuatro rutas probadas; lo único verificable es que su boletín más reciente es de marzo de 2026, de modo que "
  "no hubo boletín en la ventana, pero no se puede decir nada de sus comunicados ni dictámenes."),
 ("Fuentes que no se han podido alcanzar, y se declaran", "Lista completa, porque no alcanzar una fuente no es "
  "lo mismo que que no haya nada. Bloqueadas por cortafuegos, captcha o denegación: el <b>portal de avisos y "
  "guías del CCN-CERT</b>; el <b>Congreso</b> en ocho rutas, incluidos datos abiertos y boletines oficiales, y "
  "el <b>Senado</b>; el <b>Consejo de Estado</b> en su sitio propio; <b>une.org</b> en tres rutas; "
  "<b>iso.org</b>, suplido por el espejo del catálogo por comité, que es la misma ficha; <b>eur-lex</b>, "
  "suplido por el repositorio de la Oficina de Publicaciones, que es la misma base de datos y es acceso oficial "
  "y documentado, no evasión; el <b>Supervisor Europeo de Protección de Datos</b>; la <b>autoridad británica</b>, "
  "que sirve contenido de 2024 a clientes automatizados; el <b>equipo de respuesta belga</b> y el <b>listado de "
  "alertas del equipo italiano</b>; <b>Citrix</b>, cuya página es una cáscara de guion, de modo que las fechas "
  "de sus dos avisos del 3 de noviembre son del intermediario y no del fabricante y quedan <b>no "
  "confirmadas</b>; la <b>bitácora de días de parches de SAP</b>; la página de aviso de <b>Ivanti</b>; la "
  "página del aviso de <b>Fortinet</b>, con error de servidor; el <b>censo europeo de organismos notificados</b>, "
  "por exigir clave; la interfaz de programación de la <b>base nacional de vulnerabilidades</b>, que sirve un "
  "recurso provisional; el <b>registro de decisiones de infracción</b> de la Comisión en tres rutas; la base de "
  "resoluciones de la <b>autoridad polaca</b>; las rutas de comunicados de la <b>autoridad federal alemana</b> "
  "y de <b>cuatro autoridades de Land</b>; el <b>diario oficial catalán</b> para el documento de la circular de "
  "videovigilancia y su corrección de errores; la <b>sala de prensa de Danfoss</b>, aunque sí se ha leído su "
  "página de avisos de seguridad, que es el canal pertinente; los <b>canales propios de las cadenas de "
  "distribución</b> distintas de una, de modo que el barrido de canales propios queda incompleto; y el "
  "<b>registro público del Consejo de la Unión</b>, de modo que no se han podido barrer documentos del Consejo "
  "con fecha en la ventana. Y una limitación transversal que afecta a la datación: el <b>archivo histórico de "
  "internet está bloqueado</b> en este entorno, de modo que <b>no se puede datar de forma independiente la "
  "primera publicación</b> de ninguna página."),
 ("Prensa, agregadores y trampas de método", "Semana cargada, con tres patrones que se han repetido y que "
  "conviene tener en la cabeza, los tres documentados en los asuntos de esta edición. Uno, <b>la fecha del "
  "listado no es la fecha del documento</b>, y ha salido tres veces en tres sitios distintos: en ENISA, con las "
  "fechas de dos avisos técnicos <b>cruzadas entre sí</b> en el elemento temporal de cada página; en su propio "
  "listado, con el comunicado de PHP apareciendo con fecha de noviembre siendo de octubre; y en la dirección "
  "general de redes, con 98 páginas cambiando de fecha de modificación por una regeneración del sitio. Dos, <b>el "
  "estado abierto que no es una actualización</b>, con cinco casos medidos: la alerta francesa de refrigeración, "
  "con estado en curso y última versión del 16 de octubre; un aviso de virtualización con estado abierto y "
  "fechas del 27 y 28 de octubre; y tres revisiones de Siemens de las que una es cosmética y otra solo añade "
  "productos a la lista de no afectados. Tres, <b>la fecha del intermediario tomada por la del fabricante</b>, "
  "con desplazamientos medidos de nueve, veinte y hasta <b>ochenta y seis días</b>. Regla que ha funcionado "
  "todas las veces: ir al documento del emisor original y leer su propio historial de versiones, no el del que "
  "lo relaya. Y un cuarto patrón que conviene añadir al método, porque es nuevo esta semana y es el más "
  "peligroso: <b>un canal propio que sirve contenido viejo con apariencia de actual</b>, como el blog de una "
  "gran plataforma de criptoactivos, que devuelve publicaciones de 2019 con títulos casi idénticos a los de "
  "2026 por delante de las verdaderas. Y una corrección propia de este boletín, pequeña pero de las que delatan: al generar esta edición apareció un signo de porcentaje duplicado en la prosa de una ficha de incidentes de la edición 002, que llevaba desde agosto saliendo en la página con el signo repetido. Corregido <b>en la entrada</b>, que es donde se parchea, y no en la salida."),
]

counts = {k: 0 for k in SEC}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1
