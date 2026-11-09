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

### El banco histórico (hecho el 03/11/2026)

El banco se reconstruyó ese mismo día y ya no está vacío. Tiene **73 incidentes**, de julio de
2026 a noviembre de 2026 más un caso de 2024, en **veinte países**. Vino de dos sitios:

**1. El historial de git, que es donde estaba el tesoro.** Las ediciones 002 a 011 llevaban sus
incidentes escritos y verificados en su día dentro de `incidentes.py`. Se extrajeron de los
commits de cada edición y se dedujo lo que faltaba. Son **54 fichas**, marcadas con `retro`.
Reglas que se siguieron, y conviene respetarlas si se vuelve a hacer:

- Las ediciones 002 a 008 usaban tupla de **doce campos sin fecha de confirmación**. Esa fecha se
  **dedujo** del texto del campo «quién lo confirma», que por convención del boletín era donde
  iba, y si no, del campo de cronología, y si tampoco, de la fecha de la edición. **Las 48 fichas
  con fecha deducida llevan `conf_aprox` y la página las muestra como «hacia el …», con la
  explicación al pasar el ratón.** Una fecha deducida que no se declara como tal es un dato falso.
- **El vector no se infirió nunca.** Todas las reconstruidas llevan `["desc"]`. Deducirlo de la
  prosa habría contaminado justo el filtro que tiene que ser fiable.
- `hecho` va `oficial` porque la regla de admisión de entonces lo garantizaba por construcción:
  nada entraba sin confirmación de la entidad, un regulador o un CERT.
- Van como `detalle: "tabla"` para no inflar la página, pero **su prosa completa se conserva** y
  se despliega en la fila. No se perdió nada.
- Claves heredadas que hubo que traducir: el sector `ret` («Retail y consumo») es el actual `com`,
  y el tipo `san` («Sanción firme») se renombró a **`mul`** para que no chocara de nombre con el
  sector `san` (Sanidad). Si aparece una edición antigua más, hay que repetir esa traducción.
- **Duplicado corregido**: la campaña de refrigeración estaba dos veces, como `refrigeracion`
  (edición 009) y como `frio-francia` (dada de alta el 3 de noviembre). Se fusionaron en la
  primera, que es la que tenía la prosa publicada. Quedan tres parecidos sin tocar y conviene
  mirarlos algún día: `adif`, `adifrenfe` y `renfe` pueden ser el mismo caso contado tres veces.

**2. Los descartados de la edición 011, reinvestigados.** De los 26, cuatro eran bulos de verdad
y veintidós estaban tirados por antigüedad o por la regla vieja. De esos, la mayoría eran
seguimientos de casos que ya estaban en el banco, y **siete eran incidentes nuevos de verdad**,
que se verificaron el 3 de noviembre con sus fuentes abiertas y se dieron de alta con
**`ed: 0`**, que significa archivo: no se publicaron en ninguna edición. La página los marca con
una etiqueta «Archivo» y nunca aparecen en el filtro «esta edición».

**Correcciones de fecha que salieron al verificarlos**, y que son el argumento de por qué esto no
se hace de memoria:

- La multa española no es de marzo de 2025: el acuerdo de inicio es del 3 de febrero y el pago
  voluntario del 17 de febrero de 2025. Marzo es cuando lo recogió la prensa.
- La sanción francesa a Fnac es de **22 de octubre** de 2026, deliberación SAN-2026-015. El 29 de
  octubre es la fecha de publicación. Y son **dos sociedades y dos sanciones**, 6 y 1 millón.
- El caso polaco de los diecinueve millones es **MyDr**, y es **distinto** del de Qbusoft y su
  aplicación Medyc, que ya estaba en el banco como `medyc`. Se confirmó con la nota del propio
  regulador polaco, que los trata como incidentes separados. De paso se corrigió la fecha de
  `medyc` a 25/09/2026, que era la de su comunicado y no la de la edición.
- Los atacantes de MyDr no contactaron con la empresa el 5 de agosto: contactaron con **un medio**
  el 8, y el 12 de agosto es cuando el Gobierno polaco confirmó el acceso y la escala.

### Las dos cifras de las multas, y el aviso sobre Francia

Decisión de David del 03/11/2026: en la columna de importe va el **nominal**, que es el que se
cita, y debajo el **efectivamente pagado** tras las reducciones, en el campo `cifra_pag`. El
ejemplo que lo enseña es `ibermutua`: 1.000.000 de euros nominales y 600.000 pagados, por
acumular la reducción del 20 por ciento por reconocimiento de responsabilidad y otra del 20 por
ciento por pago voluntario, del artículo 85 de la Ley 39/2015. En Francia ese mecanismo no
existe, así que allí la nominal es la real.

**Aviso que corrige una premisa, y hay que decírselo a David si vuelve a salir:** se le preguntó
qué hacer con «las sanciones anónimas de la autoridad francesa», y él eligió admitirlas marcadas
como anónimas. **Resulta que no existen como tales.** Al verificarlo: de las 83 sanciones
francesas de 2025, **solo diez se hicieron públicas**; las 73 restantes del procedimiento
simplificado **no se publican en absoluto**, ni con nombre ni anonimizadas. Lo único que consta
es que **catorce organismos** fueron sancionados por un incumplimiento relativo a la seguridad de
los datos, **sin importe desglosado y sin lista**. El tope legal de ese procedimiento es de
20.000 euros por sanción. O sea: no hay nada que dar de alta, y la cifra de «6,5 millones» que se
le planteó no está sostenida por ninguna publicación del regulador. No se construye sumando
noticias sueltas.

### Lo que sigue pendiente de reingreso

Dos casos del hilo de la refrigeración **no se dieron de alta por no tener fecha o enlace
verificados**, y no se inventan:

- Supermercados en Rusia e Israel atacados en 2022 con controladores de frío obsoletos, que
  Danfoss cuenta en su propia web. Falta la fecha exacta de publicación.
- Planta cárnica en Estados Unidos, 2024, con más de 900 kilos de carne perdidos: la fiscalía
  federal de Los Ángeles acusó a una persona en diciembre de 2025. Hay actuaciones judiciales,
  o sea fuente primaria, pero falta localizar el documento.

Y queda **una laguna de fuente declarada**: el sitio de la Agencia Española de Protección de
Datos bloquea el acceso automatizado y devuelve error, de modo que el texto de la resolución de
`ibermutua` se leyó en una copia alojada por un tercero, que es la que enlaza la ficha. Está
dicho en la propia ficha. Si alguna vez se puede abrir el original, conviene cambiar el enlace.

### El peso de la página, que ahora sí es un problema medido

Con 73 incidentes la página va por **730 KB**, frente a 520 KB con trece. La tabla pesa mucho
menos que una ficha, pero no pesa cero, y la prosa completa de las 54 reconstruidas va dentro del
HTML aunque esté plegada. **Antes de pasar de unos 150 incidentes hay que decidir** si la prosa
de las entradas antiguas se carga aparte en lugar de ir incrustada. No se ha tocado todavía
porque a 730 KB la página sigue cargando bien.

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

## Lo aprendido y lo pendiente de la edición 012 (09/11/2026)

### Correcciones a este propio LEEME, que conviene hacer antes de volver a usarlo

- **El paquete de infracciones de octubre de 2026 se decidió y se comunicó el 1 de octubre**, no el 30 de
  septiembre. La fuente primaria (INF/26/1760) da `eventDate` 2026-10-01 y usa «hoy la Comisión ha decidido»;
  el 30 de septiembre no aparece ni en los metadatos ni en el texto. Y **no existe ningún paquete de
  septiembre de 2026**: los de 2026 son seis, 30 ene (INF/26/115), 11 mar (INF/26/431), 29 abr (INF/26/720),
  4 jun (INF/26/1084), 8 jul (INF/26/1376) y 1 oct (INF/26/1760). La lista de fechas que este LEEME traía
  («29 ene, 10 mar, 28 abr, 3 jun, 7 jul y 30 sep») mezcla fechas de decisión con fechas de comunicado.
  Criterio a partir de ahora: usar la fecha que da el propio documento y no deducir la decisión.
- **La lista anual de proveedores terceros críticos de TIC es del artículo 31(9) de DORA, no del 31(8).** El
  31(8) es la lista de exclusiones de la designación. Citar el 8 dice lo contrario de lo que se quiere decir.
- **El considerando de CER que limita el sector alimentario es el 5, no el 29.**
- **El artículo 2.2.c) de NIS2 dice «el orden público», no «la protección pública».** La expresión «la
  seguridad y la protección públicas» sí existe, pero en el considerando 69 y sobre incidentes a gran escala.
- **El artículo 23.11 de NIS2 no cubre a los proveedores de servicios de confianza.** Su listado obligatorio
  es de infraestructura y servicios digitales.
- **«Entidad importante y no esencial» está incompleto para la alimentación.** El artículo 3.1.e) permite al
  Estado que designa por el artículo 2.2 letras b) a e), y la c) es la de salud pública, clasificar la entidad
  como **esencial**, con el régimen del 34.4 (10 millones o 2 %) en lugar del 34.5 (7 millones o 1,4 %).
- **El techo del 2 de agosto de 2030 del artículo 111.2 del Reglamento de IA ya estaba en el texto de 2024.**
  Lo que el Reglamento 2026/1744 cambió es el disparador, que pasa de fecha fija a la fecha de aplicación del
  capítulo III.
- **La trampa de los enlaces de fichas ISO muy vendidas no se reproduce.** `committee.iso.org/standard/42001`
  sin `.html` sirve hoy la ficha correcta, no una etapa 95.99 de 2014. Dejar el aviso pero como no reproducible.

### Ganancias de método, que son las que ahorran tiempo el lunes que viene

- **La AEPD es alcanzable.** Lo que falla son tres direcciones de canal heredadas (HTTP 500) y **cualquier
  cadena de consulta en sus vistas** (403 de Akamai, incluidos `?page=` y el parámetro de ordenación). Los
  canales que funcionan: `/noticias/feed.xml`, `/blog/feed.xml` y
  `/informes-y-resoluciones/resoluciones/feed.xml`. El mapa del sitio **sí** acepta parámetros. Los listados
  de resoluciones y de blog se sirven montados en servidor; el de notas de prensa se carga por guion. Hay
  retraso de caché demostrado: el canal del blog omitió una entrada del 3 de noviembre que sí estaba en el
  listado, así que los ceros de la AEPD van «con reserva de caché».
- **Para todo articulado de la UE, el Cellar sustituye a EUR-Lex y no es evasión:**
  `publications.europa.eu/resource/celex/<CELEX>` con `Accept: application/xhtml+xml` y `Accept-Language`.
  Sin `Accept-Language` devuelve 400. Para propuestas COM puede devolver **HTTP 300** y hay que seguir al
  `.../DOC_1`. Y dos CELEX que existen devuelven 404 por esta ruta (`52026DC0710`, `52026PC0013`): hay que ir
  por SPARQL al identificador de cellar y de ahí al DOC_1 o DOC_2. **WebFetch no sirve para articulado
  consolidado largo: trunca en torno a 133.000 caracteres.**
- **Trampa de SPARQL que produce ceros falsos y que ya ha costado una pasada:** `?x
  cdm:resource_legal_id_celex "32022L2555"` como literal llano devuelve cero **también para la norma de
  control**, porque el celex va tipado. La forma que funciona es
  `?x cdm:resource_legal_id_celex ?c . FILTER(CONTAINS(STR(?c),"32022L2555"))`. Y en medidas nacionales, un
  `MAX` agregado con `VALUES` devolvió un máximo falso donde el `GROUP BY ?fecha` dio el correcto: usar el
  desglose por fecha.
- **El HTML de presscorner sirve una cáscara vacía.** La vía es la API JSON,
  `ec.europa.eu/commission/presscorner/api/documents?reference=...`, que devuelve el contenido en limpio, y
  `.../api/search?text=...` para buscar. El parámetro `query` de la API de búsqueda **se ignora**. Y el sondeo
  de referencias inexistentes devuelve **HTTP 200 con cuerpo vacío**, que es la señal de inexistencia.
- **Rutas correctas de la CNMV:** `www.cnmv.es/portal/otra-informacion-relevante/resultado-oir?fechaDesde=...`
  y `www.cnmv.es/portal/informacion-privilegiada/resultado-ip?...`, con `page` empezando en 0; el sufijo
  `.aspx` es opcional y da el mismo resultado byte a byte. Las rutas de `consultas/busqueda/` devuelven 403
  por ruta incorrecta, no por bloqueo. **Falso positivo recurrente: «dora» casa dentro de «DISTRIBUIDORA».**
  Usar límite de palabra.
- **Siemens:** el índice y el `changes.csv` del directorio CSAF devuelven 403, pero el **feed CSAF completo**
  `cert-portal.siemens.com/productcert/csaf/ssa-feed-tlp-white.json` responde 200 y permite enumerar
  publicaciones y revisiones. El RSS clásico está **congelado en el 22 de enero de 2026**: usarlo produce un
  falso «sin novedad».
- **SonicWall:** la página de su PSIRT es una cáscara de guion de menos de 1 KB. La vía es
  `psirtapi.global.sonicwall.com/api/v1/vulndetail/?advisory_id=SNWLID-...`, que devuelve el historial.
- **Datatilsynet danesa:** su canal real lleva un identificador opaco enlazado en el pie,
  `/gbapi/rss/feed?id=...`. Las rutas evidentes devuelven 404.
- **Garante italiano:** `garanteprivacy.it/o/gpdp-rss/rss?t=news` funciona; las fichas `docweb` sirven una
  redirección por metarrefresco cuyo destino (`gpdp.it/...`) sí trae el contenido.
- **La Moncloa:** el patrón `refc<AAAAMMDD>.aspx` ya no existe y **deja la conexión caída**, que es la forma
  más fácil de confundir fuente inalcanzable con reunión inexistente. El patrón vigente es
  `<AAAAMMDD>-referencia-rueda-de-prensa-ministros.aspx`. Y **la referencia publicada está truncada en
  origen**: se corta a mitad de palabra en el último asunto. No hay cola que leer.
- **La base de dictámenes del Consejo de Estado del BOE lleva un mes de retraso.** Comprobado: 26 dictámenes
  desde el 1 de septiembre y el más reciente con fecha de aprobación de 8 de octubre de 2026. **Su cero nunca
  es concluyente.** Y su búsqueda libre no hace búsqueda de frase.
- **NIST:** para `CSWP` e `IR` el campo «Date Published» da **solo el mes**. El día sale del «Document
  History» de la ficha o de la nota de retirada del documento derogado. Y la ruta corta `/pubs/cswp/50/final`
  devuelve 404: hay que usar el slug completo.
- **CERT-FR no numera las versiones de sus alertas.** No existe un «v3» que citar: lo citable es «última
  revisión del DD de mes». Y en el índice, las alertas actualizadas llevan el prefijo `[MàJ]` en el título,
  lo que da una forma rápida de distinguir «en curso» de «actualizada».
- **Tres fuentes que dan la fecha del listado distinta de la del documento**, y las tres salieron esta
  semana: en ENISA, los marcadores temporales de dos avisos técnicos están **cruzados entre sí**; su
  comunicado de PHP aparece con fecha de noviembre siendo de octubre; y el mapa del sitio de DG CONNECT
  mostró 98 páginas con fecha de la ventana por una **regeneración masiva del sitio**. Regla: la fecha buena
  es la que el documento declara en su cuerpo.
- **Rastreadores de ataques obsoletos.** El agregador que aparece en primeras posiciones con el rótulo de
  ataques de 2026 sirve entradas de enero a agosto de **2025** y ninguna de noviembre de 2026. Es un cero
  falso, no un bulo, y es peor.

### Cambio de taxonomía: vector `hum`

Se ha añadido a `VECTORES` el vector **`hum`, «Error humano al enviar o publicar»**. Hacía falta: la sanción
polaca de esta edición trae el mecanismo publicado por el regulador con todo detalle, una empleada que adjunta
un fichero por error y un fichero que queda publicado en la plataforma. Meterlo en `cfg` habría ensuciado el
filtro que tiene que ser fiable, y dejarlo en `desc` habría perdido un dato que la fuente sí publica. **Las
entradas antiguas no se han reclasificado**: solo se usa donde la fuente lo declare.

### Correcciones de vector con fuente propia, hechas en esta edición

Se han corregido dos vectores de fichas antiguas, y queda dicho en el `act` de cada una, que es la forma de no
destruir el rastro: **`copenhague`** pasa a `cfg` porque la entidad declara un error de configuración en un
entorno de pruebas y lo califica de error propio, y **`eichstatt`** pasa a `ter` porque el ayuntamiento
declara entrada por una brecha de seguridad de un proveedor de software. Criterio: el vector se corrige cuando
la fuente propia lo publica, porque el filtro tiene que ser fiable; la prosa antigua no se toca.

### Un `%%` latente corregido en el banco

La ficha `ua` (Universidad de Alicante, edición 002) llevaba desde agosto un `%%` en el campo `sabe`, que
salía literal en la página. Corregido **en la entrada**. Conviene barrer `banco.json` por `%%` cada lunes:
es una línea y evita que se repita.

### Decisiones que necesita David, y dos son nuevas

1. **El censo NANDO del Reglamento de Ciberresiliencia.** El buscador exige una clave que la propia
   aplicación pública de la Comisión incrusta en el navegador, y usarla desde este entorno queda bloqueada
   por su política de seguridad. No se ha eludido ni se eludirá por iniciativa propia. **O David autoriza
   expresamente esa consulta, o el cero de organismos notificados se arrastra con fecha del 26 de octubre.**
   No se ha encontrado una tercera vía, y el hito del artículo 35.2 es el 11 de diciembre.
2. **Los cuatro `%%` del CSS de `web.py`** (punto 5 de este LEEME) siguen sin tocar, porque un lunes no toca
   maqueta. Es un carácter por sitio y conviene hacerlo en una pasada aparte.
3. **Las dos escalas de color del mapa** (punto 3) siguen pendientes de su confirmación.
4. **La identidad de la ficha `comtf`**, «colegio de médicos de Tenerife», de la edición 009. No se ha podido
   reconfirmar y las búsquedas dirigidas no devuelven nada; sí existe un caso de junio de 2026 en el
   **colegio de enfermería** de la misma provincia. Hay que resolverlo antes de volver a citarla. Se ha dejado
   la entrada con el aviso en su `act` en vez de borrarla.
5. **La lista de destinatarios de los dos correos** sigue incompleta: David dijo «y algunos más».

### Pendientes concretos para la edición 013

- **Fechar la brecha del estudio nacional ENEIDA** comunicada por un hospital universitario de Valladolid. La
  página se lee pero **no lleva fecha de publicación**, y sin fecha verificable no entra. Hay un PDF homólogo
  de otra gerencia sin abrir cuyo nombre de fichero sugiere 2025.
- **Verificar o descartar el ayuntamiento de Santa Perpètua de Mogoda**, que solo consta por una mención de
  pasada en un medio canario.
- **Reintentar la nota hib 899/2026 del Bundestag**, de 5 de noviembre, que devuelve 404 y es la única fuente
  que sostiene los seis dispositivos infectados y la única que menciona un segundo vector, el bombardeo de
  correo.
- **Pedir el informe posterior al incidente de Binance**, comprometido en su actualización del 1 de noviembre.
- **Barrer los canales propios de las demás cadenas de distribución afectadas** (ICA, Coop Suecia, Carrefour
  Bélgica, Intermarché, Musgrave, Selver, Kesko): sus páginas de prensa no fueron alcanzables esta semana.
- **Las publicaciones propias de las dos casas de seguridad** que dieron telemetría de la campaña del frío,
  si se quieren usar sus cifras como algo más que prensa sectorial.
- **Mirar `adif`, `adifrenfe` y `renfe`**, que siguen sin tocar y pueden ser el mismo caso contado tres veces.
- **El peso de la página va por 758 KB con 87 incidentes.** Sube menos de lo lineal porque las trece entradas
  nuevas de tabla pesan poco, pero el umbral de decisión de los 150 incidentes de este LEEME se acerca:
  a este ritmo se alcanza en cinco o seis ediciones.
