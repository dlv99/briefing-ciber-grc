# -*- coding: utf-8 -*-
"""Despliegue de siglas. EXPANDIR se escribe entero la primera vez que aparece
en cada asunto; el resto queda como <abbr> con el significado al pasar el raton."""
import re

EXPANDIR = {
 "NIS2": "Directiva de seguridad de las redes y sistemas de información",
 "DORA": "Reglamento de resiliencia operativa digital del sector financiero",
 "MUS": "Mecanismo Único de Supervisión, la supervisión bancaria del Banco Central Europeo",
 "SREP": "proceso de revisión y evaluación supervisora, el examen anual del supervisor bancario",
 "TJUE": "Tribunal de Justicia de la Unión Europea",
 "CSIRT": "equipo de respuesta a incidentes de seguridad informática",
 "PYME": "pequeña y mediana empresa",
 "RDL": "Real Decreto-ley",
 "INCIBE": "Instituto Nacional de Ciberseguridad",
 "CRA": "Reglamento de Ciberresiliencia",
 "ENS": "Esquema Nacional de Seguridad",
 "CCN": "Centro Criptológico Nacional",
 "CNMV": "Comisión Nacional del Mercado de Valores",
 "AESIA": "Agencia Española de Supervisión de la Inteligencia Artificial",
 "EIOPA": "Autoridad Europea de Seguros y Pensiones de Jubilación",
 "ESMA": "Autoridad Europea de Valores y Mercados",
 "EBA": "Autoridad Bancaria Europea",
 "BCE": "Banco Central Europeo",
 "JST": "Equipo Conjunto de Supervisión",
 "JERS": "Junta Europea de Riesgo Sistémico",
 "AES": "Autoridades Europeas de Supervisión",
 "CEPD": "Comité Europeo de Protección de Datos",
 "CPSTIC": "Catálogo de Productos y Servicios de Seguridad de las Tecnologías de la Información y la Comunicación",
 "KEV": "catálogo de vulnerabilidades explotadas conocidas de la agencia estadounidense de ciberseguridad",
 "EPSS": "sistema de puntuación de probabilidad de explotación",
 "RMM": "monitorización y gestión remota de equipos",
 "MSSP": "proveedor de servicios gestionados de seguridad",
 "MDR": "detección y respuesta gestionadas",
 "PQC": "criptografía poscuántica",
 "IAF": "International Accreditation Forum, el foro internacional de acreditación",
 "ILAC": "International Laboratory Accreditation Cooperation",
 "MLA": "acuerdo multilateral de reconocimiento",
 "MRA": "acuerdo de reconocimiento mutuo",
 "CASP": "proveedores de servicios de criptoactivos",
 "EUMSS": "esquema europeo para servicios gestionados de seguridad",
 "EUCS": "esquema europeo de certificación para servicios en la nube",
 "EUCC": "esquema europeo de certificación de criterios comunes",
 "CSA2": "revisión del Reglamento de Ciberseguridad",
 "CER": "resiliencia de las entidades críticas",
 "ITS": "Instrucción Técnica de Seguridad",
 "CET1": "capital de nivel 1 ordinario",
 "CVSS": "sistema común de puntuación de vulnerabilidades",
 "SOC": "centro de operaciones de seguridad",
 "XDR": "detección y respuesta extendidas",
 "NGFW": "cortafuegos de nueva generación",
 "CNPIC": "Centro Nacional de Protección de Infraestructuras Críticas",
 "DGSFP": "Dirección General de Seguros y Fondos de Pensiones",
 "SEPD": "Supervisor Europeo de Protección de Datos",
 "INES": "Informe Nacional del Estado de Seguridad",
 "BOCG": "Boletín Oficial de las Cortes Generales",
 "DOUE": "Diario Oficial de la Unión Europea",
 "PCE": "Perfil de Cumplimiento Específico",
}
SOLO_ABBR = {
 "TIC": "tecnologías de la información y la comunicación",
 "AEPD": "Agencia Española de Protección de Datos",
 "RGPD": "Reglamento General de Protección de Datos",
 "BOE": "Boletín Oficial del Estado",
 "IA": "inteligencia artificial",
}
TODAS = {**EXPANDIR, **SOLO_ABBR}
_RX = re.compile(r"\b(" + "|".join(sorted(TODAS, key=len, reverse=True)) + r")\b")

def marcar(texto, vistas, modo="web", contexto=None):
    """Despliega siglas en un fragmento de HTML sin tocar el interior de las etiquetas.
    Si el texto ya explica la sigla por su cuenta, no se duplica la glosa."""
    ctx = (contexto if contexto is not None else texto).lower()
    partes = re.split(r"(<[^>]+>)", texto)
    def rep(m):
        s = m.group(1)
        if s in vistas:
            return s
        vistas.add(s)
        if s in EXPANDIR:
            exp = EXPANDIR[s]
            clave = exp.split(",")[0].lower()[:20]
            ya_explicada = clave in ctx
            if modo == "web":
                glosa = "" if ya_explicada else f' <span class="exp">({exp})</span>'
                return f'<abbr title="{exp}">{s}</abbr>{glosa}'
            return s if ya_explicada else f'{s} ({exp})'
        return f'<abbr title="{TODAS[s]}">{s}</abbr>' if modo == "web" else s
    for i, p in enumerate(partes):
        if not p.startswith("<"):
            partes[i] = _RX.sub(rep, p)
    return "".join(partes)
