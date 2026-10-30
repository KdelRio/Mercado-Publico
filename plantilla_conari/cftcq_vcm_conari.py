import sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from conari_pdf import *
from reportlab.graphics.shapes import Drawing, Rect, String
OUT=sys.argv[1]; COD="1004823-122-COT26"
NETO=int(sys.argv[2]) if len(sys.argv)>2 else 420000
iva=round(NETO*0.19); total=NETO+iva
f=lambda v:"$"+f"{v:,}".replace(",",".")

def wire(w):
    """Esquema de la página principal de VcM y de una página interior por año."""
    H=8.6*cm; d=Drawing(w,H); dw=w*0.6; mx=dw+0.8*cm; mw=w-mx
    def box(x,y,bw,bh,txt,fill=CREAM,size=6.5,col=NAVY):
        d.add(Rect(x,y,bw,bh,fillColor=fill,strokeColor=LINEG,strokeWidth=0.8))
        if txt: d.add(String(x+bw/2,y+bh/2-2.5,txt,fontName="NS",fontSize=size,fillColor=col,textAnchor="middle"))
    top=H-0.5*cm
    d.add(String(0,top+0.15*cm,"PÁGINA PRINCIPAL VcM",fontName="NSB",fontSize=7,fillColor=GOLD))
    box(0,top-0.55*cm,dw,0.5*cm,"Encabezado y menú del sitio del CFT (se mantienen)",colors.white,6,GRAY)
    y=top-0.7*cm-1.5*cm; box(0,y,dw,1.5*cm,"Banner y presentación breve de Vinculación con el Medio",CREAM,7)
    tw=(dw-2*0.12*cm)/3
    for r,row in enumerate([["Política y documentos","Convenios","Programas"],["Innovación","Red de Titulados","Material audiovisual"]]):
        y-=1.15*cm
        for i,t in enumerate(row): box(i*(tw+0.12*cm),y,tw,1.0*cm,t,colors.white,6.5)
    y-=1.15*cm; box(0,y,dw,1.0*cm,"Programas destacados: Fondo Concursable · Mentorías · CFT 360°",colors.white,6.5)
    box(0,0,dw,0.5*cm,"Pie de página del sitio del CFT (se mantiene)",colors.white,6,GRAY)
    d.add(String(mx,top+0.15*cm,"PÁGINA INTERIOR (EJ. FONDO CONCURSABLE)",fontName="NSB",fontSize=7,fillColor=GOLD))
    d.add(Rect(mx,0,mw,top,fillColor=colors.white,strokeColor=NAVY2,strokeWidth=1,rx=4,ry=4))
    y=top-0.3*cm; iw=mw-0.4*cm; ix=mx+0.2*cm
    box(ix,y-0.9*cm,iw,0.85*cm,"Descripción del programa",CREAM,6.5); y-=1.05*cm
    yw=(iw-3*0.1*cm)/4
    for i,a in enumerate(["2024","2025","2026","2027"]): box(ix+i*(yw+0.1*cm),y-0.55*cm,yw,0.5*cm,a,NAVY if i==2 else colors.white,6.5,colors.white if i==2 else NAVY)
    y-=0.7*cm
    for t,h in [("Bases (descarga)",0.5),("Adjudicaciones (descarga)",0.5),("Galería de fotos y gráficas",1.3),("Registro de actividades y cierre",0.8)]:
        box(ix,y-h*cm,iw,h*cm-0.08*cm,t,colors.white,6.3); y-=h*cm+0.04*cm
    d.add(String(ix,0.25*cm,"Se agrega un año nuevo sin rediseñar.",fontName="NS",fontSize=6,fillColor=GRAY))
    return d

doc=Doc(os.path.join(OUT,f"Cotizacion_Propuesta_{COD}_StudiosConari.pdf"),f"Cotización y propuesta · {COD}","Studios Conari · Cotización y propuesta")
w=doc.width; E=[]
E+=cover("Cotización y propuesta técnica","SECCIÓN WEB<br/>VINCULACIÓN CON EL MEDIO",
 f"Compra Ágil {COD} · CFT Estatal de la Región de Coquimbo · Proyecto CRC 2495",
 [("Oferente","Studios Conari SpA<br/>RUT 78.465.252-1<br/>Empresa de menor tamaño · Sello Empresa Mujer · emite factura"),
  ("Servicio","Diseño, desarrollo e implementación<br/>de la sección VcM dentro del<br/>sitio institucional vigente"),
  ("Oferta",f"{f(NETO)} neto<br/>{f(total)} IVA incluido<br/>Plazo: 30 días corridos")],
 ("Contacto del oferente","María Inés Cisterna Escobar, socia fundadora y administradora · postulaciones@studiosconari.cl · +56 9 8759 8952 · Colo Colo 379, oficina 706, Concepción, Región del Biobío."),
 "30 de octubre de 2026 · Validez de la oferta: 30 días corridos<br/><font color='#a8780f'>studiosconari.cl</font>",w)

E+=section("01","Cotización","Valor total del servicio","Precio a suma alzada por el servicio completo: etapas I, II y III de las especificaciones técnicas")
E.append(table([["Ítem","Cantidad","Valor neto"],
 ["Servicio de diseño, desarrollo y actualización de interfaz web para Vinculación con el Medio (propuesta de interfaz, implementación, carga inicial de contenidos, ajustes, archivos fuente y guía de actualización)","1",f(NETO)],
 ["Total neto","",f(NETO)],["IVA 19 %","",f(iva)],["Total con IVA","",f(total)]],[w-5.4*cm,2.2*cm,3.2*cm],bold_last=1,right_cols=(1,2)))
E.append(Spacer(1,6))
E+=section("02","Propuesta técnica","Lo que pide el CFT","Cada punto de las especificaciones técnicas y cómo lo cumplimos")
E.append(table([["Especificación","Cómo lo cumplimos"],
 ["2. Dentro del sitio vigente","Trabajamos en el gestor de contenidos actual, coordinados con quien administra el sitio. Se mantienen encabezado, menú y pie de página."],
 ["3.1 Política y documentos","Presentación, Política y Modelo de Gestión descargables, espacio para otros documentos y reportería por año (2025 y 2026, ampliable)."],
 ["3.2 Convenios","Presentación, tipos de convenios, socios comunitarios y muro de logos; se agregan nuevos convenios sin rediseñar."],
 ["3.3 Programas","Tarjetas con foto para Fondo Concursable (2024–2027), Mentorías (2025–2026) y CFT 360°, con páginas por año: bases, adjudicaciones, fotos y cierres."],
 ["3.4 a 3.6","Innovación (texto, gráficas, descargas y espacio para proyectos), acceso a Red de Titulados y sección de videos y cápsulas."],
 ["5. Diseño y usabilidad","Identidad del CFT, carácter estatal y territorial, navegación de dos niveles, buena jerarquía, accesible y responsivo."],
 ["6. Requerimientos técnicos","Sin licencias ni plugins de pago no informados. Imágenes optimizadas. Sin dependencias del proveedor: el CFT actualiza solo."],
 ["9 y 10. Propiedad y garantía","Todo lo desarrollado queda del CFT. Corregimos sin costo los errores detectados en la recepción."]],[4.4*cm,w-4.4*cm]))
E.append(PageBreak())
E+=section("03","Propuesta","Arquitectura de la sección","Esquema referencial; la arquitectura y el diseño final se aprueban en la reunión de revisión (etapa I)")
E.append(wire(w))
E.append(Spacer(1,8))
E.append(cards([("Simple","Solo dos niveles: página principal y páginas de cada tema. Todo documento a un máximo de dos clics."),
 ("Por años","Fondo Concursable, Mentorías y reportería se ordenan por año; sumar un año es duplicar un bloque."),
 ("Territorial","Fotografías reales de actividades, socios y titulados del CFT en la Región de Coquimbo.")],w))
E.append(Spacer(1,10))
E+=section("04","Plazo de ejecución","Etapas y plazos","30 días corridos desde la aceptación de la orden de compra y la entrega de los antecedentes; trabajo remoto con reuniones por videollamada")
E.append(table([["Días","Etapa","Entregables"],
 ["1–3","Inicio","Reunión de inicio, acceso al gestor del sitio, recepción de textos, fotos, logos y documentos."],
 ["4–10","I · Propuesta de interfaz","Arquitectura y navegación, diseño de la página principal y de programas, escritorio y móvil. Reunión de revisión y aprobación."],
 ["11–24","II · Desarrollo","Implementación de las seis secciones, programas por año, documentos, enlaces, videos y adaptación responsiva."],
 ["25–30","III · Ajustes y entrega","Observaciones, revisión de enlaces y dispositivos, archivos fuente y guía breve de actualización."]],[1.6*cm,3.6*cm,w-5.2*cm]))
E.append(PageBreak())
E+=section("05","Equipo","Experiencia en diseño y desarrollo web",None)
E.append(cards([("María Inés Cisterna","Socia fundadora y directora creativa. Diseño de interfaz, gráfica, iconografía e ilustración. Full Stack Java (SENCE, 480 h)."),
 ("Kevin del Río","Socio fundador y director técnico. Desarrollo e implementación web, responsivo, optimización y pruebas. Ingeniero en Informática (Duoc UC 2023)."),
 ("Trabajo conjunto","Carga de contenidos, revisión de accesibilidad y coordinación con el Departamento de Vinculación con el Medio.")],w))
E.append(Spacer(1,10))
E+=section("06","Portafolio","Trabajos publicados del equipo",None)
E.append(table([["Trabajo","Enlace"],
 ["Sitio web de Studios Conari","<link href='https://studiosconari.cl'><u>studiosconari.cl</u></link>"],
 ["Sitio de cápsulas educativas en salud (diseño, desarrollo y 9 cápsulas animadas)","<link href='https://manecist.github.io/Matrona/capsula.html'><u>manecist.github.io/Matrona/capsula.html</u></link>"]],[w-6.5*cm,6.5*cm]))
E.append(Spacer(1,4))
E.append(Paragraph("<b>Nota:</b> Studios Conari SpA se constituyó en julio de 2026; los trabajos listados son del equipo fundador.",sty["small"]))
E.append(Spacer(1,10))
E+=section("07","Condiciones","Condiciones de la oferta",None)
E+=bullets(["Factura afecta a IVA; pago contra recepción conforme. Sin costos posteriores: no incluye plugins ni licencias de pago, ni mantención obligatoria.",
 "Trabajo remoto. Para implementar, el CFT entrega un usuario del gestor de contenidos; al terminar se puede desactivar.",
 "Incorporamos los ajustes de la contraparte hasta la aprobación final, dentro del alcance de las especificaciones técnicas.",
 "Todo lo desarrollado (diseños, gráficas, plantillas, editables y código) queda de propiedad del CFT."])
E.append(signature("María Inés Cisterna Escobar","Socia fundadora y administradora","Studios Conari SpA · RUT 78.465.252-1",img=os.path.join(A,"firma_maria.png")))
doc.build(E); print(NETO,iva,total)
