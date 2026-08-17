# Generador del briefing

Este directorio es **la plantilla del sitio**. La tarea de los lunes lo descarga entero,
reescribe solo los ficheros de contenido y vuelve a ejecutar `web.py`. Así la maqueta se
conserva idéntica semana a semana en lugar de reconstruirse de memoria, que es lo que
haría que fuese degradándose.

## Qué se reescribe cada semana

| Fichero | Frecuencia | Qué contiene |
|---|---|---|
| `contenido.py` | **Cada lunes, entero** | `NUM`, `FECHA_ISO`, `FECHA_TXT`, `PERIODO`, titular, entradilla, claves, plazos, `TITS` (titulares de las tarjetas de portada), asuntos, correcciones y «comprobado y sin novedad» |
| `incidentes.py` | **Cada lunes, entero** | Incidentes confirmados, descartados y lagunas |
| `mapa.py` | Solo si algo cambió | Estado de las 5 normas en los 27 Estados |
| `siglas.py` | Al añadir siglas nuevas | Despliegue de siglas |
| `glosario.py` | Al añadir siglas nuevas | Explicaciones largas del glosario |

## Qué NO se toca nunca

`web.py` (la plantilla), `silabas.py` (partición de palabras) y `geo.json` (geometría del
mapa).

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
