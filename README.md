# Briefing Ciber-GRC · España y UE

Boletín semanal sobre gobernanza, riesgo, cumplimiento y regulación de ciberseguridad
en España y la Unión Europea. Se publica cada lunes por la mañana.

- **Web**: Cloudflare Pages, desplegada automáticamente desde la rama `main` de este
  repositorio (migrada desde Netlify el 21-09-2026 con una copia exacta de lo publicado).
- **Última edición**: 004, 14 de septiembre de 2026
- **Ediciones publicadas**: 4

## Cómo funciona

Cada lunes una tarea programada investiga el periodo, verifica cada fecha y cada plazo
contra su fuente primaria, genera el sitio con `_gen/web.py` (ver `_gen/LEEME.md`) y lo
sube a este repositorio. Todo lo que llega a `main` (push o subida por la web de GitHub)
se publica solo en Cloudflare Pages en uno o dos minutos. Los push a otras ramas generan
una previsualización con URL propia, sin tocar producción.

`ediciones.json` es el manifiesto del histórico: la tarea lo lee para reconstruir el
archivo, porque cada ejecución arranca sin memoria de las anteriores.

## Estructura

```
index.html          última edición, con pestañas por tema y archivo
ed-YYYY-MM-DD.html  permalink de cada edición
ediciones.json      manifiesto del histórico
404.html            página de error personalizada
robots.txt          bloquea la indexación
_headers            cabeceras de seguridad (CSP, Permissions-Policy, HSTS…)
_gen/               generador: NO se publica
```

El sitio lleva `noindex`: es accesible para quien tenga el enlace, pero no aparece en buscadores.

## Configuración en Cloudflare Pages

| Ajuste | Valor |
|---|---|
| Production branch | `main` |
| Framework preset | `None` |
| Build command | `mkdir -p dist && cp *.html *.json robots.txt _headers dist/` |
| Build output directory | `dist` |

El build command solo copia los archivos del sitio a `dist/`, para que `_gen/` y este
README no se sirvan en la web (en GitHub Pages los ocultaba Jekyll; en Netlify se subía
solo el sitio). Si algún día el sitio necesita otro tipo de archivo (por ejemplo
`_redirects` o imágenes), añádelo a ese comando.

Las URL limpias (`/ed-2026-08-24` sin `.html`) funcionan de serie, igual que en Netlify.
No hace falta `_redirects`.

## Cabeceras

`_headers` reproduce las cabeceras que servía Netlify (misma sintaxis en Cloudflare Pages).
Si activas *Web Analytics* de Cloudflare en el proyecto, la CSP bloqueará el beacon: añade
`https://static.cloudflareinsights.com` a `script-src` y `https://cloudflareinsights.com`
a `connect-src`.
