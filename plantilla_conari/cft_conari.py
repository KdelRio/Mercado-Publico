import sys, os
sys.path.insert(0,os.path.dirname(__file__))
from conari_pdf import *
OUT=sys.argv[1]
doc=Doc(OUT,"Cotización y propuesta · 1267913-13-COT26","Studios Conari · Cotización y propuesta creativa")
w=doc.width; E=[]
E+=cover("Cotización y propuesta creativa","CÁPSULAS AUDIOVISUALES<br/>VINCULACIÓN CON EL MEDIO Y ADMISIÓN",
 "Compra Ágil 1267913-13-COT26 · CFT Estatal de la Región de Antofagasta",
 [("Oferente","Studios Conari SpA<br/>RUT 78.465.252-1<br/>Empresa de menor tamaño · Sello Empresa Mujer"),
  ("Servicio","4 cápsulas animadas de hasta 3 minutos<br/>Full HD, música, locución y subtítulos"),
  ("Oferta","$420.000 neto<br/>$499.800 IVA incluido<br/>Entrega en 10 días")],
 ("Contacto del oferente","María Inés Cisterna Escobar, socia fundadora y administradora · postulaciones@studiosconari.cl · +56 9 8759 8952 · Colo Colo 379, oficina 706, Concepción, Región del Biobío."),
 "30 de octubre de 2026 · Validez de la oferta: 30 días corridos<br/><font color='#a8780f'>studiosconari.cl</font>",w)
E+=section("01","Oferta económica","Valor de la propuesta","Precio a suma alzada que incluye guion, animación, locución, música con licencia, subtítulos, correcciones y entregables")
E.append(table([["Ítem","Cantidad","Valor unitario neto","Total neto"],
 ["Cápsula audiovisual animada (hasta 3 min, Full HD 1080p)","4","$105.000","$420.000"],
 ["Total neto","","","$420.000"],["IVA 19 %","","","$79.800"],["Total con IVA","","","$499.800"]],
 [8.2*cm,2.2*cm,3.2*cm,w-13.6*cm],bold_last=1,right_cols=(1,2,3)))
E.append(Spacer(1,8))
E.append(callout("Condiciones de la oferta","Factura afecta a IVA. Pago contra recepción conforme, según las condiciones de la compra ágil. Validez de la oferta: 30 días corridos.",w))
E.append(Spacer(1,10))
E+=section("02","Cumplimiento","Estándar solicitado","Cómo cumplimos cada requisito de la compra")
E.append(table([["Requisito","Cómo lo cumplimos"],
 ["Duración máxima de 3 minutos","Cuatro cápsulas de 1:30 a 3:00 minutos, según la extensión del contenido que entregue el CFT."],
 ["Carácter informativo, socioeducativo y de sensibilización","Relato breve y cercano, con ejemplos del territorio y un llamado a la acción al cierre de cada cápsula."],
 ["Animación y recursos gráficos","Motion graphics 2D: ilustraciones propias, tipografía animada, iconografía, infografías animadas y transiciones."],
 ["Música","Música con licencia de uso comercial para difusión institucional (redes, sitio web y pantallas)."],
 ["Calidad de audio e imagen (mínimo Full HD 1080p)","MP4 H.264 de 1920×1080 a 25 fps; locución en off grabada y masterizada, con voz clara y sin ruido."],
 ["Subtítulos","Subtítulos incrustados en cada video y archivo .SRT por cápsula, para accesibilidad."],
 ["Contenidos aportados por el CFT","Adaptamos los contenidos a guion audiovisual; el CFT valida cada guion antes de animar."]],[5.6*cm,w-5.6*cm]))
E.append(PageBreak())
E+=section("03","Propuesta creativa","Tu camino en el CFT empieza aquí","Concepto, línea gráfica y estructura de las cuatro cápsulas")
E.append(callout("Concepto","Un hilo visual común —una ruta que recorre el paisaje de la Región de Antofagasta: desierto, ciudad, puerto y cielo nocturno— une las cuatro cápsulas. Cada cápsula es una estación de esa ruta. La línea gráfica usará los colores y la tipografía institucional del CFT; el paisaje regional aporta identidad local.",w))
E.append(Spacer(1,6))
E.append(cards([("Estilo visual","Ilustración plana con texturas suaves y ritmo dinámico de 3 a 5 segundos por plano."),
 ("Diversidad","Personajes diversos en edad, género, origen y discapacidad, sin estereotipos."),
 ("Accesibilidad","Textos breves en pantalla, subtítulos y voz en off cercana y clara.")],w))
E.append(Spacer(1,8))
E.append(Paragraph("ESTRUCTURA PROPUESTA (REFERENCIAL; SE AJUSTA A LOS CONTENIDOS DEL CFT)",sty["h"]))
E.append(table([["N°","Cápsula","Enfoque"],
 ["1","¿Qué es la Vinculación con el Medio en el CFT?","Qué significa, para qué sirve y cómo el CFT trabaja con comunidades, empresas e instituciones del territorio."],
 ["2","El CFT en el territorio","Proyectos, convenios y acciones con la comunidad, con los datos y testimonios que entregue el CFT."],
 ["3","Admisión: ¿cómo postulo?","Carreras, requisitos, pasos de postulación y fechas clave, de forma simple y visual."],
 ["4","Estudiar en un CFT estatal","Gratuidad, beneficios, apoyos al estudiante y cómo resolver dudas: llamado a postular."]],[1*cm,5.4*cm,w-6.4*cm]))
E.append(Spacer(1,8))
E.append(Paragraph("GUION Y STORYBOARD DE MUESTRA · CÁPSULA 3 «ADMISIÓN: ¿CÓMO POSTULO?» (APROX. 2:30)",sty["h"]))
E.append(table([["Tiempo","Imagen (animación)","Voz en off"],
 ["0:00–0:12","La ruta del desierto se ilumina; aparece una estudiante mirando el horizonte. Logo del CFT.","«¿Quieres estudiar una carrera técnica cerca de tu casa? Te contamos cómo postular.»"],
 ["0:12–0:40","La ruta se convierte en un mapa con íconos de cada área de carreras, que se encienden uno a uno.","«El CFT ofrece carreras técnicas pensadas para el trabajo en nuestra región.»"],
 ["0:40–1:20","Lista animada: requisitos, documentos y postulación en línea; cada paso se marca al completarse.","«Postular es simple: revisa los requisitos, ten tus documentos listos y completa tu postulación.»"],
 ["1:20–1:50","Calendario animado con las fechas clave; un reloj avanza.","«Anota las fechas: inicio de postulación, matrícula e inicio de clases.»"],
 ["1:50–2:15","La estudiante llega a la sede; aparecen íconos de gratuidad y beneficios.","«Al ser un CFT estatal, puedes acceder a gratuidad y otros beneficios.»"],
 ["2:15–2:30","Cierre: la ruta forma la palabra «Postula»; sitio web y redes del CFT.","«Tu camino empieza aquí. Postula en el sitio web del CFT.»"]],[2*cm,(w-2*cm)*0.5,(w-2*cm)*0.5]))
E.append(PageBreak())
E+=section("04","Plan de trabajo","Plazo y entregables","Diez días corridos desde la aceptación de la orden de compra, sujeto a recibir los contenidos del CFT en la reunión de inicio")
E.append(table([["Día","Hito"],["1","Reunión de inicio por videollamada; recepción de contenidos, logos y manual de marca del CFT."],
 ["3","Entrega de los cuatro guiones y storyboards para validación del CFT."],["6","Entrega de las primeras versiones animadas de las cuatro cápsulas."],
 ["8","Ronda de corrección (incluye dos instancias de corrección por cápsula)."],["10","Entrega final: 4 videos MP4 Full HD, 4 archivos .SRT y gráficas en PNG y SVG."]],[1.6*cm,w-1.6*cm]))
E.append(Spacer(1,10))
E+=section("05","Equipo","Equipo y capacidades",None)
E.append(cards([("María Inés Cisterna","Socia fundadora y directora creativa. Dirección, guion, ilustración y animación 2D. Matrona (USS 2018), Full Stack Java (SENCE, 480 h)."),
 ("Kevin del Río","Socio fundador y director técnico. Edición, postproducción, subtítulos y control de calidad. Ingeniero en Informática (Duoc UC 2023)."),
 ("María José Cañas","Equipo de apoyo. Locución en off.")],w))
E.append(Spacer(1,10))
E+=section("06","Antecedentes","Muestra de capacidad y condiciones",None)
E.append(callout("Muestra de capacidad del equipo","Studios Conari SpA es una empresa constituida en julio de 2026. Las siguientes piezas son muestras de capacidad del equipo, no trabajos realizados para clientes: cápsula educativa animada (manecist.github.io/Matrona/capsula.html) y portafolio del equipo (studiosconari.github.io).",w))
E.append(Spacer(1,6))
E+=bullets(["Trabajo 100 % remoto; coordinación por correo y videollamada con la Unidad de Vinculación con el Medio.",
 "Los derechos de uso de las cuatro cápsulas quedan para el CFT para difusión institucional sin límite de plazo; la música se entrega con licencia para ese uso.",
 "Iniciativa sustentable: trabajo digital y remoto, sin traslados ni material impreso."])
E.append(signature("María Inés Cisterna Escobar","Socia fundadora y administradora","Studios Conari SpA · RUT 78.465.252-1"))
doc.build(E); print("ok")
