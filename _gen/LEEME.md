# Generador del briefing

Este directorio es **la plantilla del sitio**. La tarea de los lunes lo descarga entero,
reescribe solo los ficheros de contenido y vuelve a ejecutar `web.py`. Así la maqueta se
conserva idéntica semana a semana en lugar de reconstruirse de memoria, que es lo que
haría que fuese degradándose.

## Qué se reescribe cada semana

| Fichero | Frecuencia | Qué contiene |
|---|---|---|
| `contenido.py` | **Cada lunes, entero** | `NUM`, `FECHA_ISO`, `FECHA_TXT`, `PERIODO`, titular, entradilla, claves, plazos, `TITS` (titulares de las tarjetas de portada), asuntos, correcciones y «comprobado y sin novedad» |
| `banco.json` | **Cada lunes, SE AÑADE, nunca se vacía** | El registro acumulado de incidentes. Se añaden incidentes nuevos y se añaden entradas al campo `act` de los que ya estaban. Vaciarlo o reescribir entradas antiguas destruye el histórico |
| `incidentes.py` | Cada lunes, solo `BULOS` y `LAGUNAS` | Taxonomías, cargador y validador del banco, más los bulos y las lagunas de la semana. Las taxonomías solo cambian al añadir un sector, un tipo o un vector nuevos |
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
3. **Incidentes: entra todo, con etiqueta.** Desde el 03/11/2026 la confirmación oficial ya
   no es una puerta sino una etiqueta, y van dos: una para el hecho y otra para la causa.
   Lo estricto se mantiene solo en el campo de obligaciones. Ver la sección del registro.
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

## El registro de incidentes (rehecho el 03/11/2026, lee esto antes de tocarlo)

Hasta la edición 011 la sección de incidentes era **una foto semanal**: `incidentes.py` se
reescribía entero cada lunes y lo de la semana anterior desaparecía. Desde la 012 es un
**registro acumulado y vivo** que persiste en `_gen/banco.json`.

### Por qué cambió, que es lo que no hay que olvidar

David lo planteó el 2 y el 3 de noviembre de 2026, y tenía razón. El boletín existe para que
no le pillen desprevenido delante de un cliente, y dos casos demostraron que el diseño
trabajaba en contra:

1. **El robo a Binance** (6.300 millones de dólares, el mayor de la historia) no entró en la
   edición 011 en su primera versión.
2. **La campaña contra controladores de refrigeración** se seguía como amenaza y no como
   incidente, y cuando se materializó no se podía enlazar con sus capítulos anteriores.

Al migrar los 26 descartados de la 011 apareció el motivo de fondo, y **no era la regla de
admisión** como se creyó al principio: **era la ventana de una semana**. En la papelera había
una brecha de datos médicos de **diecinueve millones de personas en Polonia**, descartada por
«fuera de ventana»; hospitales belgas con cirugías canceladas, descartados por ser de febrero;
y un caso de Ellwangen anotado como «instructivo, porque documenta expresamente la notificación
al responsable de protección de datos del Land y el aviso a la aseguradora de ciberriesgo»,
tirado por ser de 2025.

Una historia que se desarrolla a lo largo de meses **no se podía contar nunca**: cada lunes
estaba o demasiado vieja o todavía sin confirmar. El caso de la refrigeración lo ilustra
entero: agosto de 2026, economatos de siete bases militares de Estados Unidos, con el hecho
confirmado por el Departamento de Defensa y la causa sin determinar; octubre, distribución
francesa; noviembre, resto de Europa.

### Las cuatro decisiones de David del 03/11/2026

1. **Alcance mundial con umbral**: todo lo de España y la UE, y del resto del mundo lo que
   tenga cifra grande, sector crítico, técnica novedosa o víctima reconocible.
2. **Dos niveles de presentación**: entre cinco y ocho fichas desarrolladas y el resto en tabla
   larga filtrable.
3. **Cifras con etiqueta de origen**, siempre publicadas, nunca sin procedencia.
4. **Cambio completo en la edición 012**, no por fases.

### El contrato de datos

Cada incidente de `banco.json` es un objeto con estas claves. `_gen/incidentes.py` las valida
al importar y **aborta** ante cualquiera que esté mal: se parchea la entrada, no la salida.

| Clave | Qué es |
|---|---|
| `id` | Identificador único y estable. Es lo que permite actualizar un incidente en ediciones posteriores |
| `ent`, `pais`, `sec` | Entidad, país y clave de `SECTORES` |
| `tips` | Lista de claves de `TIPOS`, al menos una |
| `vec` | Lista de claves de `VECTORES`, al menos una. **Si no se conoce va `["desc"]`**, que no es lo mismo que vacío. NO se infiere |
| `hecho` | Nivel de confirmación **del hecho**: `oficial`, `proveedor`, `prensa` o `atribuido` |
| `causa` | Nivel de confirmación **de la causa**: los mismos más `desconocida` |
| `cifra`, `cifra_org` | Importe y su procedencia. Una sin la otra aborta |
| `afec`, `afec_org` | Personas o entidades afectadas y su procedencia. Idem |
| `conf` | `AAAA-MM-DD` en que se conoció públicamente. Alimenta el filtro de fechas |
| `ed` | Número de edición en la que entró |
| `detalle` | `ficha` o `tabla`. Si es `ficha`, los campos de prosa son obligatorios |
| `estado`, `fecha`, `sabe`, `quien`, `obl`, `lec` | La prosa de siempre. Solo obligatoria en las fichas |
| `url` | **Obligatoria siempre**, también en las filas de tabla. David la pidió expresamente |
| `act` | Lista de actualizaciones `{ed, fecha, nota}`. Es lo que convierte el registro en vivo |

### Hecho y causa son dos campos, y es lo más importante de todo esto

Confundirlos fue el error de fondo. El caso que lo explica: en agosto de 2026 el Departamento
de Defensa de Estados Unidos confirmó por escrito «a possible refrigeration disruption at some
Defense Commissary Agency commissaries» y Fort Huachuca publicó en su propio canal que «ALL
freezers went into defrost mode, ALL frozen food has spoiled». **Hecho oficial.** La causa no
la sostuvo nadie hasta que Reuters publicó el 29 de octubre, con cuatro funcionarios, que el
Pentágono la trataba como presunto ciberataque. **Causa, prensa.** Con un solo campo esa
entrada no se podía escribir, y era la mejor entrada posible: habría hecho legible en agosto
todo lo que pasó en octubre.

El nivel `proveedor` se añadió el mismo día porque hacía falta: Danfoss y Copeland no son la
entidad afectada ni una autoridad, pero son quienes más detalle técnico dieron.

### Lo estricto se mantiene en un sitio

En el campo `obl`, el de obligaciones. Ahí no se afirma que algo dispara un plazo de
notificación sobre una noticia de prensa, porque es donde un cliente actúa. En el resto del
registro, etiquetar; en obligaciones, rigor.

### BULOS ya no es la papelera

`BULOS`, en `incidentes.py`, es **solo** lo comprobado y desmentido y las trampas de fecha que
circulan como actuales. Lo no confirmado ya no se tira: entra al banco con su etiqueta.

### Los filtros de la web

Cinco desplegables, todos construidos solos a partir de los datos: **Sector**, **Tipo**,
**Vector**, **Confirmación** (por el nivel del hecho) y **Fecha**. Los cuatro primeros son de
selección múltiple; dentro de un grupo la condición es «o», entre grupos «y»; ninguna casilla
marcada equivale a todas; solo aparecen las opciones con al menos un incidente.

El desplegable de fecha tiene «Esta edición», «Últimos 30 días», «Últimos 90 días», «Todo el
histórico» y un intervalo a medida. **«Esta edición» filtra por el campo `ed`, no por una
ventana de siete días.** Se probó con fechas y escondía incidentes de la propia edición, porque
un caso puede conocerse semanas antes de que entre al boletín. Un incidente aparece en «esta
edición» si entró en ella **o si se actualizó en ella**, que es lo que hace visible el
seguimiento. Los atajos de 30 y 90 días sí se calculan desde `FECHA_ISO` de la edición y no
desde el día en que se lee la página, en UTC a propósito.

**Fichas y filas de la tabla obedecen al mismo filtro**, y la fila de historial (`tr.det`) se
oculta con la suya. Si se rompe esa sincronización el contador miente y el lector cree que un
incidente no está, que es exactamente el problema que todo esto venía a resolver.

### Cola de reingreso al banco (pendiente)

Al reclasificar los 26 descartados de la edición 011, cuatro pasaron a `BULOS` y **veintidós
quedaron pendientes de reingreso**. Ya no se caen por antigüedad, pero necesitan sus metadatos
y, sobre todo, su enlace, que la nota de descarte no conserva. Hay que reingresarlos con
investigación, no de memoria. Los de más valor:

- Brecha de datos médicos de cerca de diecinueve millones de personas en Polonia (confirmada
  por la empresa el 13/08/2026, inspección de la autoridad polaca ese mismo día).
- Ciberataque a hospitales belgas con cancelación de cirugías (febrero de 2026).
- Exposición de datos vinculados a los servicios de información portugueses (08/10/2026,
  reivindicado sin confirmar: entra con `hecho: "atribuido"`).
- Acceso no autorizado y copia de base de datos en un proveedor polaco de facturación
  (27 y 28/09/2026, bien documentado).
- Ciberataque a la administración municipal de Ellwangen (mayo de 2025), por documentar la
  notificación al delegado de protección de datos **y** el aviso a la aseguradora.
- Sanción de la CNIL de siete millones de euros a FNAC y multa de la AEPD a una mutua: entran
  como `judicial` o `regulador` en el origen de la cifra.

Y dos del hilo de la refrigeración que **no se dieron de alta por no tener fecha o enlace
verificados**, y que no se inventan:

- Supermercados en Rusia e Israel atacados en 2022 con controladores de frío obsoletos, que
  Danfoss cuenta en su propia web. Falta la fecha exacta de publicación.
- Planta cárnica en Estados Unidos, 2024, con más de 900 kilos de carne perdidos: la fiscalía
  federal de Los Ángeles acusó a una persona en diciembre de 2025. Hay actuaciones judiciales,
  o sea fuente primaria, pero falta localizar el documento.

## El recuento de plazos vivos (corregido el 19/10/2026)

La línea de datos de la portada y la del archivo dicen «N plazos vivos». Hasta la edición 008
ese número era `len(PLAZOS)`, es decir **todos** los plazos, incluidos los marcados como lejanos.
Desde la edición 009 cuenta solo los que llevan el indicador de vivo, con `VIVOS` calculado en
`web.py`. Las entradas de `ediciones.json` anteriores a la 009 conservan el número antiguo, que
era el total: no se han reescrito porque no se pueden reverificar sus plazos a posteriori.

## Pendiente para la edición 012 o posterior (actualizado el 03/11/2026)

### 0. Encargo de David del 02/11/2026: los ataques a la refrigeración de supermercados (prioritario)

David mandó una noticia de prensa sobre ciberataques a sistemas de frío de la distribución
alimentaria diciendo «es super clave». Se investigó el 03/11/2026 y **el dosier completo está en
el proyecto, en `banco-incidentes/refrigeracion-distribucion-2026.md`**. Resumen de lo que hay
que hacer y de las trampas:

- **Confirmado oficialmente en su núcleo estrecho**: incidentes en controladores de
  refrigeración de la distribución alimentaria, confirmados por **CERT-FR** (ALE-012, 12 a 16 oct),
  **CERT-SE y NCSC Suecia** (02/11/2026 17:40 y 17:39) y **NCSC-NL** (02/11/2026), y por
  **Delhaize en su propia web** (02/11/2026 14:00). Esa última es la que habilita la admisión.
- **Entra con etiqueta de prensa, no como hecho confirmado**: el recuento de países (oscila entre
  siete y nueve), el recuento de cadenas y tiendas, y **todas las cifras de pérdidas millonarias**.
  La única cifra monetaria verificada en toda la cobertura son 15.000 euros de carne en una
  carnicería belga, a Reuters. La premisa de «pérdidas millonarias» no la sostiene nadie.
- **Trampa de fecha ya detectada en la 010 y que sigue viva**: la ALE-012 figura como «Alerte en
  cours» con `closed_at: null`, pero su última versión es del **16 de octubre**. Abierta no es
  actualizada. Comprobar cada lunes si por fin se ha movido.
- **La alerta no cita ningún CVE**: `cves` y `vendor_advisories` vacíos en el JSON y «Risque: non
  spécifié par l'éditeur». **No vincular la campaña a los CVE de Danfoss de 2025 ni de 2023.**
- **Danfoss no ha publicado nada propio** sobre esta campaña, y **no existe ningún aviso de Danfoss
  para la serie AK-SC**, que es uno de los cuatro productos que nombra CERT-FR.
- **Copeland y Dixell sí**: boletín de 14/10/2026, alojado en el dominio del distribuidor francés,
  que admite la vulnerabilidad en XWEB EVO **sin CVE y sin parche** (la remediación es migrar) y
  que **publica las credenciales de fábrica Admin/Admin para toda la gama**. Documento de dos
  capas: la fecha del boletín original de Copeland no consta más allá de «octubre de 2026».
- **Delhaize dice «IT-incident», no «ciberataque»**, no da número de tiendas y no menciona
  pérdidas ni seguridad alimentaria. Y su misma página de preguntas frecuentes **separa dos
  incidentes distintos**: el de servicios de TI del 11/10/2026 y el de refrigeración del
  02/11/2026. No confundirlos.
- **El ángulo regulatorio corrige una premisa del encargo y es el titular**: el anexo II.4 de NIS2
  exige **distribución al por mayor o producción y transformación industriales**, de modo que una
  tienda minorista **no encaja en el literal**; entra por plataformas logísticas, producción propia
  o designación nacional del artículo 2.2.c) por salud pública. Al estar en el anexo II y no en el
  I, una cadena es **entidad importante y no esencial** (artículo 3.2), con multas del 34.5 (7
  millones o 1,4 %) y no del 34.4. Y el anexo de CER dice **«exclusivamente»** mayorista y
  logística, así que el minorista queda **fuera de CER**. El gancho real es el artículo 21.2.d) y
  **21.3** de cadena de suministro, porque los controladores los gestiona por telemetría un
  frigorista externo, más el aviso de CERT-FR de que **cortar el envío de datos al frigorista puede
  romper condiciones del seguro**.
- **Lagunas que hay que cerrar**: el aviso del CCB belga **existe** (título indexado) pero el
  dominio da 403 de Akamai, así que **no citarlo con fecha**; la página de avisos del INCIBE-CERT
  que cubre **del 16 al 20 de octubre** devolvió 404 en cinco intentos y el listado **no tiene
  nada posterior al 30 de octubre**, de modo que no se puede afirmar que INCIBE no haya publicado
  nada; y la Recomendación 2003/361/CE de umbrales de pyme **no está reverificada en primaria**.


Tres cosas detectadas al revisar el mapa después de publicar la 009. Las dos primeras son de datos
y le tocan a la tarea del lunes. La tercera es un cambio de diseño y **no se hace sin que David lo
confirme**.

### 1. La nota de España en el Reglamento de IA está desactualizada ~~(hacer)~~ **HECHO el 26/10/2026**

`mapa.py`, entrada `ES` de `ia`, dice: «AESIA designada y notificada, pero la ley orgánica que le da
competencias formales sigue pendiente». **Ya no está pendiente: está caducada** desde el 6 de octubre
de 2026, porque el expediente 121/000096 figura «Concluido - (Caducado)» en el Congreso. Pendiente y
caducada no son lo mismo y el matiz importa: pendiente sugiere que avanza. Reescribir la nota.

### 2. El mapa del CRA se contradice con su propia nota ~~(verificar y luego hacer)~~ **HECHO el 26/10/2026**

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

### 4. Un plazo que puede faltar en la tabla ~~(verificar)~~ **CERRADO el 26/10/2026**

La nota del CRA afirma que **el plazo para que los Estados tengan organismos notificados suficientes
es el 11 de diciembre de 2026**. Si es correcto, es un plazo vivo y no entró en la tabla de la
edición 009. **Verificar contra el articulado del Reglamento (UE) 2024/2847 antes de publicarlo**, no
darlo por bueno desde esta nota.

### 6. Banco histórico de incidentes desde 2015 (pedido el 02/11/2026, RESUELTO EN PARTE el 03/11/2026)

**El conflicto que había aquí está resuelto, y al revés de como se había planteado.** Esta nota
decía que rellenar el banco con prensa «rompe la regla de admisión 3» y que había que
proponerle a David limitarse a archivos de reguladores y CERT. David lo rechazó expresamente el
3 de noviembre, con razón: el boletín existe para que esté informado, y un banco que solo
recoge lo que publican los reguladores recoge, en sus palabras, «la mitad de la mitad de la
mitad». La prensa entra; lo que cambia es que va etiquetada. Ver la sección del registro.

**Lo que sí sigue en pie de aquella nota, porque es método y no criterio:**

- La maqueta ya soporta el volumen: el filtro tiene rango de fechas por `conf`, los contadores
  se calculan solos y desde el 03/11/2026 hay además dos niveles de detalle, así que los casos
  antiguos entran como `tabla` y no inflan la página como lo haría una ficha.
- **El peso de la página sí es un problema real** y no está resuelto: va por 520 KB con trece
  incidentes, de los cuales ocho son fichas. Con cientos de entradas hay que medirlo antes de
  seguir cargando. La tabla pesa mucho menos que una ficha, pero no pesa cero.
- **Riesgo de método ya medido:** el archivo histórico de internet está bloqueado en este
  entorno, de modo que no se puede datar de forma independiente la primera publicación de una
  página. Para un banco histórico es grave, porque muchas notas antiguas no llevan fecha.
  `conf` es obligatoria y el validador aborta sin ella, así que **un caso sin fecha de
  publicación verificable no entra**. Eso se mantiene: es una regla de datos, no de criterio.
- Fuentes de relleno que siguen siendo las más rentables, porque son las que menos trabajo de
  verificación exigen: archivos de resoluciones y notas de AEPD, CCN-CERT, INCIBE-CERT,
  autoridades autonómicas, CNIL, Garante, BfDI y los Länder, Datatilsynet, AP neerlandesa,
  UODO, DPC irlandesa, IMY sueca, EDÖB suizo, ICO; comunicaciones de incidente a la CNMV; y las
  once ediciones ya publicadas de este boletín. A eso se le suma ahora prensa de agencia y
  prensa sectorial, con su etiqueta.

**Las cuatro decisiones que David dejó sin contestar el 02/11/2026 siguen abiertas**, y dos de
ellas ya no son urgentes pero las otras dos sí:

1. Importe nominal frente a importe pagado, en las multas (la AEPD reduce un 20 y un 40 por
   ciento por pronto pago y reconocimiento). **Sigue abierta.** Propuesta: publicar el nominal
   en `cifra` y el pagado en la prosa, porque el nominal es el que se cita.
2. Francia: admitir o no las filas anónimas, porque la CNIL anonimiza unos 6,5 millones de
   euros de sanciones de seguridad de 2025. **Sigue abierta.**
3. Criterio de ventana, «incidentes de 2025» frente a «cifras publicadas en 2025».
   **Resuelta de hecho por el registro acumulado**: `conf` es la fecha en que se conoció, y el
   filtro permite las dos lecturas sin tener que elegir.
4. Si el banco vive en una pestaña aparte. **Resuelta: no.** Es la misma sección, con el filtro
   de fecha puesto por defecto en «esta edición».

### 7. Dos automatizaciones de correo (pedidas por David el 02/11/2026)

- **Aviso al publicar la edición**, con resumen incrustado, por Gmail. Montada el 02/11/2026.
- **Correo diario de vulnerabilidades críticas**, CVSS 9,0 o más, con descripción. Montada el 02/11/2026.
  Criterio acordado con David: además del umbral de 9,0 se incluye **el catálogo de vulnerabilidades
  explotadas de CISA con independencia de la puntuación**, porque es el que de verdad anticipa. Esta semana lo
  ha demostrado: la de PHP entró en el catálogo el 26/10 con tres días de plazo, y la del núcleo de Linux que
  encadenaba hasta root puntúa **7,8** y se habría perdido con un filtro de 9,0 a secas.
- **Destinatarios: pendiente de que David complete la lista.** Dijo «jaimecalleja99@gmail.com y algunos más».
  No inventar destinatarios: añadir solo los que él confirme.

### Trampas de fecha y de método aprendidas el 02/11/2026

- **La legislatura en curso es la XV, no la XVI.** El desplegable del propio Congreso dice «XV Legislatura
  (2023-Actualidad)» y su valor de formulario es `15`. Pasar `legislatura=XVI` en la URL de la ficha devuelve
  **la cáscara de la página sin datos y con HTTP 200**, que es un falso negativo perfecto: parece que el
  expediente no existe.
- **La ficha individual del Congreso no es necesaria.** La ruta que funciona y que cierra el apartado es
  `https://www.congreso.es/proyectos-de-ley`, que se renderiza con navegador tras aceptar las cookies y sirve
  **el listado completo de la legislatura con la situación de cada expediente**, paginado con un control
  «siguiente» que avanza de cinco en cinco. De ahí salen los 115 expedientes y los 89 caducados.
- **Los registros de la CNMV sí se pueden barrer, y esta semana se ha cerrado la laguna.** El formulario es
  ASP.NET y el POST no sirve resultados, pero la página de resultados **es direccionable por URL** y se
  renderiza con navegador: `resultado-oir.aspx?fechaDesde=DD/MM/AAAA&fechaHasta=DD/MM/AAAA&page=N`, con
  **`page` empezando en 0** y el mismo patrón en `resultado-ip.aspx`. El parámetro `pagina=` **se ignora** y
  devuelve siempre la página 1, que es el falso negativo que tumbó el barrido de la edición 010. Una página
  puede devolver cuerpo vacío de forma intermitente: reintentar esa sola.
- **El universo de avisos del DOUE serie C son 1.207 si se cuenta por fecha de publicación en 2026**, no los
  328 de la edición 010, que eran los asuntos del Tribunal de Justicia incoados en 2026. Fijar el criterio por
  fecha de publicación, que es el correcto para detectar novedades.
- **El aviso de recurso por incumplimiento SÍ indexa la directiva invocada** en el grafo de citas de Cellar,
  con el predicado `cdm:communication_case_new_requests_establishment_of_failure_of_obligation_resource_legal`.
  Esto corrige el aviso anterior: no hace falta abrir el texto de cada aviso, aunque conviene contrastar.
- **Para las medidas nacionales de ejecución, el predicado de enlace es
  `cdm:measure_national_implementing_implements_resource_legal`**, no `..._transposes_resource_legal`, que
  devuelve cero. La fecha sigue siendo `cdm:measure_national_implementing_date_notification`.
- **El censo NANDO se consulta mejor por el PDF oficial de listas de la Comisión**, que no necesita clave, va
  autofechado con su fecha de generación y es más primario que el endpoint de búsqueda interno, el cual exige
  una `apiKey` incrustada en el frontal. Prueba de control obligatoria igualmente.
- **Los paquetes de infracciones no son mensuales ni caen los días 1 y 2.** Fechas de decisión de 2026: 29
  ene, 10 mar, 28 abr, 3 jun, 7 jul y 30 sep, con comunicado **al día siguiente**. Cadencia de seis a ocho
  semanas en día variable.
- **El feed RSS de catálogo por comité de la ISO no funciona como feed:** redirige y sirve el catálogo del
  comité en HTML con las etapas actuales pero **sin fechas**. La única vía con fechas es abrir el bloque de
  ciclo de vida de cada ficha, una por una, en el espejo `committee.iso.org`.
- **curia.europa.eu no es consultable de forma automatizada:** devuelve 200 con la cáscara de una aplicación
  JavaScript sin dato del asunto, y su calendario judicial da 403. Consecuencia precisa: Cellar es
  concluyente para **documentos publicados**, pero una vista o una fecha de sentencia señaladas y no
  publicadas no se verían desde aquí.
- **El JSON de sumarios del BOE anida asuntos bajo claves `texto`.** Un recorrido superficial del árbol pierde
  unos 28 asuntos; hay que recorrerlo de forma recursiva. Esta semana: 1.576 y no 1.548.
- **IAF e ILAC cesaron el 1 de enero de 2026** y son Global ACI. Sus documentos siguen válidos por las
  resoluciones 2025-25 y 2025-29. Dejar de escribir «documentos obligatorios del IAF».

> **Corrección pendiente de arrastre.** La edición 010 publicó en `TITS` que «la ISO publica la 27028». **No
> está publicada:** está en etapa 60.00 desde el 20/10/2026. Corregido en la sección de correcciones de la 011.
> Si vuelve a aparecer, es que se copió de `TITS` y no de la ficha.

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

> **Cerrado el 26/10/2026 (punto 1).** La entrada `ES` de `ia` ya dice «caducada, no pendiente» desde el
> 6 de octubre de 2026, con el expediente 121/000096, lo que se cayó con él (arts. 4, 5, 6 y 13 a 41), la
> consecuencia verificada (hoy ninguna autoridad española puede imponer las multas de los arts. 99 y ss.) y
> el obstáculo del art. 86.1 CE, que impide arreglarlo por real decreto-ley.

> **Cerrado el 26/10/2026 (punto 2).** Reverificado el censo contra NANDO y reescrito el bloque `cra` entero:
> 14 Estados en `parcial` por tener autoridad notificante, Finlandia en `completa`, **España en `ninguna`** por
> ausencia verificada (ya no `desc`) y 11 en `desc`. Los quince Estados de la edición 009 eran correctos; lo que
> estaba mal era la atribución: **las dos autoridades son belgas, no lituanas** (Lituania tiene dos, pero en el
> EUCC). Y sigue habiendo **cero organismos notificados** en toda la Unión.
>
> **Método que funciona, corregido respecto del aviso anterior.** El endpoint es
> `POST https://webgate.ec.europa.eu/es/search-api/rest/search`, con el cuerpo en `multipart/form-data`. Tres
> cosas que hay que saber o la consulta no sale:
> 1. **El `?type=` de la URL se ignora.** El tipo va dentro del JSON `query`, como `{"term":{"csType":"..."}}`.
>    El índice de autoridades es **`nando_na_ab`** y el de organismos notificados **`nando_notification`**.
> 2. **El campo `query` debe ir con `Content-Type: application/json`** dentro del multipart. Como campo de texto
>    plano devuelve HTTP 500, y esa es la causa de que el método «no funcionase» antes.
> 3. **`naLegislation` no está indexado** en `nando_na_ab`: solo vive dentro del `jsonDoc`. Hay que descargar los
>    registros con `organizationRole=1` y `organizationIfLatestVersion=Y` (el `pageSize` real tope es 200) y
>    filtrar en cliente. Filtrar por `naProcedure` **da ceros falsos**, eso se confirma.
>
> `legislationId` verificados: CRA 2024/2847 = **167953**, EUCC 2024/482 = 164702, IA 2024/1689 = 168380,
> máquinas 2006/42/CE = 131881, reglamento de máquinas 2023/1230 = 162400. La prueba de control sigue siendo
> obligatoria.

> **Cerrado el 26/10/2026 (punto 4).** El plazo **existe y es el artículo 35.2** del Reglamento (UE) 2024/2847,
> la única aparición de esa fecha en todo el texto. Pero **no es lo que parecía** y hay que decirlo así o se
> sobrevende: obliga **a los Estados miembros**, no a las empresas; es obligación **de medios** («se esforzarán
> por garantizar» / «shall strive to ensure»); y el umbral es **agregado en la Unión**, no un cupo por Estado.
> Ya está en la tabla de la edición 010 con esa literalidad. Y ojo al citar el texto español: el DOUE dice
> literalmente «**Los Estados** se esforzarán», no «Los Estados miembros»; corregirlo entre comillas sería una
> cita falsa.
>
> Las demás fechas del artículo 71, verificadas: capítulo IV desde el **11 de junio de 2026**, artículo 14 desde
> el **11 de septiembre de 2026**, aplicación general el **11 de diciembre de 2027**. Y el **artículo 69.3**, que
> casi nadie cita: las obligaciones del artículo 14 alcanzan **a todos los productos comercializados antes del
> 11 de diciembre de 2027**, no solo a los nuevos.

### 5. Cuatro `%%` literales en el CSS de `web.py` (decisión de David, no hacer por iniciativa propia)

Detectado el 26/10/2026 y **heredado de la edición 009**, que se publicó ya con ellos. En las reglas del panel
de filtros hay cuatro `%%` que llegan literales al HTML, porque esa parte de la plantilla no pasa por el
operador `%`:

- `.pop{... top:calc(100%% + 6px) ...}` y su equivalente en la consulta de medios de 560 px
- `.opt{... width:100%% ...}`
- `.ddb{width:100%%}` en la consulta de medios de 560 px

El navegador **descarta esas tres declaraciones** por inválidas. **Comprobado con Playwright sobre la página
publicada, a 1280 px y a 390 px:** el filtro funciona (6 incidentes, 2 al marcar Administración pública, 3 al
añadir Sanidad, 6 al limpiar, 1 con «Esta edición»), el panel abre debajo del botón, no hay desbordamiento
horizontal y **no hay errores de consola**. El único efecto visible es que las filas de opción no llegan al
borde del panel y que, en móvil, los tres botones no se estiran.

No se ha tocado porque un lunes cualquiera no toca maqueta y porque el commit de la edición no debe incluir
`web.py`. **Es un cambio de un carácter por sitio** y conviene hacerlo en una pasada aparte. Aviso para quien lo
haga: comprobar si ese fragmento de CSS llega a pasar por el operador `%` en algún camino, porque si se cambia
a `%` donde sí lo hace, el generador aborta.

### Trampas de fecha y de método aprendidas el 26/10/2026

- **El identificador del sumario del BOE ya no admite el formato por fecha.** `xml.php?id=BOE-S-AAAAMMDD`
  devuelve 302 a la página de error; el identificador real es correlativo de diario (`BOE-S-2026-259`). La ruta
  que funciona es `https://boe.es/datosabiertos/api/boe/sumario/AAAAMMDD` con `Accept: application/json`.
- **En Cellar, para fechar notificaciones de transposición hay que usar
  `cdm:measure_national_implementing_date_notification`, no `cdm:work_date_document`.** No coinciden: hay
  medidas con fecha de documento de 1930, 1964 y 1991. Filtrar por la segunda mete en la ventana cosas que no
  corresponden.
- **`publications.europa.eu/resource/celex/<CELEX>` exige `Accept-Language`.** Sin él devuelve HTTP 400.
- **El listado de consultas públicas del CEPD no ordena por fecha ni pone las abiertas primero.** Las consultas
  vivas no aparecen en la primera página. Hay que ir a las fichas individuales o se concluye que no hay ninguna.
- **El paquete mensual de infracciones de la Comisión sale el día 1 o 2 del mes.** Buscarlo en una ventana del
  19 al 25 dará vacío casi siempre, por diseño del calendario. Y su HTML no se renderiza: el texto completo solo
  se obtiene por el endpoint PDF de impresión de presscorner.
- **Los avisos de recurso por incumplimiento no llevan el objeto en el título**, y el grafo de citas de Cellar no
  indexa la legislación invocada en ellos. La única forma fiable de saber de qué va un recurso es **abrir el
  texto del aviso**. Cualquier barrido por título o por citas produce falsos negativos.
- **Desfase medido entre interponer un recurso y publicar su aviso en el DOUE serie C: de siete a ocho semanas**,
  sobre cuatro casos de 2026. Ausencia de aviso no es ausencia de recurso.
- **La ruta de avisos del INCIBE-CERT enlazada en su propio menú devuelve 404.** La que funciona es
  `https://www.incibe.es/incibe-cert/alerta-temprana/avisos` con su paginación. El sitio es intermitente:
  peticiones idénticas alternan 200, 404 y conexión cerrada. No concluir «no hay avisos» al primer fallo.
- **`iso.org` da 403 a cualquier acceso automatizado; `committee.iso.org/standard/<ficha>.html` sirve el mismo
  catálogo** y sí responde. El feed RSS de catálogo de cada comité cubre más de un año de cambios de etapa.
- **Dominios que han migrado:** la autoridad catalana de `apdcat.gencat.cat` a `www.apdcat.cat`, y la vasca de
  `avpd.euskadi.eus` a `www.avpd.eus`. Los dominios antiguos sirven la misma cáscara de aplicación para
  cualquier ruta, lo que produce **falsos positivos de fecha** si se raspa el antiguo.
- **El registro de certificaciones del ENS admite fechas de concesión futuras** y va con retraso de carga. No
  es un diario de altas: sirve para el total y la tendencia, no para una serie temporal fina.
