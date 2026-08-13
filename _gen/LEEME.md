# Generador del briefing

Este directorio es **la plantilla del sitio**. La tarea de los lunes lo descarga entero,
reescribe solo los ficheros de contenido y vuelve a ejecutar `web.py`. Así la maqueta se
conserva idéntica semana a semana en lugar de reconstruirse de memoria, que es lo que
haría que fuese degradándose.

## Qué se reescribe cada semana

| Fichero | Frecuencia | Qué contiene |
|---|---|---|
| `contenido.py` | **Cada lunes, entero** | Titular, entradilla, claves, plazos, asuntos, correcciones y «comprobado y sin novedad» |
| `incidentes.py` | **Cada lunes, entero** | Incidentes confirmados del periodo, descartados y lagunas |
| `mapa.py` | Solo si algo cambió | Estado de las 5 normas en los 27 Estados |
| `siglas.py` | Al añadir siglas nuevas | Despliegue de siglas |
| `glosario.py` | Al añadir siglas nuevas | Explicaciones largas del glosario |

## Qué NO se toca nunca

`web.py` (la plantilla), `silabas.py` (partición de palabras) y `geo.json` (geometría del
mapa). Si se tocan, la maqueta cambia y hay que revisarla a mano.

## Cómo se ejecuta

```
python3 web.py     # escribe index.html y ed-AAAA-MM-DD.html
```

`web.py` lee `geo.json` desde su propio directorio y descarga `ediciones.json` del
repositorio para reconstruir el archivo histórico.

## Reglas que no se pueden romper

1. **Nada de guiones largos ni medios.** `web.py` lo comprueba y aborta si aparece alguno.
2. **Las cifras se calculan**, nunca se escriben a mano. El total de asuntos sale de contar.
3. **Gmail elimina los bloques `<style>`**: el correo va con estilo en línea, elemento a elemento.
4. **Incidentes: solo lo confirmado** por la entidad afectada, un regulador o un CERT oficial.
5. **El correo no se recorta.** Mismo contenido que la web, por debajo de 100 KB de marcado.
