import sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from conari_pdf import *
OUT=sys.argv[1]; COD="1259202-15-COT26"
NETO_VIDEO=334000; N=3
neto=NETO_VIDEO*N; iva=round(neto*0.19); total=neto+iva; video_iva=round(NETO_VIDEO*1.19)
f=lambda v:"$"+f"{v:,}".replace(",",".")
FIRMA=lambda: signature("María Inés Cisterna Escobar","Socia fundadora y administradora","Studios Conari SpA · RUT 78.465.252-1",img=os.path.join(A,"firma_maria.png"))
LUGAR="Concepción, 30 de octubre de 2026"
VID="https://manecist.github.io/Matrona/capsula/videos/"
EXP=[("Cápsula educativa de lactancia para Chile Crece Contigo (Andacollo)","2020","https://manecist.github.io/Matrona/capsula.html"),
 ("¿Cómo guardo mi leche? (cápsula animada)","2026",VID+"Capsula_01_como_guardo_mi_leche.mp4"),
 ("Masaje Shantala paso a paso (cápsula animada)","2026",VID+"Capsula_02_masaje_shantala.mp4"),
 ("Sacar los chanchitos y aliviar gases (cápsula animada)","2026",VID+"Capsula_03_sacar_chanchitos.mp4"),
 ("Sueño seguro (cápsula animada)","2026",VID+"Capsula_04_sueno_seguro.mp4"),
 ("¿Ya es hora de ir a la maternidad? (cápsula animada)","2026",VID+"Capsula_05_hora_de_ir_a_la_maternidad.mp4"),
 ("¿Qué es el PAP? (cápsula animada)","2026",VID+"Capsula_06_que_es_el_pap.mp4"),
 ("Píldora del día después (cápsula animada)","2026",VID+"Capsula_07_pildora_del_dia_despues.mp4"),
 ("Mitos de la lactancia (cápsula animada)","2026",VID+"Capsula_08_mitos_de_la_lactancia.mp4")]
lnk=lambda u:f'<link href="{u}"><u>Ver pieza</u></link>'

def propuesta(path):
    doc=Doc(path,f"Cotización y propuesta · {COD}","Studios Conari · Cotización y propuesta"); w=doc.width; E=[]
    E+=cover("Cotización y propuesta","PRODUCCIÓN AUDIOVISUAL Y GRÁFICA<br/>TRES VIDEOS INSTITUCIONALES",
     f"Compra Ágil {COD} · Subsecretaría de Educación · Dirección de Comunicaciones",
     [("Oferente","Studios Conari SpA<br/>RUT 78.465.252-1<br/>Empresa de menor tamaño · Sello Empresa Mujer"),
      ("Servicio","3 videos horizontales de hasta 1:30<br/>Guion, edición, animación, música<br/>y piezas para redes"),
      ("Oferta",f"{f(neto)} neto<br/>{f(total)} IVA incluido<br/>Entrega hasta el 06-12-2026")],
     ("Contacto del oferente","María Inés Cisterna Escobar, socia fundadora y administradora · postulaciones@studiosconari.cl · +56 9 8759 8952 · Colo Colo 379, oficina 706, Concepción, Región del Biobío."),
     "30 de octubre de 2026 · Validez de la oferta: 30 días corridos<br/><font color='#a8780f'>studiosconari.cl</font>",w)
    E+=section("01","Oferta económica","Valor de la propuesta","Precio a suma alzada por video: guion, edición, montaje, postproducción de sonido y color, música con licencia, animación, piezas para redes, archivos fuente e informe final")
    E.append(table([["Ítem","Valor neto","IVA 19 %","Valor IVA incluido"]]+
     [[f"Video {i}",f(NETO_VIDEO),f(video_iva-NETO_VIDEO),f(video_iva)] for i in (1,2,3)]+
     [["Total",f(neto),f(iva),f(total)]],[w-10.2*cm,3.2*cm,3*cm,4*cm],bold_last=1,right_cols=(1,2,3)))
    E.append(Spacer(1,8))
    E.append(callout("Condiciones de la oferta",f"Factura afecta a IVA. El total ofertado en la plataforma es {f(total)} IVA incluido, igual al Anexo N°1. Pago a 30 días desde la factura, con recepción conforme. Validez: 30 días corridos.",w))
    E.append(Spacer(1,10))
    E+=section("02","Cumplimiento","Lo que pide el Ministerio","Cómo cumplimos cada punto de los términos de referencia")
    E.append(table([["Requisito","Cómo lo cumplimos"],
     ["Guion en co-creación con la contraparte técnica","Propuesta de guion por video después de la reunión de inicio; lo ajustamos con la contraparte hasta su aprobación. La edición parte con el guion aprobado."],
     ["Edición, montaje, postproducción de sonido y color","Montaje con el material que aporte el Ministerio (imágenes, logos, registros previos) y gráfica propia; corrección de color y mezcla de audio."],
     ["Musicalización","Música con licencia de uso comercial para difusión institucional en redes, web y plataformas."],
     ["Animación de piezas gráficas","Motion graphics 2D: tipografía animada, íconos, datos e ilustraciones con la línea gráfica del Ministerio."],
     ["3 videos horizontales de hasta 1:30","MP4 H.264 Full HD 1920×1080, aptos para YouTube, LinkedIn y sitio web. Subtítulos incrustados y archivo .SRT."],
     ["Archivos fuente/editables","Proyectos de edición y animación, gráficas en SVG/PNG y tipografías o recursos usados."],
     ["Piezas gráficas complementarias","Por cada video: versión cuadrada 1:1 y vertical 9:16 (recorte o adaptación), más una portada o gráfica fija."],
     ["Instancias de revisión","Dos rondas de ajustes por video antes de la entrega final. Correcciones de garantía en 3 días hábiles."],
     ["Informe final","Informe con el detalle de los entregables y la evaluación del servicio, al entregar el tercer video."],
     ["Confidencialidad","La información del Ministerio se usa solo para este servicio y no se publica sin su autorización."]],[5.6*cm,w-5.6*cm]))
    E.append(PageBreak())
    E+=section("03","Propuesta creativa","Claro, cercano e inspirador","Cómo abordamos los tres videos")
    E.append(callout("Enfoque","Cada video cuenta una sola idea en menos de 90 segundos: qué es, a quién sirve y qué hacer. Usamos un lenguaje simple, pensado para familias, estudiantes, docentes y comunidad educativa, y cerramos con un llamado a la acción claro. Los tres videos comparten una misma línea gráfica, basada en la identidad del Ministerio, para que se reconozcan como una serie.",w))
    E.append(Spacer(1,6))
    E.append(cards([("Ritmo","Planos de 3 a 5 segundos, textos breves en pantalla y una idea por escena: pensado para redes."),
     ("Accesibilidad","Subtítulos en todos los videos, buen contraste y tipografía legible. Si el Ministerio lo pide, dejamos espacio para intérprete de LSCh."),
     ("Diversidad","Personas y familias diversas en edad, género, origen y territorio, sin estereotipos.")],w))
    E.append(Spacer(1,8))
    E.append(Paragraph("ESTRUCTURA BASE DE CADA VIDEO (SE AJUSTA AL TEMA QUE DEFINA EL MINISTERIO)",sty["h"]))
    E.append(table([["Tiempo","Bloque","Contenido"],
     ["0:00–0:08","Gancho","Una pregunta o situación cotidiana que conecta con quien mira."],
     ["0:08–0:35","Qué es","El programa o proceso explicado en una frase, con imagen y texto animado."],
     ["0:35–1:05","Cómo funciona","Pasos, fechas o beneficios clave, con íconos y datos animados."],
     ["1:05–1:20","Por qué importa","Un testimonio, una cifra o una imagen del material del Ministerio."],
     ["1:20–1:30","Cierre","Llamado a la acción, sitio web y logo del Ministerio."]],[2.2*cm,3.2*cm,w-5.4*cm]))
    E.append(Spacer(1,10))
    E+=section("04","Plan de trabajo","Plazo y entregables","Desde la aceptación de la orden de compra hasta el 06 de diciembre de 2026 inclusive. Las fechas de cada video se ajustan a lo que informe el Ministerio")
    E.append(table([["Etapa","Hito"],
     ["Semana 1","Reunión de inicio (online o presencial). Recepción de información, imágenes, logos y manual de marca."],
     ["Semana 1–2","Propuesta de guion de los 3 videos y validación con la contraparte técnica."],
     ["Semana 2–3","Edición y animación con guion aprobado. Primera versión de cada video."],
     ["Semana 3–4","Rondas de ajustes. Piezas cuadradas y verticales derivadas de cada video."],
     ["Hasta 06-12","Entrega final: 3 videos, archivos fuente, piezas gráficas e informe final."]],[2.6*cm,w-2.6*cm]))
    E.append(PageBreak())
    E+=section("05","Equipo","Equipo de producción",None)
    E.append(cards([("María Inés Cisterna","Socia fundadora y directora creativa. Guion, dirección de arte, ilustración y animación 2D."),
     ("Kevin del Río","Socio fundador y director técnico. Edición, montaje, color, sonido, subtítulos y control de calidad. Ingeniero en Informática (Duoc UC 2023)."),
     ("María José Cañas","Equipo de apoyo. Locución en off, cuando el video la requiera.")],w))
    E.append(Spacer(1,4))
    E+=section("06","Experiencia","Trabajos audiovisuales publicados","Piezas animadas de autoría de María Inés Cisterna, directora creativa del equipo")
    E.append(table([["N°","Pieza","Año","Enlace"]]+[[str(i),p,a,lnk(u)] for i,(p,a,u) in enumerate(EXP,1)],[0.9*cm,w-5.2*cm,1.3*cm,3*cm]))
    E.append(Spacer(1,4))
    E.append(Paragraph("<b>Nota:</b> Studios Conari SpA se constituyó en julio de 2026. Las piezas son trabajos publicados del equipo: la cápsula 2020 fue realizada para Chile Crece Contigo y las ocho de 2026 son de producción propia. Todas en manecist.github.io/Matrona/capsula.html.",sty["small"]))
    E.append(Spacer(1,8))
    E+=section("07","Condiciones","Condiciones de la oferta",None)
    E+=bullets(["No incluye rodaje ni traslados: los videos se construyen con el material que aporte el Ministerio y con gráfica y animación propias.",
     "Los derechos de uso de los videos y piezas quedan para el Ministerio para difusión institucional sin límite de plazo; la música se entrega con licencia para ese uso.",
     "Coordinación por correo y videollamada. Garantía técnica de 30 días desde la entrega."])
    E.append(FIRMA()); doc.build(E)

def anexo(path,num,titulo,body):
    doc=Doc(path,f"Anexo N°{num} · {COD}",f"Studios Conari · Anexo N°{num}",footer_right="Anexo"); w=doc.width
    doc.build([Spacer(1,4),*section(f"Anexo N°{num}",f"Compra Ágil {COD}",titulo,"Subsecretaría de Educación · Servicio de producción audiovisual y gráfica"),*body(w),
     Spacer(1,14),Paragraph(LUGAR,sty["body"]),FIRMA()])

def a1(w): return [table([["Ítem","Valor impuesto incluido"]]+[[f"Video {i}",f(video_iva)] for i in (1,2,3)]+[["Total",f(total)]],[w-6*cm,6*cm],bold_last=1,right_cols=(1,)),
    Spacer(1,8),callout("Detalle",f"Valor neto por video {f(NETO_VIDEO)} + IVA 19 %. Total neto {f(neto)}, IVA {f(iva)}, total {f(total)}. Factura afecta a IVA.",w)]
def a2(w): return [table([["Oferente cuenta con programas de integridad y ética empresarial (compliance) conocido por su personal","Marcar con X"],["Sí","X"],["No",""]],[w-4*cm,4*cm]),
    Spacer(1,8),table([["N°","Vía por la cual se dio a conocer el programa","Medio de verificación"],
     ["1","Correo electrónico enviado el 07-10-2026 a todo el personal (socios administradores), con el programa adjunto y solicitud de confirmación de lectura.","Impresión del correo con las respuestas «Recibido y leído» de cada persona (archivo Correo_difusion_Programa_Integridad.pdf)."],
     ["2","Entrega del programa y firma del Acta de recepción y conocimiento (Anexo A del programa), 07-10-2026.","Acta firmada por cada persona, incluida en el programa (archivo Programa_Integridad_Studios_Conari.pdf, página 4)."],
     ["3","Inducción a quienes se incorporen y sesión anual de capacitación, según el punto 4 del programa.","Registro de asistencia (se genera en cada sesión)."]],[1*cm,(w-1*cm)/2,(w-1*cm)/2]),
    Spacer(1,8),callout("Documentos adjuntos","Programa de Integridad y Ética Empresarial de Studios Conari SpA, versión 1.0, aprobado el 07-10-2026 (incluye Código de Ética y Conducta, modelo de prevención de delitos según Leyes N° 20.393 y N° 21.595, canal de denuncias y Acta de recepción firmada), y correo de difusión con confirmaciones de lectura.",w)]
def a3(w): return [table([["Campo","Dato"],["Nombre de la empresa o contratista","Studios Conari SpA"],["RUT de la empresa","78.465.252-1"],
    ["Nombre contacto","María Inés Cisterna Escobar"],["Dirección comercial","Colo Colo 379, oficina 706, Concepción, Región del Biobío"],
    ["Correo electrónico","postulaciones@studiosconari.cl"],["Teléfonos móviles","+56 9 8759 8952"]],[6.5*cm,w-6.5*cm])]

propuesta(os.path.join(OUT,f"Cotizacion_Propuesta_{COD}_StudiosConari.pdf"))
anexo(os.path.join(OUT,f"Anexo1_Oferta_economica_{COD}.pdf"),1,"Oferta económica",a1)
anexo(os.path.join(OUT,f"Anexo2_Integridad_{COD}.pdf"),2,"Programa de integridad y ética empresarial",a2)
anexo(os.path.join(OUT,f"Anexo3_Datos_proveedor_{COD}.pdf"),3,"Datos del proveedor",a3)
print(neto,iva,total,video_iva)
