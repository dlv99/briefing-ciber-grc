# Briefing Ciber-GRC · España y UE

Boletín semanal sobre gobernanza, riesgo, cumplimiento y regulación de ciberseguridad
en España y la Unión Europea. Se publica cada lunes por la mañana.

- **Web**: ver GitHub Pages de este repositorio
- **Última edición**: 001, 13 de agosto de 2026
- **Ediciones publicadas**: 1

## Cómo funciona

Cada lunes una tarea programada investiga el periodo, verifica cada fecha y cada plazo
contra su fuente primaria, genera el sitio y hace push a este repositorio.
GitHub Pages publica el resultado automáticamente.

`ediciones.json` es el manifiesto del histórico: la tarea lo lee para reconstruir el
archivo, porque cada ejecución arranca sin memoria de las anteriores.

## Estructura

```
index.html          última edición, con pestañas por tema y archivo
ed-YYYY-MM-DD.html  permalink de cada edición
ediciones.json      manifiesto del histórico
robots.txt          bloquea la indexación
```

El sitio lleva `noindex`: es accesible para quien tenga el enlace, pero no aparece en buscadores.
