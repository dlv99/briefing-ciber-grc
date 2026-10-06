# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Hoy el briefing tiene dos lectores confirmados y un tercero previsto:

- **El autor.** Lo usa como radar propio de normativa y plazos de ciberseguridad, gobernanza, riesgo y cumplimiento en España y la Unión Europea. Lee la edición completa el lunes, en escritorio, en una sesión larga: recorre pestañas, revisa el cuadro de plazos y se queda con lo que cambia su trabajo de las próximas semanas.
- **Un círculo de amigos.** Reciben el enlace directo. Mismo perfil de lectura: profesional, en español, interesado en el ámbito ciber-GRC español y europeo.
- **Lectores públicos (previsto, sin caracterizar).** El autor quiere expandir el alcance y abrir el sitio al público. Quién es ese lector exactamente (función, sector, antigüedad) **no está decidido** y el trabajo futuro no debe darlo por supuesto.

Modo de lectura confirmado: **escritorio, lectura larga**. No se ha confirmado que móvil, impresión o PDF sean usos reales, aunque el código actual los soporte.

## Product Purpose

Boletín semanal que publica cada lunes por la mañana el estado verificado de la regulación de ciberseguridad, gobernanza, riesgo y cumplimiento en España y la Unión Europea, cubriendo el periodo desde la edición anterior.

El producto existe para que su lector no pierda un plazo ni una norma, y para que pueda afirmar en una reunión algo concreto con la fuente detrás. Éxito es que cada fecha, cada plazo y cada incidente de la edición aguanten la comprobación contra su fuente primaria, y que lo que no se pudo comprobar aparezca dicho como tal.

## Positioning

**El método es el producto.** Lo que un boletín vecino no puede copiar sin hacer el mismo trabajo:

- Fuentes primarias siempre que han sido accesibles (EUR-Lex, ENISA, Supervisión Bancaria del BCE, JERS, EBA, ESMA, EIOPA, CEPD, CCN, BOE, Congreso de los Diputados, ISO, NIST), citadas con enlace.
- Cada plazo reverificado de forma independiente contra su fuente primaria en cada edición, no heredado de la edición anterior.
- Incidentes solo con confirmación de la entidad afectada, de un regulador o de un CERT oficial; lo descartado se lista aparte para que el lector sepa que existe y por qué no entró.
- Se publica el estado de un hecho a la hora en que se comprobó, distinguiendo lo anunciado de lo consumado.
- Las limitaciones de acceso se declaran (hay fuentes que bloquean el acceso automatizado), y los asuntos afectados llevan advertencia explícita.
- Las previsiones propias van etiquetadas como propias, con fecha de revisión, y dan horizontes en lugar de fechas inventadas.
- Sección de bulos: afirmaciones circulantes que conviene desmontar, con la comprobación que permite afirmar lo contrario.

La credibilidad viene del método y de las fuentes, no de una firma. Esa es una decisión deliberada del autor, no una carencia.

## Operating Context

- **Cadencia.** Una edición por lunes. El periodo cubierto se declara en cada edición y puede ser mayor que una semana cuando ha habido pausa (la 004 cubrió tres).
- **Producción.** Una tarea programada investiga el periodo, verifica, descarga `_gen/` entero como plantilla, reescribe solo los ficheros de contenido y vuelve a ejecutar `web.py`. La plantilla se conserva idéntica semana a semana en lugar de reconstruirse de memoria, porque reconstruirla la degrada.
- **Sin memoria entre ejecuciones.** Cada ejecución arranca de cero, así que `ediciones.json` es el manifiesto del histórico: la tarea lo lee para reconstruir el archivo.
- **Publicación.** Todo lo que llega a `main` se despliega en Cloudflare Pages en uno o dos minutos. Las ramas distintas de `main` generan previsualización con URL propia sin tocar producción. `_gen/` no se publica.
- **Estructura del sitio.** `index.html` es la última edición; `ed-AAAA-MM-DD.html` es el permalink de cada una; el archivo histórico vive dentro de la propia página.
- **Superficies dentro de una edición.** Portada, Plazos, seis ámbitos temáticos (España, Unión Europea, Financiero, Normas, IA y datos, Amenaza), Incidentes, Mapa UE de transposición, Glosario, Correcciones y Archivo. Además: buscador dentro de la edición, filtros de incidentes por sector y tipo, enlace copiable por asunto, siglas desplegadas con glosario largo.
- **Idioma.** Español de España, en todo el producto.

## Capabilities and Constraints

**Técnicas**

- Sitio estático sin backend y sin framework de construcción: un generador en Python escribe HTML con CSS y JavaScript en línea. No hay paso de empaquetado ni dependencias de npm.
- CSP estricta en `_headers`: solo origen propio, con estilos y scripts en línea permitidos, tipografías de Google Fonts, e imágenes propias, `data:` y `flagcdn.com`. Cualquier origen nuevo exige editar esa cabecera a conciencia.
- Hoy el sitio lleva `noindex,nofollow` y es accesible solo con el enlace.
- El comando de build de Cloudflare copia a `dist/` solo los HTML, los JSON, `robots.txt` y `_headers`; cualquier tipo de fichero nuevo (imágenes, `_redirects`) hay que añadirlo ahí o no se sirve.

**Reglas del generador que no se pueden romper** (documentadas en `_gen/LEEME.md`, algunas comprobadas en tiempo de generación)

1. Nada de guiones largos ni medios en el texto: `web.py` lo comprueba y aborta.
2. Las cifras se calculan contando, nunca se escriben a mano.
3. Incidentes: solo lo confirmado.
4. Nada de dobles signos de porcentaje en el texto; se escribe el símbolo una sola vez.
5. `counts` se inicializa con todos los ámbitos a cero: una semana sin nada en un ámbito es un resultado válido y no debe romper la plantilla.
6. `web.py`, `silabas.py` y `geo.json` no los toca la tarea semanal. El contenido vive en `contenido.py`, `incidentes.py`, `mapa.py`, `siglas.py` y `glosario.py`. Si vuelve a aparecer contenido de una edición dentro de `web.py`, es un error.

**Terminología propia** (es vocabulario del producto, no etiquetas de maqueta): ámbitos (`es`, `eu`, `fin`, `std`, `ai`, `thr`), asuntos, plazos vivos, bulos, «comprobado y sin novedad», previsión propia, lagunas, descartados.

**Decisiones abiertas**

- **Apertura al público.** Confirmado como objetivo: el sitio debe dejar de ser privado y pasar a ser indexable y presentable a desconocidos. No hay fecha ni condición definida para el cambio.
- **Entrada para quien llega de cero.** La versión pública necesita que un desconocido entienda qué es esto: qué cubre, con qué método y cada cuánto sale. Hoy no existe esa superficie.
- **Vía de contacto y corrección.** La versión pública necesita una forma de escribir, señalar un error o aportar una fuente. Hoy no existe.
- **Versión correo y suscripción: fuera de alcance por ahora.** El docstring de `contenido.py` menciona una versión apta para Gmail y Outlook; no es un objetivo confirmado. No hay captura de correo ni proveedor de envío, y no se debe diseñar como si los hubiera.

## Brand Commitments

- **Nombre.** «Briefing Ciber-GRC», con «España y Unión Europea» como bajada. Cada edición se numera a tres cifras (Edición 007) y se fecha en largo.
- **Sin firma visible, deliberadamente.** No hay autor, seudónimo ni entidad que firme, y el trabajo futuro no debe añadir ninguno: el método y las fuentes son la credibilidad.
- **Voz.** Sobria, declarativa, específica. Dice la hora a la que comprobó un hecho, separa lo anunciado de lo consumado, traduce la norma a consecuencia concreta para el lector y nombra lo que no pudo comprobar. Nada de entusiasmo de boletín ni de lenguaje promocional.
- **Sin guiones largos ni medios**, también como norma de estilo y no solo como comprobación del generador.

## Evidence on Hand

- **Siete ediciones publicadas**, de la 001 (13 de agosto de 2026) a la 007 (5 de octubre de 2026), en `ed-2026-*.html`, con su contenido real verificado y sus enlaces a fuente primaria.
- **`ediciones.json`**: manifiesto del histórico con número, fecha, titular, entradilla, periodo y recuento de asuntos y plazos de cada edición.
- **`_gen/`**: generador completo y documentado (`_gen/LEEME.md`), con el historial de correcciones de reglas rotas.
- **Declaración de método y de limitaciones de acceso** al pie de cada edición.

Lo que **no** existe y no se debe fabricar: testimonios, citas de lectores, cifras de suscriptores o de audiencia, logotipos, fotografía, cartera de clientes, premios, menciones de prensa y cualquier reconocimiento institucional. Tampoco hay autor al que atribuir nada.

## Product Principles

1. **Lo comprobado y lo no comprobado se distinguen siempre.** Antes que parecer completo, el producto prefiere decir qué no pudo verificar y por qué.
2. **Un hecho sin fuente primaria enlazada no es un hecho publicable.** El enlace es parte del contenido, no una cortesía.
3. **La plantilla se conserva, no se reinventa.** La repetición semana a semana es lo que impide que el producto se degrade; el cambio de maqueta es una decisión aparte y deliberada.
4. **Cada asunto termina en consecuencia para el lector.** Qué cambia, por qué importa y qué leer; nunca resumen de boletín oficial por el resumen.
5. **Una semana vacía en un ámbito es información.** El silencio se publica como silencio comprobado, no se rellena.
