# -*- coding: utf-8 -*-
"""Mapa de cuadricula de la UE-27 por norma. Codificacion compuesta:
color + simbolo + etiqueta, para que sea legible con daltonismo (rojo y verde
estan a delta-E 4.1 en deuteranopia, asi que el color NO puede ir solo)."""

EST = {  # clave: (etiqueta, color, simbolo, relleno)
 "completa": ("Traspuesta o en vigor", "#0ca30c", "&#10003;", "solido"),
 "parcial":  ("Parcial o pendiente",   "#fab219", "&#9680;", "rayado"),
 "ninguna":  ("Sin medidas",           "#ec835a", "&#8211;", "hueco"),
 "tjue":     ("Demandado ante el TJUE","#d03b3b", "&#10007;", "solido"),
 "desc":     ("Sin dato público",      "#898781", "?",        "hueco"),
}

REJILLA = [
 [None,None,None,None,None,"FI",None],
 [None,None,"IE",None,"SE","EE",None],
 [None,None,None,"DK",None,"LV",None],
 [None,None,"NL","DE","PL","LT",None],
 [None,"BE","LU","CZ","SK",None,None],
 ["PT","ES","FR","AT","HU","RO",None],
 [None,None,"IT","SI","HR","BG",None],
 [None,None,"MT",None,"GR","CY",None],
]
PAIS = {"BE":"Bélgica","BG":"Bulgaria","CZ":"Chequia","DK":"Dinamarca","DE":"Alemania",
 "EE":"Estonia","IE":"Irlanda","GR":"Grecia","ES":"España","FR":"Francia","HR":"Croacia",
 "IT":"Italia","CY":"Chipre","LV":"Letonia","LT":"Lituania","LU":"Luxemburgo","HU":"Hungría",
 "MT":"Malta","NL":"Países Bajos","AT":"Austria","PL":"Polonia","PT":"Portugal","RO":"Rumanía",
 "SI":"Eslovenia","SK":"Eslovaquia","FI":"Finlandia","SE":"Suecia"}

NORMAS = [
 ("nis2","NIS2","Directiva (UE) 2022/2555","directiva",
  "Transposición nacional obligatoria. El plazo venció el 17 de octubre de 2024.",
  "Países Bajos puso su ley en vigor el 15 de agosto de 2026 y sale del grupo, que queda en tres: Irlanda, España y Francia. Otros nueve países siguen en fase de dictamen motivado. La retirada formal del asunto está pendiente de que se notifiquen las medidas a la Comisión."),
 ("cer","CER","Directiva (UE) 2022/2557","directiva",
  "Transposición nacional obligatoria. El plazo venció el 17 de octubre de 2024 y la identificación de entidades críticas, el 17 de julio de 2026.",
  "Países Bajos puso su ley en vigor el 15 de agosto de 2026 y los remitidos al Tribunal de Justicia bajan de siete a seis. No existe cifra pública de cuántos Estados completaron la identificación de entidades críticas antes del plazo del 17 de julio."),
 ("dora","DORA","Reglamento (UE) 2022/2554","reglamento",
  "Aplicable directamente en los 27 desde el 17 de enero de 2025. Lo que varía es el régimen sancionador nacional del capítulo VII.",
  "España tiene carta de emplazamiento desde julio de 2026 por no notificar el régimen sancionador. El proyecto 121/000105 no es solo retraso interno: es un procedimiento de infracción vivo."),
 ("ia","Reglamento de IA","Reglamento (UE) 2024/1689","reglamento",
  "Aplicable directamente en los 27. Lo que varía es la designación de autoridades nacionales, que debía notificarse antes del 2 de agosto de 2025.",
  "La lista oficial de la Comisión lleva congelada desde septiembre de 2025 con solo ocho países. El reparto de aquí procede de un rastreador que cubre los 27 y está más actualizado."),
 ("cra","CRA","Reglamento (UE) 2024/2847","reglamento",
  "Aplicable directamente en los 27. Lo que varía es la designación de autoridades de vigilancia del mercado y notificantes.",
  "El vacío es el dato. A menos de un mes del 11 de septiembre de 2026 ni la Comisión ni ENISA publican designaciones por país, no hay ningún organismo notificado en toda la UE y la plataforma de notificación no estaba operativa en junio."),
]

D = {
"nis2": {
 "BE":("completa","Ley de 26 de abril de 2024 y Real Decreto de junio. Transpuso en plazo, nunca tuvo expediente."),
 "BG":("parcial","Ley de modificación de febrero de 2026. Solo una medida notificada, expediente activo."),
 "CZ":("completa","Ley 264/2025 de ciberseguridad. 83 medidas notificadas, expediente cerrado en julio de 2026."),
 "DK":("completa","Ley de mayo de 2025. Expediente cerrado en enero de 2026."),
 "DE":("parcial","NIS2UmsuCG publicada en diciembre de 2025, con leyes de los Länder. Expediente aún activo."),
 "EE":("parcial","Modificación de la ley de ciberseguridad de diciembre de 2025. Expediente activo."),
 "IE":("tjue","Cero medidas notificadas. Demandada el 8 de julio de 2026 con petición de sanciones."),
 "GR":("completa","Ley 5160/2024. Expediente cerrado en febrero de 2025 sin llegar a dictamen motivado."),
 "ES":("tjue","Cero medidas notificadas. Demandada el 8 de julio de 2026 con suma a tanto alzado y multa coercitiva diaria."),
 "FR":("tjue","15 medidas notificadas, todas anteriores a 2023. Ninguna norma de transposición. Demandada el 8 de julio de 2026."),
 "HR":("completa","Ley de ciberseguridad de febrero de 2024. Sin expediente de infracción."),
 "IT":("completa","Decreto legislativo 138/2024, de 4 de septiembre. Sin expediente."),
 "CY":("completa","Ley modificativa de abril de 2025. Expediente cerrado en octubre de 2025."),
 "LV":("completa","Ley nacional de ciberseguridad de julio de 2024. Expediente cerrado en enero de 2026."),
 "LT":("completa","Ley de ciberseguridad modificada en julio de 2024. Expediente cerrado en febrero de 2025."),
 "LU":("completa","Ley de 5 de mayo de 2026. Expediente cerrado el mismo día de las demandas."),
 "HU":("parcial","Ley LXIX de 2024 y decreto de desarrollo. 39 medidas, expediente activo."),
 "MT":("completa","Legal Notice de abril de 2025. Expediente cerrado en octubre de 2025."),
 "NL":("completa","Cyberbeveiligingswet en vigor desde el 15 de agosto de 2026. Unas 8.000 organizaciones en 18 sectores, con notificación en 24 horas desde el primer día."),
 "AT":("parcial","Ley federal NISG de diciembre de 2025. Expediente activo pese a la ley."),
 "PL":("parcial","Ley de enero de 2026 que modifica la ley KSC. Expediente activo."),
 "PT":("parcial","Decreto-Ley 125/2025, de 4 de diciembre. Solo dos medidas, expediente activo."),
 "RO":("completa","Ordenanza de urgencia de diciembre de 2024. Expediente cerrado en octubre de 2025."),
 "SI":("completa","Ley de seguridad de la información de junio de 2025. Expediente cerrado en enero de 2026."),
 "SK":("completa","Expediente cerrado en octubre de 2025, pero sin medidas posteriores a 2022 en el registro. Es la ficha menos fiable."),
 "FI":("parcial","Ley de ciberseguridad 124/2025. 13 medidas, expediente aún activo."),
 "SE":("parcial","Ley de ciberseguridad de diciembre de 2025. Expediente activo pese a estar en vigor."),
},
"cer": {
 "AT":("completa","Ley RKEG de 2025. Estrategia y análisis de riesgos de enero de 2026; falta el reglamento de desarrollo."),
 "BE":("completa","Ley de 19 de diciembre de 2025, publicada en enero de 2026."),
 "BG":("tjue","Proyecto en consulta pública, no adoptado. Remitida al Tribunal de Justicia con petición de sanciones."),
 "CY":("completa","Reglamento de protección civil sobre resiliencia de entidades críticas de 2025."),
 "CZ":("completa","Ley 266/2025 sobre resiliencia de la infraestructura crítica. 27 medidas notificadas."),
 "DE":("completa","KRITIS-Dachgesetz en vigor desde marzo de 2026, pero el reglamento de desarrollo seguía sin cerrarse y aplazó el registro."),
 "DK":("completa","Ley 433/2025. Operativa desde 2025, de los Estados más avanzados."),
 "EE":("completa","Reforma de la ley de emergencias de octubre de 2024. 23 medidas notificadas."),
 "GR":("completa","Ley 5236/2025, de octubre. Sanciones de uno a diez millones de euros."),
 "ES":("tjue","Anteproyecto sin aprobar. Dictamen motivado en julio de 2025 y remisión al Tribunal de Justicia en 2026."),
 "FI":("completa","Ley 310/2025 sobre protección de la infraestructura crítica. En aplicación desde 2025."),
 "FR":("tjue","Proyecto aprobado en el Senado en marzo de 2025, bloqueado en la Asamblea con más de 500 enmiendas."),
 "HR":("completa","Ley de infraestructura crítica de junio de 2025."),
 "HU":("completa","Ley LXXXIV de 2024. 68 medidas notificadas, el mayor número de la UE."),
 "IE":("completa","Reglamento de 2024, notificado antes de vencer el plazo."),
 "IT":("completa","Decreto legislativo 134/2024, de 4 de septiembre, adoptado antes del plazo."),
 "LT":("completa","15 medidas notificadas, sin ley CER única. Ficha de confianza menor."),
 "LU":("tjue","Sin norma nacional ni proyecto público identificado. Remitida al Tribunal de Justicia."),
 "LV":("completa","Reforma de la ley de seguridad nacional y reglamentos de enero de 2026. Transposición fragmentada."),
 "MT":("completa","Orden sobre resiliencia de entidades e infraestructuras críticas de enero de 2026."),
 "NL":("completa","Wet weerbaarheid kritieke entiteiten en vigor desde el 15 de agosto de 2026, con unas 500 entidades críticas alcanzadas."),
 "PL":("tjue","Proyecto de reforma de la ley de gestión de crisis sin adoptar. Procedimiento judicial desde mayo de 2026."),
 "PT":("completa","Decreto-Ley 22/2025, de 19 de marzo, que transpone expresamente la Directiva."),
 "RO":("completa","Ley 294/2024 y decreto de desarrollo. No confundir con la ordenanza que transpone NIS2."),
 "SE":("tjue","Proyecto presentado al Parlamento el 14 de julio de 2026, con entrada en vigor prevista para enero de 2027."),
 "SI":("completa","Ley de infraestructura crítica de 2024, que cita expresamente la Directiva."),
 "SK":("completa","Ley 367/2024, en vigor desde el 1 de enero de 2025."),
},
"dora": {c: ("completa","Medidas nacionales del capítulo VII notificadas a la Comisión.") for c in PAIS},
"ia": {
 "CY":("completa","Comisionado de Comunicaciones como autoridad de vigilancia, notificante y punto de contacto."),
 "DK":("completa","Ley 467, en vigor desde agosto de 2025. Agencia Danesa de Administración Digital."),
 "FI":("completa","Ley 1377/2025, en vigor desde enero de 2026. Modelo descentralizado."),
 "HU":("completa","Decreto gubernamental 344/2025."),
 "IE":("completa","Reglamento de 2025 con quince organismos designados y oficina nacional prevista."),
 "IT":("completa","Ley 132/2025, en vigor desde octubre. Primer Estado con ley nacional de IA."),
 "LT":("completa","Autoridad reguladora de comunicaciones y agencia de innovación."),
 "MT":("completa","Autoridad de innovación digital como vigilancia y notificante."),
 "SI":("completa","Legislación nacional en vigor desde noviembre de 2025."),
 "CZ":("parcial","Propuesta legislativa sin aprobar."),
 "DE":("parcial","Proyecto aprobado por el Gabinete en febrero de 2026, pendiente de las cámaras."),
 "ES":("parcial","AESIA designada y notificada, pero la ley orgánica que le da competencias formales sigue pendiente."),
 "FR":("parcial","Autoridad de consumo como coordinadora, con propuesta de modelo descentralizado de más de doce autoridades."),
 "LV":("parcial","Centro de protección del consumidor como punto de contacto; notificante solo recomendada."),
 "LU":("parcial","Autoridad de protección de datos propuesta; proyecto de ley sin aprobar."),
 "NL":("parcial","Proyecto de abril de 2026 con diez autoridades sectoriales propuestas."),
 "PL":("parcial","Ley aprobada por la cámara baja en junio de 2026, pendiente del Senado."),
 "PT":("parcial","Regulador de comunicaciones anunciado, notificante sin identificar."),
 "RO":("parcial","Regulador de comunicaciones propuesto en marzo de 2026."),
 "SE":("parcial","Autoridad de correos y telecomunicaciones propuesta como coordinadora."),
 "SK":("parcial","Oficina para la integridad digital como coordinadora."),
 "AT":("ninguna","Sin designar. Se espera una mesa de ayuda de IA en el regulador de telecomunicaciones."),
 "BE":("ninguna","Sin designar. Se espera el regulador de telecomunicaciones según el acuerdo de coalición."),
 "BG":("ninguna","Sin designar. El ministerio de gobernanza electrónica solo coordina."),
 "EE":("ninguna","Sin designar."),
 "GR":("ninguna","Sin designar. Proyecto esperado para junio de 2026."),
 "HR":("ninguna","Sin designar."),
},
"cra": {
 "FI":("completa","Ley nacional de ciberresiliencia en vigor desde el 1 de junio de 2026, con autoridad de vigilancia y notificante designadas."),
 "DE":("parcial","Proyecto de aplicación aprobado por el Consejo de Ministros federal en abril de 2026, con el BSI designado. No en vigor."),
},
}
# DORA: solo tres Estados con expediente abierto
for c, n in [("ES","Carta de emplazamiento de julio de 2026 por no notificar el régimen sancionador. Las autoridades operan por el artículo 46, pero no hay sanciones."),
             ("FR","Ninguna medida comunicada. Los supervisores actúan por el artículo 46, pero falta régimen sancionador."),
             ("LV","Transpuso la directiva de acompañamiento pero no notificó el capítulo VII del Reglamento.")]:
    D["dora"][c] = ("parcial", n)
# CRA: el resto sin dato publico
for c in PAIS:
    D["cra"].setdefault(c, ("desc","Ni la Comisión ni ENISA publican designaciones por país."))

for k in D:
    assert len(D[k]) == 27, (k, len(D[k]))
    for c in D[k]: assert c in PAIS, (k, c)
print("mapa: 5 normas x 27 países, datos completos")
for nid, nom, _, tipo, _, _ in NORMAS:
    from collections import Counter
    c = Counter(v[0] for v in D[nid].values())
    print(f"  {nom:18s} {tipo:10s}", dict(c))
