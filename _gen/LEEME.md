# Generador del briefing

Este directorio es **la plantilla del sitio**. La tarea de los lunes lo descarga entero,
reescribe solo los ficheros de contenido y vuelve a ejecutar `web.py`. Así la maqueta se
conserva idéntica semana a semana en lugar de reconstruirse de memoria, que es lo que
haría que fuese degradándose.

## Qué se reescribe cada semana

| Fichero | Frecuencia | Qué contiene |
|---|---|---|
| `contenido.py` | **Cada lunes, entero** | `NUM`, `FECHA_ISO`, `FECHA_TXT`, `PERIODO`, titular, entradilla, claves, plazos, `TITS` (titulares de las tarjetas de portada), asuntos, correcciones y «comprobado y sin novedad» |
| `incidentes.py` | **Cada lunes, entero** | Incidentes confirmados, descartados y lagunas. Cada incidente lleva `conf`, la fecha de confirmación pública en `AAAA-MM-DD`: es obligatoria |
| `mapa.py` | Cada lunes, al menos la previsión | Estado de las 5 normas en los 27 Estados y previsión de los que no tienen ley |
| `siglas.py` | Al añadir siglas nuevas | Despliegue de siglas |
| `glosario.py` | Al añadir siglas nuevas | Explicaciones largas del glosario |

## Qué NO se toca nunca

`web.py` (la plantilla), `silabas.py` (partición de palabras), `geo.json` (geometría del
mapa) y `contador.py` (fechas ancla y cuantías verificadas del incumplimiento de
transposición: solo se toca si cambia un hecho verificado, como una sentencia o un
número de asunto nuevo).

«No se toca» quiere decir **no metas contenido de la edición ahí dentro**. Mejorar la
maqueta sí es tocar `web.py`, y es legítimo: para eso existe. Lo que nunca entra en
`web.py` es una fecha, un titular ni un dato de la semana.

> **Corregido el 17/08/2026.** `web.py` tenía incrustados la fecha, el número de edición,
> el periodo y los titulares de las tarjetas de portada de la edición 001. Ahora los lee
> de `contenido.py`. Si vuelve a aparecer contenido de una edición dentro de `web.py`,
> es un error: sácalo a `contenido.py`.

## Cómo se ejecuta

```
cd _gen && SALIDA=/ruta/de/salida python3 web.py
```

Escribe `index.html` y `ed-AAAA-MM-DD.html`. Lee `geo.json` de su propio directorio y
`ediciones.json` del directorio de salida para reconstruir el archivo histórico, así que
descárgalo antes desde el repositorio.

## Reglas que no se pueden romper

1. **Nada de guiones largos ni medios.** `web.py` lo comprueba y aborta si aparece alguno.
2. **Las cifras se calculan**, nunca se escriben a mano. El total de asuntos sale de contar.
3. **Incidentes: solo lo confirmado** por la entidad afectada, un regulador o un CERT oficial.
4. **No uses `%%` en el texto.** Solo el campo «qué leer» de `contenido.py` convierte `%%` en `%`;
   en el resto sale tal cual. Escribe `%` directamente. (Corregido el 17/08/2026: la edición 001
   se publicó con «2 %%» visible en tres incidentes.)
5. **`counts` se inicializa con todos los ámbitos a cero**, para que una sección vacía no rompa
   la plantilla. Una semana sin nada en un ámbito es un resultado válido.

## Previsión de transposición en el mapa (añadido el 22/09/2026)

Cada Estado **sin ley en vigor de NIS2 o de CER** lleva al final de su nota en `mapa.py` un bloque
con tres ladillos: «¿Cuándo se espera?», «Qué lo movería» y «Qué vigilar», cerrado con
«Previsión propia, revisada el DD de mes de AAAA». La nota de cada una de las dos normas lleva
además «¿Quién llega antes?». Se revisa **cada lunes**:

1. Fuentes que hay que mirar: el cuadro de plazos de enmiendas del Congreso (se actualiza varias
   veces por semana), el orden del día de la comisión competente, el BOCG, la referencia del Consejo
   de Ministros de cada martes y el Plan Anual Normativo. Fuera de España, el orden del día del
   parlamento de cada país. Ojo: el BOE no anuncia lo que va a salir; las señales previas están en
   las Cortes, el Consejo de Ministros y el Plan Anual Normativo.
2. Da horizontes, no fechas inventadas: «este trimestre», «primer semestre de 2027», «más tarde»,
   y di qué lo descarta a corto plazo (por ejemplo, que ni siquiera haya pasado por el Consejo de
   Ministros). Menciona siempre la vía rápida si existe, como un real decreto-ley.
3. Si nada cambió, actualiza solo la fecha de revisión. Si un Estado aprueba su ley, el bloque se
   sustituye por la fecha de entrada en vigor y se cuenta como asunto de la semana.

> **Aviso del 22/09/2026.** El generador con el que se publicó la edición 004 no llegó al
> repositorio. `mapa.py` se reconstruyó a partir de la página publicada de esa edición, pero la
> pestaña Cronología y la capa de procedimiento de infracción de aquel mapa no existen en este
> `web.py`. Si aparece aquel `_gen`, hay que subirlo.

## Bloque fijo de seguimiento del incumplimiento (añadido el 12/10/2026)

Desde la edición 009 el briefing lleva **un asunto fijo en la sección «es»** con el
contador de incumplimiento de transposición de CER y de NIS2. No es un asunto de la
semana: va siempre, aunque no se haya movido nada, porque la cifra sube sola cada día
y es el mejor argumento disponible para explicar a un cliente por qué un real
decreto-ley es probable.

**Las cifras NO se escriben a mano.** Se calculan con `_gen/contador.py`, que es
plantilla y **no se toca** salvo que cambie un hecho verificado (una sentencia, un
número de asunto nuevo, una transposición). En `contenido.py`:

```python
from contador import CER, NIS2, dias, tanto_alzado, eur, millones, resumen
R = resumen()                     # a día de la edición
R["cer"]["tanto_alzado_eur"]      # '24.743.670'
R["cer"]["tanto_alzado_millones"] # '24,7'
R["cer"]["dias"]                  # 725
```

Qué tiene que decir el asunto, cada lunes:

1. **La cifra acumulada de CER a día de hoy** y los días transcurridos desde el
   18 de octubre de 2024. Siempre con la salvedad de que es **lo pedido por la
   Comisión**, no impuesto: solo el Tribunal fija el importe final y puede reducirlo.
2. **Que el contador del tanto alzado se detiene al transponer**, no al dictarse
   sentencia. Es lo que convierte el dato en incentivo y no en anécdota.
3. **El delta de la semana**, que son siete días por el importe diario: 238.904,40
   euros. Calcúlalo, no lo copies de aquí.
4. **El estado de NIS2 sin inventar cuantías.** `NIS2["asunto"]` y `NIS2["diario"]`
   valen `None` a propósito: la remisión se decidió el 8 de julio de 2026 pero no hay
   número de asunto ni importes públicos. Si algún lunes aparecen, se rellenan en
   `contador.py` y **eso es asunto propio de portada**, no una línea más.
5. **La previsión de entrada en vigor**, coherente con las notas del mapa: por ley
   ordinaria no antes del segundo semestre de 2027 y con 2028 como caso central;
   por real decreto-ley, primer semestre de 2027 si hay gobierno en enero o febrero.
   Horizontes, no fechas inventadas.

Dos cosas que hay que revisar cada lunes antes de dar el bloque por bueno:

- **¿Hay ya número de asunto de NIS2?** Barrer los avisos de «recurso interpuesto»
  de 2026 en el DOUE serie C y comprobar si alguno cita la Directiva 2022/2555. El
  desfase medido entre interposición y publicación es de seis a ocho semanas.
- **¿Hay sentencia en C-616/26?** Si la hay, el tanto alzado se congela en la fecha
  que fije el Tribunal y arranca la multa coercitiva de 183.781,44 euros diarios.
  Ese día el bloque cambia de naturaleza y `contador.py` necesita una fecha de cierre.

Si España transpone, por ley o por decreto-ley, el bloque **no desaparece**: pasa a
decir cuánto se acumuló hasta la fecha de notificación a la Comisión, que es lo que
seguirá pidiéndose como tanto alzado.

## Filtros de la sección de incidentes (añadido el 19/10/2026)

La sección de incidentes lleva un panel de filtros con tres controles, y los tres se
construyen solos a partir de los datos de `incidentes.py`:

1. **Sector y Tipo**, cada uno en su propio desplegable, con casillas, icono de color e
   indicador del número de incidentes. Son de **selección múltiple**: marcar «Banca y
   seguros» y «Sanidad» muestra los de los dos. Dentro de un grupo la condición es «o»;
   entre los dos grupos, «y». Ninguna casilla marcada equivale a todas. Solo aparecen las
   opciones con al menos un incidente.
2. **Fecha de confirmación**, en un tercer desplegable, con cuatro atajos («Esta edición»,
   «Últimos 30 días», «Últimos 90 días» y «Todo») y dos campos de calendario para un rango
   a medida.
   Los atajos se calculan **desde `FECHA_ISO` de la edición, no desde el día en que se
   lee la página**: así una edición archivada sigue diciendo lo mismo dentro de un año.
   La aritmética de fechas va en UTC a propósito; con horas locales, un lector al este
   de Greenwich veía el rango desplazado un día.
3. **Contador y botón de limpiar**, que aparecen y se actualizan solos.

### El campo `conf`, y por qué el generador aborta sin él

Cada incidente lleva una fecha de confirmación pública legible por máquina:

```python
("cpr", "Registro central de personas de Dinamarca", "Dinamarca", "adm",
 ["acc","rgpd","sum"],
 "Accesos durante unos diez días de septiembre; actividad irregular detectada el 2 de octubre...",
 "2026-10-05",          # <- conf: AAAA-MM-DD, obligatoria
 "Abierto, con revisión de seguridad ordenada por el ministerio", ...)
```

`conf` es **la fecha en que la entidad afectada, el regulador o el CERT lo confirmaron**,
que es justamente la que exige la regla de admisión del boletín: si un incidente entra,
esa fecha existe. No es la fecha del ataque ni la de la detección, que muchas veces no se
declaran o son un rango de días.

El campo largo de texto se mantiene y es donde va la cronología completa en prosa, que es
lo que se lee. `conf` solo alimenta el filtro y la línea «confirmado el …».

`web.py` **aborta** si falta o no es una fecha válida, igual que aborta con un guion largo.
Es deliberado: se parchea la entrada, no la salida. Un filtro de fechas que silenciosamente
se come los incidentes sin fecha es peor que un generador que no compila.

## El recuento de plazos vivos (corregido el 19/10/2026)

La línea de datos de la portada y la del archivo dicen «N plazos vivos». Hasta la edición 008
ese número era `len(PLAZOS)`, es decir **todos** los plazos, incluidos los marcados como lejanos.
Desde la edición 009 cuenta solo los que llevan el indicador de vivo, con `VIVOS` calculado en
`web.py`. Las entradas de `ediciones.json` anteriores a la 009 conservan el número antiguo, que
era el total: no se han reescrito porque no se pueden reverificar sus plazos a posteriori.

## Pendiente para la edición 010 o posterior (anotado el 20/10/2026)

Tres cosas detectadas al revisar el mapa después de publicar la 009. Las dos primeras son de datos
y le tocan a la tarea del lunes. La tercera es un cambio de diseño y **no se hace sin que David lo
confirme**.

### 1. La nota de España en el Reglamento de IA está desactualizada (hacer)

`mapa.py`, entrada `ES` de `ia`, dice: «AESIA designada y notificada, pero la ley orgánica que le da
competencias formales sigue pendiente». **Ya no está pendiente: está caducada** desde el 6 de octubre
de 2026, porque el expediente 121/000096 figura «Concluido - (Caducado)» en el Congreso. Pendiente y
caducada no son lo mismo y el matiz importa: pendiente sugiere que avanza. Reescribir la nota.

### 2. El mapa del CRA se contradice con su propia nota (verificar y luego hacer)

El reparto por país del CRA es de 25 Estados en `desc`, «sin dato público», con la explicación de que
ni la Comisión ni ENISA publican designaciones por país. Pero **la nota de esa misma norma enumera
quince Estados con autoridad notificante registrada**, con nombre: Bélgica, Chipre, Alemania, Estonia,
Finlandia, Francia, Croacia, Hungría, Irlanda, Lituania con dos, Malta, Países Bajos, Polonia, Suecia
y Eslovaquia. España no está. El mapa dice «no sabemos» encima de un texto que sí sabe.

Antes de tocarlo, **reverificar los quince contra el censo europeo**, porque el dato es del 12 de
octubre. Después, ponerlos en `parcial` con la nota de que tienen autoridad notificante pero no
organismos notificados, y dejar en `desc` solo a los que de verdad no tengan dato.

Aviso de método: la consulta al censo que sí funciona es la API de búsqueda que usa el propio
frontal, con los índices `nando_legislation` y `nando_notification`, filtrando por el identificador
de legislación. Y hay que hacer **prueba de control** con otra legislación que devuelva una cifra
distinta de cero, porque un campo mal puesto da ceros falsos.

### 3. Dos escalas de color en lugar de una (decisión de David, no hacer por iniciativa propia)

El mapa usa los mismos cinco estados para las cinco normas, y eso hace que el verde signifique cosas
distintas según la pestaña sin que nada lo avise:

- En **directivas** (NIS2, CER) el verde es «hay ley nacional en vigor que ya obliga a las empresas».
- En **reglamentos** (DORA, IA, CRA) el verde es «el Estado ha designado autoridades», que no obliga
  a nadie a nada nuevo porque la norma ya obligaba igual.

Hay además una asimetría escondida: **el rojo, «sin ley y demandado», solo puede darse en una
directiva**. Por eso DORA e IA no tienen ni un país en rojo aunque España tenga carta de
emplazamiento viva por DORA desde julio de 2026.

La propuesta, pendiente de confirmación: mantener los cinco colores y la misma paleta, pero que
cambie **qué pregunta responde el color**, con una línea fija encima del mapa que lo diga.

- Directivas, la pregunta es **«¿te obliga ya?»**: verde, ley en vigor; amarillo, aprobada pero no
  aplicable aún o solo en parte; naranja, sin ley; rojo, sin ley y demandado.
- Reglamentos, la pregunta es **«¿quién te vigila y quién te sanciona?»**: verde, autoridades
  designadas y régimen sancionador nacional en vigor; amarillo, autoridad designada sin régimen
  sancionador; naranja, sin designar; gris, sin dato público.

Lo que esto haría visible y hoy no se ve: **España saldría amarilla en IA y amarilla en DORA por
exactamente la misma razón**, que la autoridad existe y el régimen sancionador no. Hoy DORA la pinta
verde y la coincidencia se pierde. Es un patrón español que se repite en tres normas seguidas.

### 4. Un plazo que puede faltar en la tabla (verificar)

La nota del CRA afirma que **el plazo para que los Estados tengan organismos notificados suficientes
es el 11 de diciembre de 2026**. Si es correcto, es un plazo vivo y no entró en la tabla de la
edición 009. **Verificar contra el articulado del Reglamento (UE) 2024/2847 antes de publicarlo**, no
darlo por bueno desde esta nota.

### Trampa de nombres de clase (aprendida el 20/10/2026)

Los filtros se rehicieron como tres desplegables en fila. La barra que los contiene se llama
`.fbar`, **y no `.barra`**, porque esa clase ya existía en `web.py` para la barra de leyenda
del mapa, con `height:13px` y `overflow:hidden`. Al coincidir el nombre, la regla del mapa, que
va después, ganaba: la barra de filtros quedaba aplastada a trece píxeles y, peor, el
`overflow:hidden` **recortaba el panel desplegable**, que se abría vacío.

El síntoma era desconcertante porque el panel existía, tenía sus cinco opciones y el navegador
lo daba por visible: simplemente no se pintaba. Lo que lo localizó fue preguntarle al navegador
`elementFromPoint` sobre el centro del panel, que devolvía la tarjeta de incidente de debajo, y
después recorrer los ancestros buscando quién creaba recorte o contexto de apilamiento.

**Antes de añadir una clase a `web.py`, comprueba que no existe ya**: la hoja de estilos es una
sola y la última regla gana.
