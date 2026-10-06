---
name: Briefing Ciber-GRC
description: Diario de regulación ciber-GRC en papel claro, con seis ámbitos de color y la custodia del dato dibujada.
colors:
  bg: "#f7f4ef"
  paper: "#fffdfa"
  ink: "#14161a"
  ink2: "#3f464f"
  ink3: "#767d87"
  rule: "#d9d3c8"
  hair: "#ebe6dd"
  hot: "#C62828"
  hot-t: "#FDECEA"
  es: "#C62828"
  es-t: "#FDECEA"
  eu: "#1565C0"
  eu-t: "#E8F1FB"
  fin: "#00796B"
  fin-t: "#E3F2F0"
  std: "#6A1B9A"
  std-t: "#F4E9F8"
  ai: "#E65100"
  ai-t: "#FDEEE2"
  thr: "#AD1457"
  thr-t: "#FCE9F1"
  bg-dark: "#0e0f11"
  paper-dark: "#17191c"
  ink-dark: "#f0f2f5"
  ink2-dark: "#bcc2ca"
  ink3-dark: "#8b929b"
  rule-dark: "#2c3036"
  hair-dark: "#202329"
  hot-dark: "#F0857C"
  hot-t-dark: "#331d1c"
  es-dark: "#F08A80"
  es-t-dark: "#3A1A18"
  eu-dark: "#7FB0F5"
  eu-t-dark: "#152534"
  fin-dark: "#4FC9B8"
  fin-t-dark: "#122B29"
  std-dark: "#C39BF0"
  std-t-dark: "#261830"
  ai-dark: "#F2A25C"
  ai-t-dark: "#33200F"
  thr-dark: "#F08BB4"
  thr-t-dark: "#331522"
typography:
  display:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: "clamp(33px, 5.4vw, 50px)"
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "-0.028em"
  headline:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: "clamp(30px, 4.8vw, 44px)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.025em"
  title:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: "clamp(23px, 3.1vw, 29px)"
    fontWeight: 600
    lineHeight: 1.24
    letterSpacing: "-0.016em"
  subtitle:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.68
  body-small:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.5
  ladillo:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.35
    fontStyle: "italic"
  label:
    fontFamily: "Inter, ui-sans-serif, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "0.15em"
    textTransform: "uppercase"
  ui:
    fontFamily: "Inter, ui-sans-serif, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: "13.5px"
    fontWeight: 600
    lineHeight: 1
  mono:
    fontFamily: "ui-monospace, Menlo, monospace"
    fontSize: "13.5px"
    lineHeight: 1
rounded:
  nada: "0"
  sello: "2px"
  caja: "4px"
  flotante: "5px"
  pastilla: "20px"
  marca: "50%"
spacing:
  xs: "5px"
  sm: "7px"
  md: "13px"
  lg: "19px"
  xl: "26px"
  xxl: "34px"
  bloque: "64px"
components:
  nav-tab:
    textColor: "{colors.ink3}"
    typography: "{typography.ui}"
    padding: "12px 13px"
    rounded: "{rounded.nada}"
  nav-tab-selected:
    textColor: "{colors.eu}"
    typography: "{typography.ui}"
    padding: "12px 13px"
  card-ambito:
    backgroundColor: "{colors.es-t}"
    textColor: "{colors.ink2}"
    rounded: "{rounded.caja}"
    padding: "19px 21px"
  card-ambito-hover:
    backgroundColor: "{colors.es-t}"
    rounded: "{rounded.caja}"
  sec-header:
    backgroundColor: "{colors.es}"
    textColor: "#ffffff"
    rounded: "{rounded.caja}"
    padding: "14px 19px"
  tag-solido:
    backgroundColor: "{colors.es}"
    textColor: "#ffffff"
    rounded: "{rounded.sello}"
    padding: "5px 9px"
  tag-perfilado:
    textColor: "{colors.es}"
    rounded: "{rounded.sello}"
    padding: "5px 9px"
  chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink2}"
    rounded: "{rounded.pastilla}"
    padding: "7px 14px"
  chip-pressed:
    backgroundColor: "{colors.ink}"
    textColor: "#ffffff"
    rounded: "{rounded.pastilla}"
    padding: "7px 14px"
  input-busca:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.caja}"
    padding: "9px 13px"
    width: "420px"
  boton-banderola:
    backgroundColor: "{colors.hot}"
    textColor: "{colors.bg}"
    rounded: "{rounded.nada}"
    padding: "13px 26px 13px 19px"
  boton-banderola-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.bg}"
  boton-banderola-2:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.nada}"
    padding: "12px 25px 12px 18px"
  panel-tinte:
    backgroundColor: "{colors.es-t}"
    rounded: "{rounded.caja}"
    padding: "30px 32px"
  caja-papel:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.caja}"
    padding: "17px 20px"
  ficha-margen:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.nada}"
    padding: "20px 22px 22px"
    width: "15.5em"
  chip-estado:
    textColor: "{colors.ink2}"
    rounded: "{rounded.nada}"
    padding: "2px 8px"
  chip-estado-firme:
    textColor: "{colors.hot}"
    rounded: "{rounded.nada}"
    padding: "2px 8px"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.bg}"
    rounded: "{rounded.flotante}"
    padding: "11px 14px"
    width: "290px"
---

# Design System: Briefing Ciber-GRC

> Documento descriptivo, escrito después de la construcción. Cada valor sale del artefacto
> publicado: la constante `CSS` de `_gen/web.py` (f-string: las llaves van **dobladas**,
> `{{`/`}}`), la constante `CSS_QE` del mismo fichero (cadena normal: llaves **sencillas**),
> y el HTML servido en `index.html`, `ed-2026-*.html` y `que-es.html`. No hay fichero `.css`:
> **la hoja de estilos es el generador**. Lo que no está en el artefacto no está aquí.

## Overview

**Creative North Star: "El diario de taller"**

Un periódico de una sola columna impreso en papel barato y bueno: fondo hueso, tinta casi
negra, filetes finos, titulares en serifa apretada y una franja de seis colores arriba que
dice de qué va cada cosa antes de leer una palabra. No hay ilustración, no hay fotografía,
no hay logotipo, no hay firma. La densidad es alta y deliberada: el lector viene el lunes a
leer largo en escritorio, así que el cuerpo es grande (19px), la medida es corta (`--medida:
34em`) y la página se deja recorrer sin sobresaltos. Todo adorno que no distinga un hecho
comprobado de uno que no lo está sobra.

El sistema es de **dos mundos completos**, no de un tema con variantes: `prefers-color-scheme`
cambia todas las fichas de una vez, incluidos los seis colores de ámbito y sus seis tintes de
fondo. Nada se queda a medias entre claro y oscuro.

Lo propio del mundo, y lo único que la superficie nueva `/que-es` ha añadido al sistema, es
que **el estado de verificación de un dato es un elemento gráfico**: línea continua donde hay
documento detrás, línea discontinua gris donde el briefing no llega. Ese es el movimiento que
el resto de las decisiones protege.

**Key Characteristics:**

- Papel hueso `#f7f4ef` y tinta `#14161a`; mundo oscuro equivalente y total.
- Seis ámbitos fijos con color propio, tinte de fondo propio y variante oscura propia.
- Serifa de lectura a 19px/1.68, justificada, con guion blando inyectado; Inter solo para etiquetas y mandos.
- Plano: ni sombras de elevación ni degradados decorativos. La profundidad es tinte y filete.
- El estado de un dato se dice tres veces a la vez: línea, marca y chip de texto.

## Colors

Paleta de imprenta: un hueso cálido, una tinta fría, un rojo de titular y seis colores de
ámbito saturados que solo aparecen en superficies pequeñas o sobre blanco.

### Primary

- **Rojo de cinta** (`hot`): el acento único. Titula lo urgente (`tr.u` en la tabla de plazos,
  `.rad.urg` en el radar), marca los enlaces de la cabecera, dibuja la banderola y la línea de
  custodia de lo comprobado, y rellena el botón principal de `/que-es`. En oscuro pasa a un
  coral claro porque el rojo original no aguanta sobre `#0e0f11`.
- **Tinte de cinta** (`hot-t`): fondo de la fila de plazo urgente y del panel de correcciones.

### Secondary

Los seis **ámbitos** (`es`, `eu`, `fin`, `std`, `ai`, `thr`) son vocabulario del producto antes
que paleta. Cada uno trae tres fichas: color de trazo, tinte de fondo (`-t`) y variante oscura.
Gobiernan la franja de seis segmentos del mastil (`.stripe`), la barra de pestañas (variable
`--tc` por pestaña), la cabecera de sección (`.sec-h`, color pleno con texto blanco), la tarjeta
de portada (tinte de fondo, rótulo a color), el ladillo interrogativo, el aside `.why`, la
capitular y la lista de ámbitos de `/que-es` (variable `--ac`).

- **Rojo España** (`es`): ámbito nacional. Coincide en valor con el rojo de cinta, y eso es
  intencionado: el ámbito nacional y la urgencia comparten tinta.
- **Azul Unión** (`eu`): regulación horizontal; también el mapa UE y el perfil de pestaña por defecto.
- **Verde finanzas** (`fin`): DORA y supervisores; también el panel «comprobado y sin novedad».
- **Violeta normas** (`std`): marcos de referencia; también el distintivo de tipo «directiva».
- **Naranja IA** (`ai`): reglamento de IA y datos. Es el color más débil del juego (3,45:1 sobre papel).
- **Magenta amenaza** (`thr`): explotación activa y avisos de CERT.

### Tertiary

Colores de navegación y de dato que no pertenecen a ningún ámbito y viven como literales en el
generador: gris pizarra `#5a6570` (pestañas Portada y Archivo), granate `#B71C1C` (Incidentes),
azul `#1565C0` (Mapa UE), verde profundo `#00695C` (Glosario), naranja `#E65100` (vencimiento
próximo, `.cd.pron`) y verde `#2E7D32` (confirmación del botón de copiar enlace).

### Neutral

- **Papel** (`bg`): fondo de página, y también fondo de la navegación fija para que la barra no flote.
- **Papel claro** (`paper`): fondo de las cajas que se levantan del fondo (`.read`, `.ed`, `.inc`, `.rad`, `.ficha`, `.chip`, el buscador).
- **Tinta** (`ink`): prosa, titulares, filete fuerte de cabecera de tabla y de pie.
- **Tinta media** (`ink2`): entradilla, prosa secundaria, texto de leyenda y de chip de estado.
- **Tinta débil** (`ink3`): texto accesorio grande, filetes y gráficos no textuales. **No es un color de texto corrido** (ver regla).
- **Filete** (`rule`) y **capilar** (`hair`): los dos únicos grosores de separación del sistema.

### Contraste medido

Sobre `#f7f4ef`: `ink` 16,5:1 · `ink2` 8,7:1 · `ink3` 3,79:1 · `hot` 5,12:1 · ámbito `ai` 3,45:1.
Sobre `#0e0f11`: `ink` 17,1:1 · `ink2` 10,7:1 · `ink3` 6,1:1 · `hot` 7,63:1.

### Named Rules

**La regla del color que no porta.** `ink3` (3,79:1) y el ámbito `ai` (3,45:1) están por debajo
de AA para texto de cuerpo sobre papel claro. No llevan nunca prosa corrida ni etiquetas
pequeñas: valen para texto grande, filetes y gráficos no textuales. En la cinta de custodia
`ink3` dibuja la línea discontinua, no la palabra.

**La regla de los seis ámbitos.** El color de un bloque no se elige: se hereda del ámbito al que
pertenece el contenido, inyectado como `style="--ac:var(--es)"` o equivalente. Seis ámbitos,
seis colores, ni uno más. Una superficie nueva que necesite un color temático usa uno de los
seis o no usa ninguno.

**La regla del doble mundo completo.** Toda ficha nueva se declara en los dos bloques: `:root` y
`@media(prefers-color-scheme:dark)`. Un color que solo existe en claro es un error, no una
simplificación.

## Typography

**Display / lectura:** Source Serif 4 (con Georgia y Times New Roman detrás), ejes ópticos
`8..60`, pesos 400/600/700 y cursiva 400/600.
**Etiquetas y mandos:** Inter 500/600/700 (con la pila del sistema detrás).
**Monoespaciada:** solo en `code`, para dominios y referencias técnicas dentro de la prosa.

**Carácter:** una serifa de texto moderna, de ojo grande y gris uniforme, apretada en titulares
con tracking negativo (hasta `-0.028em`); contra ella, una sans neutra que solo hace de rótulo,
siempre en versalitas con tracking abierto (`0.09em`–`0.17em`). La serifa habla; la sans señala.
El mastil añade `font-variant:small-caps` al nombre de la cabecera: es la única pieza con ese
rasgo y es la firma tipográfica del producto.

### Hierarchy

- **Display** (700, `clamp(33px,5.4vw,50px)`/1.06, `-0.028em`): título de una superficie propia. Hoy solo el `h1` de `/que-es`.
- **Mastil** (700, `clamp(28px,5.2vw,46px)`/1, `-0.022em`, small-caps): el nombre del briefing. No se reutiliza.
- **Headline** (700, `clamp(30px,4.8vw,44px)`/1.1, `-0.025em`, `text-wrap:balance`): titular de pestaña (`h2.tit`).
- **Headline de sección propia** (700, `clamp(25px,3.4vw,33px)`/1.18, `-0.022em`): los `h2` de `/que-es`, cada uno precedido de la banderola.
- **Title** (600, `clamp(23px,3.1vw,29px)`/1.24, `-0.016em`): titular de asunto (`h3.titular`).
- **Subtitle / entradilla** (400, 21px/1.55, `ink2`): bajada de cualquier titular. En móvil 19px.
- **Body** (400, 19px/1.68, justificado): la prosa. En móvil 18px. Medida máxima `34em`.
- **Body small** (400, 17px/1.5): cajas de servicio (`.read`, `.bulo`, `.sil`, celdas de tabla).
- **Ladillo** (600, 15px/1.35, cursiva, a color de ámbito): los tres ladillos interrogativos de cada asunto («¿Qué ha cambiado?», «¿Por qué te importa?», «¿Dónde leerlo?»).
- **Label** (600/700, 10px–12px, `0.09em`–`0.17em`, versalitas): rótulos de bloque, encabezados de tabla, sellos, chips de estado y términos de definición.
- **UI** (600, 12px–13,5px/1): pestañas, chips, botones, selectores de norma.

### Named Rules

**La regla de la medida única.** `--medida: 34em` es la medida de lectura y gobierna la página
entera, no solo los párrafos: también el pie, la leyenda y el borde izquierdo del que arranca
todo lo demás. Lo que necesita más ancho (tablas, rejillas, mapa) declara `max-width:none` de
forma explícita; no se ensancha por omisión.

**La regla del guion blando.** La prosa va justificada (`text-align:justify`,
`hyphens:auto`, `hyphenate-limit-chars:7 4 3`) y **todo** texto corrido pasa por
`silabas.blandear()` antes de imprimirse, que inyecta guiones blandos. Sin eso el justificado
abre ríos. Los titulares quedan fuera: llevan `hyphens:none` y `text-wrap:balance`.

**La regla de la sans que no narra.** Inter no escribe nunca una frase. Si un bloque de Inter
pasa de una línea de rótulo, va en serifa.

## Layout

Columna central de **1080px** máximo para la caja de página (mastil, navegación, buscador,
`main`), con `padding:0 24px 110px` y `0 18px 80px` por debajo de 640px. Dentro de esa caja, la
lectura se estrecha a `--medida` mediante `.col`, centrada con márgenes automáticos. Las piezas
anchas (`.grid`, `.tabla`, `.radar`, `.mapa-w`, `.sec-h`) rompen la medida con `max-width:none`.

**Ritmo vertical** por saltos reconocibles: 34px antes de una cabecera de sección o de un
rótulo de grupo, 38px de aire superior en cada asunto, 30px entre paneles, 64px entre secciones
de `/que-es`, 56px antes del pie. El relleno interior crece con la importancia del bloque:
13–15px en celda y chip, 17–22px en caja de servicio, 27–32px en panel y clave.

**Rejillas.** Las tarjetas de portada y el radar de plazos son rejillas fluidas
(`auto-fit, minmax(232px,1fr)` y `minmax(215px,1fr)`, `gap` 12px y 11px). El mapa UE es de dos
columnas asimétricas (`minmax(0,1fr)` + `minmax(0,280px)`, `gap` 30px). La rejilla de los 27
Estados es de 7 columnas con celdas `aspect-ratio:1`.

**La ficha de margen.** En `/que-es`, `.qe-top` es una rejilla de `minmax(0,var(--medida))` +
`15.5em` con `gap:0 46px`: la prosa manda a la izquierda sobre la medida y la ficha de datos
queda a la derecha como aparato de margen. Un bloque que necesite ocupar las dos columnas usa
`.qe-ancho` (`calc(var(--medida) + 15.5em + 46px)`). La página entera arranca del mismo borde
izquierdo, pie incluido (`.qe footer{margin-left:0}`).

**Puntos de ruptura** observados: **860px** (el mapa y `.qe-top` pasan a una columna; las
rejillas de ámbitos y de leyenda se colapsan), **820px** (segunda declaración de `.mapa-w`) y
**640px** (cuerpo a 18px, menos relleno, columna de «a quién obliga» oculta). No hay más.

La navegación es `position:sticky; top:0` con `z-index:20` y fondo opaco de papel. La hoja
incluye un bloque `@media print` de primera clase: se despintan los mandos, se despliegan todas
las pestañas ocultas, los fondos de panel pasan a gris claro y cada enlace imprime su URL con
`content:" (" attr(href) ")"`.

### Named Rules

**La regla del ancho declarado.** Nada se ensancha por descuido. Si una pieza pasa de `34em`,
lo dice en su propia regla.

## Elevation & Depth

**El sistema es plano.** No hay escala de elevación, no hay sombras de reposo, no hay
degradados decorativos. La profundidad se construye con tres recursos, en este orden: **tinte de
fondo** (los `-t` de ámbito, `hair`, `hot-t`), **papel sobre papel** (`paper` dentro de `bg`) y
**filete** (`rule` 1px, `hair` 1px, `ink` 1px–3px para los cortes fuertes).

### Shadow Vocabulary

- **Anillo capilar** (`box-shadow: 0 0 0 1px rgba(0,0,0,.13)` y `.15`): sin desplazamiento ni difusión; sustituye el borde en las banderas `img` del mapa, donde un `border` recortaría el gráfico.
- **Sombra de flotante** (`box-shadow: 0 6px 22px rgba(0,0,0,.28)`): única sombra real del sistema, y solo en el tooltip del mapa, que sí flota sobre la página.

### Named Rules

**La regla de lo plano en reposo.** Ninguna superficie en reposo proyecta sombra. Solo la
proyecta lo que de verdad está por encima del plano de la página, y hoy eso es exactamente una
pieza: el tooltip del mapa.

**La regla del tinte antes del borde.** Para separar un bloque de su entorno, primero tinte de
ámbito; después papel; el borde, solo si hay que distinguir dos bloques del mismo tono.

## Shapes

Esquinas casi rectas y una sola geometría singular.

- **4px** es el radio por defecto de todo lo que es caja: tarjetas, paneles, cajas de servicio, el buscador, la ficha del mapa, las celdas de la rejilla de Estados.
- **2px** para lo que es sello: distintivos (`.pri`, `.tag`, `.tipo-b`), `code`, las muestras pequeñas.
- **0** para lo que es imprenta: el mastil, la franja, las cabeceras de tabla, el pie, la ficha de margen y los chips de estado de `/que-es`. La superficie nueva es la parte más recta del sistema, y a propósito.
- **20px** (pastilla) solo en los chips de filtro de incidentes. **50%** solo en las marcas circulares de la cinta de custodia y de su leyenda.

**La muesca de banderola.** La forma propia del mundo: un rectángulo con el flanco derecho en
pico, recortado con
`clip-path:polygon(0 0,calc(100% - 11px) 0,100% 50%,calc(100% - 11px) 100%,0 100%)`. Es la misma
silueta que el SVG `BANDEROLA` (`viewBox 0 0 10 16`, 9x15, relleno pleno) que abre cada sección
de `/que-es`. En la variante secundaria el filete no se puede dibujar con `border` (el
`clip-path` se lo come): se consigue con 1px de relleno y el fondo del elemento exterior.

**Trazo gráfico.** Los iconos autorales del diccionario `IC` son SVG de `16x16`, `fill:none`,
`stroke:currentColor`, `stroke-width:1.45`, remates y uniones redondeados, y se pintan a 15–19px
según el sitio. Son dibujos propios, no una fuente de iconos ni un paquete.

### Named Rules

**La regla del icono autoral.** Los iconos se dibujan en `IC` con la misma rejilla de 16 y el
mismo trazo de 1,45. Ni glifos tipográficos, ni emoji, ni iconos de paquete, ni `<img>`.

## Components

### Franja de ámbitos (`.stripe`)

El primer elemento de cualquier página del sistema. Seis segmentos iguales (`display:flex`,
`flex:1`) de **5px** de alto, uno por ámbito, en el orden fijo `es, eu, fin, std, ai, thr`.
Identifica el producto antes que el nombre, y es lo primero que ve el lector en las siete
ediciones y en `/que-es`.

### Mastil (`.masthead`)

Centrado, `padding:26px 24px 0`. Nombre en serifa 700 con versalitas y tracking negativo, y
debajo una tira de datos de edición entre dos filetes de tinta de 1px. En impresión el mastil se
alinea a la izquierda y pierde el relleno.

### Navegación por pestañas (`nav`)

- **Forma:** barra fija superior, `gap:1px`, desbordamiento horizontal con barra de scroll oculta, filete `rule` abajo.
- **Reposo:** Inter 600 13,5px en `ink3`, icono a `opacity:.75`, borde inferior transparente de 3px.
- **Hover:** texto a `ink`, icono a opacidad plena.
- **Activa:** `aria-selected="true"` pone texto y borde inferior de 3px al color de la pestaña (`--tc`), que es el color del ámbito o un literal de navegación.
- **Buscando:** con el buscador activo, `body.buscando` baja las pestañas a `opacity:.35` y las desactiva.

### Tarjeta de ámbito (`.card`)

Carácter: una ficha de archivador, no un botón. Fondo de tinte de ámbito, radio 4px, borde
transparente de 1px que al hover se vuelve `rule` (el borde ya está reservado, así que nada se
mueve). Dentro: rótulo versalita con icono a color de ámbito, titular en serifa 400 16px sobre
`ink2`, y recuento en Inter 600 11,5px sobre `ink3`.

### Chips de filtro (`.chip`)

Pastilla de 20px, fondo papel, borde `rule`, Inter 600 12,5px en `ink2`. Hover: borde a `ink3`.
`aria-pressed="true"`: fondo y borde al color del grupo (`--cc`), texto blanco. El recuento va
dentro del chip en `<b>`.

### Sellos (`.pri`, `.tag`, `.tipo-b`)

Dos variantes, mismo molde: **sólido** (fondo a color, texto blanco) para la categoría
principal, y **perfilado** (fondo transparente, borde y texto al mismo color) para las
secundarias. Inter 700 9,5px, tracking 0,09–0,12em, versalitas, radio 2px.

### Cajas de servicio

- **`.read` «¿Dónde leerlo?»:** papel sobre papel, borde `rule`, radio 4px, relleno 17/20; los enlaces van en 600 subrayados con `text-underline-offset:3px`.
- **`.why` «¿Por qué te importa?»:** tinte de ámbito, sin borde, relleno 19/22.
- **`.warn`:** sin fondo; filete izquierdo de 3px al color del ámbito y texto en serifa 16px sobre `ink3`. Es la advertencia de laguna de acceso.
- **`.panel`:** el bloque grande, relleno 30/32 sobre tinte; en móvil 22/20.

### Buscador (`.busca input`)

Fondo papel, borde `rule` 1px, radio 4px, Inter 400 15px, ancho máximo 420px. **Foco:**
`outline:2px solid var(--es)` con `outline-offset:-1px` y borde al mismo color. A su lado, el
recuento de resultados en Inter 500 13px sobre `ink3`.

### Tabla de plazos

Encabezado en versalitas 700 10px sobre `ink3`, cortado por un filete de **2px de tinta**;
filas separadas por capilar. La columna de fecha es Inter 600 14px `nowrap`. La fila urgente
(`tr.u`) lleva fondo `hot-t` y la fecha en `hot` 700. Es el único sitio donde el color de fondo
de una fila significa algo.

### Entrada de archivo (`.ed`)

Bloque enlazado de papel con borde `rule` y radio 4px, relleno 22/24. Cuatro renglones fijos:
número de edición en versalitas a color de ámbito, fecha, titular en serifa 600 20px y línea de
recuentos. Hover: borde a `ink3`. La edición en curso se marca con tinte y borde del ámbito `es`.

### Botón de banderola (`.qe-bot`)

El único botón del sistema, introducido por `/que-es`. Carácter: un bloque de tinta con el
flanco en pico, no una pastilla.

- **Forma:** rectángulo con la muesca de banderola, radio 0, relleno `13px 26px 13px 19px` (asimétrico: la muesca se come el flanco derecho).
- **Primario:** fondo `hot`, texto en papel, Inter 600 12px con tracking 0,13em en versalitas.
- **Hover:** fondo a `ink`.
- **Secundario (`.qe-bot-2`):** fondo de papel con filete de tinta simulado por 1px de relleno del elemento exterior; hover invierte a tinta plena.
- **Variante correo (`.qe-correo`):** misma silueta, Inter 600 15px sin versalitas y `word-break:break-word`, porque el contenido es una dirección.
- **Foco:** `/que-es` declara `:focus-visible{outline:2px solid var(--hot);outline-offset:3px}` para toda la superficie.
- En impresión los botones desaparecen.

### Ficha de margen (`.ficha` en `/que-es`)

Lista de definición sobre papel con borde `rule` y **radio 0**. Término en Inter 600 11px
versalita con tracking 0,15em sobre `ink2`; definición en serifa 400 16px sobre `ink`, con
`font-variant-numeric:tabular-nums` para que las cifras calculadas se alineen. El valor nulo
declarado («Ninguna, a propósito») va en cursiva con la clase `.nula`: el sistema tiene una
forma para decir que un campo está vacío a propósito.

### Cinta de custodia (`.pliegues`, `.pl`) — componente firma

La única aportación de `/que-es` al sistema, y la pieza que define el mundo. Una lista ordenada
donde cada pliegue lleva, a 44px del borde izquierdo, una línea vertical y una marca, y en su
cabecera un chip de texto con el estado. **El estado se dice tres veces: trazo de línea, forma
de marca y palabra.**

| Estado | Línea | Marca | Chip |
|---|---|---|---|
| **Comprobado** (`.pl-firme`) | continua 2px en `hot` | disco pleno `hot`, 14px | texto y borde en `hot` |
| **Previsión propia** (`.pl-prev`) | filete continuo de 1px en `hot` | anillo de 1px `hot` sobre papel | texto y borde en `hot`, borde discontinuo |
| **No alcanzado** (`.pl-hueco`) | discontinua 2px, `repeating-linear-gradient(ink3 0 4px, transparent 4px 9px)` | anillo discontinuo de 2px en `ink3` | borde discontinuo, texto `ink2` |
| **Descartado** (`.pl-fuera`) | discontinua 2px en `ink3` | anillo de 1px `ink2` con cruz dibujada a dos degradados a 45º | borde discontinuo, texto `ink2` |

La línea del último pliegue se oculta (`.pl:last-child::before{display:none}`): la cinta termina,
no se desvanece. Los chips (`.pl-est`) son Inter 600 11px versalita con borde de 1px y relleno
`2px 8px`, en `nowrap`.

### Leyenda de la cinta (`.qe .leyenda`)

Rejilla de **2x2** (`repeat(2,minmax(0,1fr))`, `gap:13px 26px`) sobre un filete superior, Inter
500 12px en `ink2`. Cada entrada repite su línea **y** su marca: muestra de 36x2px con el
marcador en `::before`. La marca de la leyenda va **un paso mayor** que la de la cinta (16px
frente a 14px) porque a 12px el anillo discontinuo se rompe en fragmentos. Las cuatro entradas
en 2x2 y no en flujo libre: en flujo la cuarta quedaba huérfana y la clave se leía como un
accidente. En móvil, una columna.

### Lista de ámbitos (`.ambitos`, `.amb`)

Dos columnas con `gap:0 44px`; cada fila es una rejilla `auto 1fr` separada por capilar
superior, con un tramo de color de 20x4px como viñeta (el color entra por `--ac`), nombre en
serifa 600 17px y descripción en serifa 400 15px sobre `ink2`. Es la franja de seis ámbitos
explicada en texto, con el mismo orden y los mismos colores.

### Mapa UE

- **Mapa SVG:** relleno al color de estado, `stroke-width:1.6` con `vector-effect:non-scaling-stroke`; hover y `.act` suben el trazo a 2,6px en `ink` con `filter:brightness(1.12)`; el foco lo sube a 3px. El estado «hueco» se pinta con relleno transparente y el «rayado» con `fill-opacity:.34`. Luxemburgo y Malta llevan marca circular por tamaño.
- **Selector de norma (`.norm`):** botón de papel con borde `rule`, radio 4px, Inter 600 13,5px, con una segunda línea en 500 11px a `opacity:.7`. Pulsado: fondo e incluso borde en `ink`, texto en papel.
- **Celda de Estado (`.cel`):** cuadrada, radio 4px, borde de 2px; `.hueca` pasa el borde a discontinuo y quita el fondo, `.rayada` superpone un rayado a 45º de `rgba(0,0,0,.16)`; hover escala a 1,09. España se marca con `outline:2.5px solid var(--ink)` y `outline-offset:2px`.
- **Tooltip (`.tip`):** tinta plena, texto en papel, radio 5px, la única sombra del sistema, `pointer-events:none` y transición de opacidad de 0,12s.
- **Barra de reparto (`.barra`):** tira de 13px de alto, radio 3px, segmentos con `flex` proporcional al recuento y `gap:2px`.

### Movimiento

Casi inexistente y siempre al servicio del estado, nunca decorativo. Solo cuatro transiciones en
todo el sistema: opacidad del botón de ancla (0,15s), opacidad del tooltip (0,12s),
`filter`/`stroke-width` del mapa (0,12s) y escala de la celda (0,1s). No hay animaciones de
entrada, ni parallax, ni revelados al hacer scroll.

## Do's and Don'ts

### Do:

- **Do** declarar toda ficha nueva en los dos mundos, `:root` y `prefers-color-scheme:dark`, incluido su tinte.
- **Do** tomar el color temático de uno de los seis ámbitos, inyectado como variable (`--tc`, `--ac`, `--cc`, `--tg`), nunca como literal nuevo.
- **Do** pasar toda prosa corrida por `silabas.blandear()` antes de imprimirla; el justificado a 34em lo exige.
- **Do** mantener `--medida: 34em` como medida de lectura y declarar `max-width:none` de forma explícita en lo que deba ser más ancho.
- **Do** llevar el estado de un dato por tres canales a la vez (trazo, forma y palabra), como hace la cinta de custodia.
- **Do** dibujar los iconos nuevos en `IC`, a 16x16 con trazo de 1,45 y remates redondeados.
- **Do** separar bloques con tinte y filete antes que con sombra.
- **Do** acotar el CSS de una superficie nueva bajo su propia clase raíz, como `CSS_QE` hace con `.qe`, para que las ediciones publicadas no cambien un píxel.
- **Do** recordar que `CSS` es un f-string y necesita llaves dobladas (`{{`/`}}`), mientras `CSS_QE` es una cadena normal con llaves sencillas. Confundirlas rompe la generación.
- **Do** mantener el bloque `@media print` al día: cada pieza nueva decide si se imprime o se oculta.

### Don't:

- **Don't** poner prosa corrida ni etiquetas pequeñas en `ink3` (3,79:1) ni en el ámbito `ai` (3,45:1).
- **Don't** usar el color como único portador de un estado: si se quita el color, el estado tiene que seguir leyéndose.
- **Don't** añadir sombras de elevación en reposo. Lo plano es el sistema, no una carencia.
- **Don't** introducir un séptimo color temático ni un acento nuevo junto al rojo de cinta.
- **Don't** escribir frases en Inter: la sans rotula, la serifa narra.
- **Don't** usar guiones largos ni medios en ningún texto; `web.py` aborta la generación.
- **Don't** calcular a mano una cifra que se puede contar: recuentos, totales y fechas futuras salen del generador (`counts`, `proxima()`).
- **Don't** añadir glifos tipográficos, emoji o iconos de paquete donde toca un SVG de `IC`.
- **Don't** meter contenido de una edición dentro de `web.py`; el contenido vive en los ficheros de contenido.
- **Don't** tocar las clases no acotadas del mundo heredado (`.leyenda`, `.ficha`, `.ed`) desde una superficie nueva sin acotar la regla bajo su clase raíz.

## Deriva observada, no canonizada

Lo siguiente **está en el artefacto publicado pero no es sistema**. Se deja escrito aquí, y
fuera de las secciones normativas, para que ninguna superficie futura lo herede como regla. No
se ha reparado nada de esto a propósito: estas piezas renderizan idénticas en las siete
ediciones publicadas y arreglarlas no formaba parte de esta extensión.

- **Texto funcional por debajo de 11px.** `.mast-sub` y `.ed-n` fijan texto funcional en **10,5px** (`CSS`, reglas de `.mast-sub` y `.ed-n`). El mismo 10,5px aparece en el resto de la familia de rótulos (`.et`, `.card .ci`). El suelo del sistema para texto funcional es 11px, y la superficie nueva lo respeta (`.pl-est` y `.ficha dt` a 11px).
- **`ink3` en texto pequeño.** `.mast-sub` pinta su tira de datos de edición en `ink3`, 3,79:1 sobre papel, a 10,5px. Contradice la regla del color que no porta. `/que-es` lo corrige **solo para su superficie** con `.qe .mast-sub{color:var(--ink2)}`; la cabecera de las ediciones sigue como estaba.
- **Filete de 5px en `.clave`.** El bloque de clave de portada lleva `border-left:5px solid var(--es)` con radio `0 4px 4px 0`. Es el único filete de color de ese grosor del sistema; el resto se queda en 3px (`.warn`). No se extiende.
- **Rótulos de entradilla (`.ante`).** Cada pestaña de una edición abre con un rótulo versalita suelto sobre el titular («Lo más importante de la semana», «Calendario», «Hemeroteca»). Es un elemento de antetítulo: **no es un componente del sistema** y no se documenta como tal. `/que-es` no lo usa, y una superficie nueva tampoco debe usarlo.
- **Colisión de nombre en `.leyenda`.** La clave del mapa de las ediciones y la leyenda de la cinta de `/que-es` comparten el nombre de clase. La nueva está acotada (`.qe .leyenda`); la antigua no. Conviven solo porque la acotación va en un sentido. Un tercer uso de `.leyenda` rompería una de las dos.
