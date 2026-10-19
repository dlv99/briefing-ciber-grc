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

1. **Sector y Tipo**, en fichas de colores con el recuento de incidentes de cada uno.
   Son de **selección múltiple**: marcar «Banca y seguros» y «Sanidad» muestra los de
   los dos. Dentro de un grupo la condición es «o»; entre los dos grupos, «y». Ninguna
   ficha marcada equivale a todas. Solo aparecen las fichas con al menos un incidente.
2. **Fecha de confirmación**, con cuatro atajos («Esta edición», «Últimos 30 días»,
   «Últimos 90 días» y «Todo») y dos campos de calendario para un rango a medida.
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
