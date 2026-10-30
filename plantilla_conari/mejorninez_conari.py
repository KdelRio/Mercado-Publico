import sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from conari_pdf import *
OUT=sys.argv[1]; COD="1177296-128-COT26"
NETO=int(sys.argv[2]) if len(sys.argv)>2 else 3000000
iva=round(NETO*0.19); total=NETO+iva
f=lambda v:"$"+f"{v:,}".replace(",",".")
FIRMA=lambda: signature("María Inés Cisterna Escobar","Socia fundadora y administradora","Studios Conari SpA · RUT 78.465.252-1",img=os.path.join(A,"firma_maria.png"))
H=lambda t:Paragraph(t.upper(),sty["h"])

def gantt(w):
    acts=[("Reunión de inicio y acceso a los instrumentos",[1]),
          ("C1 · Diagnóstico técnico y funcional (UEFAA y FAE)",[1,2,3]),
          ("C1 · Consulta cuantitativa y cualitativa nacional y regional",[2,3]),
          ("C2 · Optimización, anti-duplicados y diccionario de datos",[3,4]),
          ("C3 · Indicadores y fichas técnicas",[4,5]),
          ("C4 · Paneles automatizados por instrumento",[5,6,7]),
          ("C5 · Comparabilidad y panel integrado",[6,7]),
          ("C4 · Capacitaciones grabadas, cápsulas y manuales",[7,8]),
          ("Cierre, migración de datos y certificado de eliminación",[8])]
    hit={3:"C1",4:"C2",5:"C3",7:"C4·C5",8:"Final"}
    data=[["Actividad"]+[f"S{i}" for i in range(1,9)]]
    for a,_ in acts: data.append([Paragraph(a,sty["small"])]+[""]*8)
    data.append([Paragraph("<b>Entrega de productos</b>",sty["small"])]+[Paragraph(f"<b>{hit.get(i,'')}</b>",ParagraphStyle("c",parent=sty["small"],fontSize=6.5,alignment=1)) for i in range(1,9)])
    cw=(w-7.4*cm)/8
    t=Table(data,colWidths=[7.4*cm]+[cw]*8,repeatRows=1)
    st=[("GRID",(0,0),(-1,-1),0.6,LINEG),("BACKGROUND",(0,0),(-1,0),CREAM),("FONTNAME",(0,0),(-1,0),"NSB"),("FONTSIZE",(0,0),(-1,0),7.5),
        ("TEXTCOLOR",(0,0),(-1,0),GOLD),("ALIGN",(1,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),("BACKGROUND",(0,len(data)-1),(-1,len(data)-1),CREAM)]
    for r,(_,ws) in enumerate(acts,1):
        for s in ws: st.append(("BACKGROUND",(s,r),(s,r),NAVY2))
    t.setStyle(TableStyle(st)); return t

doc=Doc(os.path.join(OUT,f"Propuesta_Tecnica_Economica_{COD}_StudiosConari.pdf"),f"Propuesta técnica y económica · {COD}","Studios Conari · Propuesta técnica y económica")
w=doc.width; E=[]
E+=cover("Propuesta técnica y económica","INSTRUMENTOS «RUTA DE LA FAMILIA» Y<br/>«MONITOREO FAMILIAS DE ACOGIDA EXTERNA»",
 f"Compra Ágil {COD} · Servicio Nacional de Protección Especializada a la Niñez y Adolescencia",
 [("Oferente","Studios Conari SpA<br/>RUT 78.465.252-1<br/>Empresa de menor tamaño · Sello Empresa Mujer"),
  ("Servicio","Diagnóstico, optimización, indicadores,<br/>paneles en Excel, panel integrado<br/>y capacitaciones grabadas"),
  ("Oferta",f"{f(NETO)} neto<br/>{f(total)} IVA incluido<br/>Plazo: 60 días corridos")],
 ("Contacto del oferente","María Inés Cisterna Escobar, socia fundadora y administradora · postulaciones@studiosconari.cl · +56 9 8759 8952 · Colo Colo 379, oficina 706, Concepción, Región del Biobío."),
 "30 de octubre de 2026 · Validez de la oferta: 30 días corridos<br/><font color='#a8780f'>studiosconari.cl</font>",w)

E+=section("01","Oferta económica","Valor total del servicio","Precio a suma alzada por los cinco componentes y todos sus productos, para ambos instrumentos")
E.append(table([["Ítem","Valor neto"],
 ["Consultoría: diagnóstico, optimización, indicadores y panel de visualización de los instrumentos «Ruta de la Familia» (UEFAA) y «Monitoreo Familias de Acogida Externa» (FAE), más panel integrado, capacitaciones grabadas, cápsulas y manuales",f(NETO)],
 ["Total neto",f(NETO)],["IVA 19 %",f(iva)],["Total con IVA",f(total)]],[w-3.6*cm,3.6*cm],bold_last=1,right_cols=(1,)))
E.append(Spacer(1,6))
E.append(callout("Condiciones","Un solo pago contra recepción conforme, con factura a nombre del Servicio (RUT 62.000.890-7) y referencia a la OC. Sin licencias ni costos adicionales: todo se desarrolla en Excel, la herramienta institucional disponible.",w))
E.append(Spacer(1,10))
E+=section("02","Enfoque","Cómo abordamos la consultoría",None)
E.append(cards([("Preservar y mejorar","No se reemplaza el SIS ni se crea otra plataforma. Se mejora lo que existe, sin perder registros ni alterar la base original."),
 ("Diferenciado y luego común","UEFAA y FAE se trabajan por separado, con su contraparte y aprobación. El panel integrado llega al final, sin mezclar universos."),
 ("Autonomía del Servicio","Todo queda documentado y parametrizable: los equipos actualizan, amplían y corrigen sin depender de la consultora.")],w))
E.append(Spacer(1,8))
E.append(H("Herramienta y metodología técnica"))
E+=bullets(["<b>Microsoft Excel</b> (versión institucional): tablas estructuradas, rangos dinámicos, listas desplegables administrables desde una hoja de catálogos, validación de datos y formato condicional para alertas.",
 "<b>Power Query</b> (incluido en Excel) para consolidar regiones y depurar duplicados de forma repetible, sin macros obligatorias.",
 "<b>Tablas y gráficos dinámicos, segmentaciones y escalas de tiempo</b> para los paneles: se actualizan al cargar datos nuevos.",
 "<b>Control de calidad:</b> casos de prueba por regla de validación, revisión de fórmulas y prueba de migración con una copia anonimizada antes de tocar la versión vigente."])
E.append(PageBreak())
E+=section("03","Metodología","Trabajo por componente","Los componentes 1 a 4 se ejecutan por separado para UEFAA y FAE; el 5 se desarrolla en conjunto")
E.append(table([["Componente","Metodología","Productos"],
 ["<b>1 · Diagnóstico técnico y funcional</b>","Revisión de estructura, campos, fórmulas, validaciones, rangos fijos, sobrescritura, rendimiento y consolidación, contrastada con las Orientaciones Técnicas FAE y los Lineamientos UEFAA. Pruebas con usuarios y revisión controlada de registros sobre una copia. Consulta: encuesta en línea (Microsoft Forms o similar) a usuarios nacionales y regionales y entrevistas o grupos focales por videollamada; muestra, instrumentos y calendario se acuerdan con cada contraparte.","Informe de diagnóstico (1 por instrumento). Informe de sistematización de la consulta (1 por instrumento)."],
 ["<b>2 · Optimización</b>","Propuesta de mejoras priorizada y acordada. Tablas dinámicas, fórmulas simples y protegidas, fechas estándar, catálogos administrables, secuencia de hitos, obligatoriedad por etapa, alertas claras, registro de fecha y responsable, bitácora de cambios y control de versiones. Anti-duplicados: llave de identificación de la familia y reglas para distinguir duplicado, actualización, traslado y reingreso, con tratamiento trazable de los casos existentes. Migración íntegra validada con conteos de control.","Informe de propuestas de ajuste (1 por instrumento). Versión optimizada y operativa (2). Diccionario de datos, catálogos y reglas (1 por instrumento)."],
 ["<b>3 · Indicadores</b>","Indicadores por etapa (contactabilidad, evaluación formativa, espera activa, matching, post acogimiento), con nivel nacional y regional, sin doble conteo y comparables entre períodos, regiones y proyectos.","Informe de propuesta de indicadores (1 por instrumento). Ficha técnica por indicador."],
 ["<b>4 · Paneles</b>","Panel en Excel tipo semáforo, que se actualiza al cargar datos: filtros por período y territorio, distribución por etapa y estado, tasas de avance, tiempos de gestión, desistimientos, familias enlazadas, calidad del registro y alertas de casos sin movimiento. Umbrales documentados y parametrizables. Capacitación por videollamada, grabada y editada en cápsulas temáticas cortas.","Panel (1 por instrumento). Manual ilustrado (1 por instrumento). Capacitación (1 por instrumento), grabación y cápsulas."],
 ["<b>5 · Panel integrado</b>","Comparación de campos, definiciones y brechas; criterios de homologación y reglas de vinculación sin doble conteo, manteniendo explícitas las diferencias entre UEFAA y FAE. Indicadores transversales y panel integrado con filtros, vistas agregadas, alertas y trazabilidad.","Informe de comparabilidad e indicadores comunes. Panel único integrado."]],
 [3.2*cm,w-7.6*cm,4.4*cm]))
E.append(PageBreak())
E+=section("04","Carta Gantt","Hitos y plazos","Ocho semanas (60 días corridos) desde la aceptación de la orden de compra, coherente con el cronograma referencial del Servicio")
E.append(gantt(w))
E.append(Spacer(1,6))
E.append(Paragraph("Reuniones de avance semanales por videollamada con cada contraparte; presenciales en Alameda 1449, Santiago, cuando el Servicio lo estime necesario.",sty["small"]))
E.append(Spacer(1,10))
E+=section("05","Equipo","Equipo consultor",None)
E.append(table([["Integrante","Perfil profesional","Rol en la consultoría"],
 ["<b>Kevin Alexis del Río Morgado</b>","Ingeniero en Informática (Duoc UC). Más de 3 años como Jefe de Informática en DailyFresh (2022–2025), donde implementó la plataforma de Business Intelligence: modelos de datos, ETL, indicadores y tableros en Power BI, SAP BusinessObjects y Excel avanzado. Certificado de Análisis de Datos de Google.","Jefe de proyecto y líder técnico: diagnóstico de los instrumentos, optimización, anti-duplicados, diccionario de datos, indicadores y paneles."],
 ["<b>María Inés Cisterna Escobar</b>","Matrona (USS 2018) con experiencia en salud pública y programas de infancia; realizó material educativo para Chile Crece Contigo. Full Stack Java (SENCE, 480 h). Diseño gráfico, ilustración y producción de cápsulas.","Consulta a usuarios, pertinencia técnica de indicadores con las orientaciones, manuales ilustrados, capacitaciones grabadas y cápsulas."]],
 [3.6*cm,w-8.2*cm,4.6*cm]))
E.append(PageBreak())
E+=section("06","Confidencialidad","Protocolo de confidencialidad y manejo de la información","Conforme a la Ley N.º 19.628 sobre Protección de la Vida Privada y la Ley N.º 20.285 sobre Acceso a la Información Pública")
E.append(table([["Etapa","Medida"],
 ["Acceso","Solo los dos integrantes del equipo, con compromiso de confidencialidad firmado. Ninguna otra persona accede a los datos."],
 ["Datos mínimos","Para diseñar y probar se usan copias con datos anonimizados o seudonimizados. Los datos identificables se usan solo cuando son indispensables (por ejemplo, la migración) y siempre en copias, sin alterar la base original."],
 ["Transferencia","Archivos solo por los canales institucionales que indique el Servicio (correo institucional o carpeta compartida del Servicio). No se usan correos personales ni servicios públicos de transferencia."],
 ["Almacenamiento","Equipos con disco cifrado, contraseña y bloqueo automático; archivos con contraseña. Sin copias en dispositivos extraíbles ni en nubes personales."],
 ["Uso","La información se usa exclusivamente para los productos contratados. Prohibido su uso, comunicación, reproducción o tratamiento con otros fines, incluido el uso en portafolios o en herramientas de IA."],
 ["Grabaciones","Las capacitaciones se graban con datos de ejemplo, sin mostrar información de familias reales."],
 ["Incidentes","Cualquier incidente o sospecha de acceso no autorizado se informa a las contrapartes dentro de 24 horas."],
 ["Eliminación","Dentro de 90 días corridos desde la recepción conforme (o antes, si ya no es necesaria), se eliminan de forma segura e irreversible la información, sus copias, respaldos y temporales, y se entrega una declaración que identifica la información eliminada, la fecha y el mecanismo usado."]],[3*cm,w-3*cm]))
E.append(Spacer(1,10))
E+=section("07","Condiciones","Condiciones de la oferta",None)
E+=bullets(["Trabajo remoto desde Concepción, con reuniones presenciales en Santiago cuando el Servicio lo requiera.",
 "Todos los productos (informes, instrumentos, paneles, manuales, grabaciones y cápsulas) quedan de propiedad del Servicio.",
 "Servicio 100 % digital: elaboración, revisión y entrega por medios electrónicos, sin impresión."])
E.append(FIRMA()); doc.build(E)

# CV y experiencia del equipo
doc=Doc(os.path.join(OUT,f"CV_y_Experiencia_Equipo_{COD}_StudiosConari.pdf"),f"CV y experiencia del equipo · {COD}","Studios Conari · CV y experiencia del equipo",footer_right="Antecedentes"); w=doc.width; E=[]
E+=section("CV","Equipo consultor","Currículum y experiencia del equipo","Reseña de trayectoria y experiencia en proyectos similares")
E.append(H("Kevin Alexis del Río Morgado · Jefe de proyecto y líder técnico"))
E.append(Paragraph("Ingeniero en Informática (Duoc UC, 2018–2023), especializado en análisis de datos y Business Intelligence. Socio fundador, administrador y director técnico de Studios Conari SpA (desde julio de 2026).",sty["body"]))
E.append(Spacer(1,4))
E.append(table([["Período","Cargo y experiencia"],
 ["Nov. 2022 – 2025","<b>Jefe de Informática · DailyFresh</b> (industria manufacturera de alimentos). Diseño, modelamiento e implementación de la plataforma de BI corporativa: ETL con Power Query desde SAP y fuentes operativas, modelos relacionales, medidas DAX y tableros de indicadores para gerencia y jefaturas (finanzas, comercial, metas, personas, inventario con alertas por umbral, producción y calidad). Rediseño del proceso de captura de datos con un formulario estandarizado y validado, que redujo los errores de registro y fortaleció la trazabilidad para auditorías."],
 ["Mar. – jul. 2022","Técnico en redes y telecomunicaciones · Inversiones Terabytes Ltda. (práctica profesional)."],
 ["Ene. – may. 2017","Técnico de mantención · Mekano (soporte de sistemas de punto de venta)."]],[3*cm,w-3*cm]))
E.append(Spacer(1,4))
E.append(Paragraph("<b>Certificaciones:</b> Certificado Profesional de Análisis de Datos de Google (Coursera, 2026); SAP BusinessObjects Essentials (2024); certificaciones de especialidad Duoc UC en Inteligencia de Negocios, Análisis y Desarrollo de Modelos de Datos, Calidad de Software y Gestión de Proyectos Informáticos. <b>Herramientas:</b> Excel avanzado, Power Query, Power BI (DAX), Tableau, SAP BusinessObjects, SQL, Python.",sty["small"]))
E.append(Spacer(1,4))
E.append(Paragraph("<b>Portafolio verificable:</b> <link href='https://github.com/KdelRio/Magic-Foods-BI'><u>github.com/KdelRio/Magic-Foods-BI</u></link> — reconstrucción, con datos ficticios para resguardar la confidencialidad de DailyFresh, del trabajo de BI realizado: 8 libros de Excel con diccionario de datos y más de 80.000 fórmulas verificadas, 7 dashboards en Power BI y su réplica en Tableau, y presentaciones ejecutivas con recomendaciones. Sitio: <link href='https://kdelrio.github.io'><u>kdelrio.github.io</u></link>.",sty["small"]))
E.append(Spacer(1,10))
E.append(H("María Inés Cisterna Escobar · Consulta a usuarios, manuales y capacitación"))
E.append(Paragraph("Matrona (Universidad San Sebastián, 2018), con experiencia en salud pública y en programas de apoyo a la infancia. Full Stack Java (SENCE, 480 h). Socia fundadora, administradora y directora creativa de Studios Conari SpA (desde julio de 2026).",sty["body"]))
E.append(Spacer(1,4))
E+=bullets(["Cápsula educativa de lactancia para Chile Crece Contigo, Andacollo (2020): <link href='https://manecist.github.io/Matrona/capsula.html'><u>manecist.github.io/Matrona/capsula.html</u></link>.",
 "Ocho cápsulas educativas animadas en salud materno-infantil (2026), con guion, ilustración, animación, música y subtítulos.",
 "Diseño gráfico, ilustración y diagramación de material informativo."])
E.append(Spacer(1,10))
E.append(H("Respaldos de experiencia adjuntos"))
E.append(Paragraph("Se adjuntan a esta cotización los documentos que acreditan la experiencia del equipo (contrato o finiquito y certificado de cotizaciones previsionales de DailyFresh, 2022–2025).",sty["small"]))
E.append(Spacer(1,8)); E.append(FIRMA()); doc.build(E)
print(NETO,iva,total)
