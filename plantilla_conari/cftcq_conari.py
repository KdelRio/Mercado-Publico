import sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from conari_pdf import *
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle
OUT=sys.argv[1]; COD="1004823-120-COT26"
NETO=int(sys.argv[2]) if len(sys.argv)>2 else 716000
iva=round(NETO*0.19); total=NETO+iva
f=lambda v:"$"+f"{v:,}".replace(",",".")

def wire(w):
    """Esquema de la página principal (escritorio y móvil)."""
    H=9.2*cm; d=Drawing(w,H); dw=w*0.66; mx=dw+0.9*cm; mw=w-mx
    def box(x,y,bw,bh,txt,fill=CREAM,size=6.5,col=NAVY):
        d.add(Rect(x,y,bw,bh,fillColor=fill,strokeColor=LINEG,strokeWidth=0.8))
        if txt: d.add(String(x+bw/2,y+bh/2-2.5,txt,fontName="NS",fontSize=size,fillColor=col,textAnchor="middle"))
    # escritorio
    top=H-0.5*cm
    d.add(String(0,top+0.15*cm,"ESCRITORIO",fontName="NSB",fontSize=7,fillColor=GOLD))
    box(0,top-0.55*cm,dw,0.5*cm,"Encabezado y menú del sitio del CFT (se mantienen)",colors.white,6,GRAY)
    side=1.5*cm; cx=0; cw=dw-side-0.15*cm
    box(cw+0.15*cm,0.6*cm,side,top-1.25*cm,"",colors.white); d.add(String(cw+0.15*cm+side/2,top/2,"Accesos",fontName="NS",fontSize=6,fillColor=GRAY,textAnchor="middle")); d.add(String(cw+0.15*cm+side/2,top/2-8,"laterales",fontName="NS",fontSize=6,fillColor=GRAY,textAnchor="middle"))
    y=top-0.7*cm-1.9*cm; box(cx,y,cw,1.9*cm,"Carrusel: 1 Política · 2 Orientación y denuncia · 3 Actualidad",CREAM,7)
    for i in range(3): d.add(Circle(cw/2-8+i*8,y+0.2*cm,1.6,fillColor=GOLD if i==0 else LGRAY,strokeColor=None))
    y-=1.05*cm; bw=(cw-4*0.12*cm)/5
    for i,t in enumerate(["La Unidad","Política","Orientación","Ley 21.369","Documentos"]): box(cx+i*(bw+0.12*cm),y,bw,0.9*cm,t,colors.white,6.5)
    y-=1.45*cm; nw=(cw-2*0.12*cm)/3
    for i in range(3): box(cx+i*(nw+0.12*cm),y,nw,1.3*cm,"Noticia: foto, fecha, título",colors.white,6)
    y-=1.05*cm; box(cx,y,cw,0.9*cm,"Campañas de sensibilización (piezas, videos, YouTube)",colors.white,6.5)
    y-=0.75*cm; box(cx,y,cw,0.6*cm,"Banner permanente: Acceder al formulario de denuncia",NAVY,6.5,colors.white)
    box(0,0,dw,0.5*cm,"Pie de página del sitio del CFT (se mantiene)",colors.white,6,GRAY)
    # móvil
    d.add(String(mx,top+0.15*cm,"MÓVIL",fontName="NSB",fontSize=7,fillColor=GOLD))
    d.add(Rect(mx,0,mw,top,fillColor=colors.white,strokeColor=NAVY2,strokeWidth=1,rx=6,ry=6))
    y=top-0.35*cm; iw=mw-0.4*cm; ix=mx+0.2*cm
    for t,h,fl,c in [("Menú",0.4,colors.white,GRAY),("Carrusel",1.3,CREAM,NAVY),("La Unidad",0.42,colors.white,NAVY),("Política",0.42,colors.white,NAVY),
                     ("Orientación",0.42,colors.white,NAVY),("Ley · Documentos",0.42,colors.white,NAVY),("Noticias",0.9,colors.white,NAVY),
                     ("Campañas",0.6,colors.white,NAVY),("Denuncia",0.45,NAVY,colors.white)]:
        y-=h*cm; box(ix,y,iw,h*cm-0.08*cm,t,fl,6,c); y-=0.05*cm
    return d

doc=Doc(os.path.join(OUT,f"Cotizacion_Propuesta_{COD}_StudiosConari.pdf"),f"Cotización y propuesta · {COD}","Studios Conari · Cotización y propuesta")
w=doc.width; E=[]
E+=cover("Cotización y propuesta","SECCIÓN WEB<br/>INCLUSIÓN Y GÉNERO",
 f"Compra Ágil {COD} · CFT Estatal de la Región de Coquimbo · Proyecto CRC23101",
 [("Oferente","Studios Conari SpA<br/>RUT 78.465.252-1<br/>Empresa de menor tamaño · Sello Empresa Mujer"),
  ("Servicio","Diseño, desarrollo e implementación<br/>de la sección web, más cartilla<br/>y guía rápida diagramadas"),
  ("Oferta",f"{f(NETO)} neto<br/>{f(total)} IVA incluido<br/>Plazo: 30 días corridos")],
 ("Contacto del oferente","María Inés Cisterna Escobar, socia fundadora y administradora · postulaciones@studiosconari.cl · +56 9 8759 8952 · Colo Colo 379, oficina 706, Concepción, Región del Biobío."),
 "30 de octubre de 2026 · Validez de la oferta: 30 días corridos<br/><font color='#a8780f'>studiosconari.cl</font>",w)

E+=section("01","Oferta económica","Valor de la propuesta","Precio a suma alzada por el servicio completo: etapas I a IV de las especificaciones técnicas")
E.append(table([["Ítem","Cantidad","Valor neto"],
 ["Diseño, desarrollo e implementación de la sección web Inclusión y Género (etapas I, II y IV)","1",""],
 ["Diseño y diagramación editable de la cartilla de la Política Integral de Género y de la guía rápida de orientación y denuncia (etapa III)","incluido",""],
 ["Total neto","",f(NETO)],["IVA 19 %","",f(iva)],["Total con IVA","",f(total)]],[w-5.4*cm,2.2*cm,3.2*cm],bold_last=1,right_cols=(1,2)))
E.append(Spacer(1,6))
E+=section("02","Cumplimiento","Lo que pide el CFT","Cada punto de las especificaciones técnicas y cómo lo cumplimos")
E.append(table([["Especificación","Cómo lo cumplimos"],
 ["2. Dentro del sitio vigente","Trabajamos dentro de la estructura actual: se mantienen encabezado, menú, accesos laterales y pie de página."],
 ["3. Carrusel de 3 banners","Desplazamiento automático, flechas, indicadores de posición y diseño responsivo. Banners 1 y 2 con los textos indicados; banner 3 editable, con botón modificable."],
 ["4. Cinco accesos principales","Tarjetas: Conoce la Unidad, Política y Modelo de Gestión, Orientación y denuncias, Ley N.° 21.369 (enlace a la BCN) y Documentos útiles, con sus páginas interiores."],
 ["5. Noticias y actualidad","Tarjetas con foto, fecha, título, bajada y «Leer más», más acceso a «Ver todas las noticias»."],
 ["6. Campañas","Sección actualizable para banners, piezas gráficas, fotos, videos y enlaces a YouTube."],
 ["7. Banner de denuncia","Banner permanente con el botón «Acceder al formulario de denuncia», enlazado al formulario vigente."],
 ["8. Documentos digitales","Cartilla de la Política Integral de Género y guía rápida de orientación y denuncia, en PDF accesible y archivo editable."],
 ["9 y 10. Diseño y responsivo","Identidad gráfica del CFT, buen contraste y lectura, y adaptación a escritorio, notebook, tablet y celular."],
 ["13. Requerimientos técnicos","Compatible con la plataforma del sitio. Imágenes optimizadas. Sin plugins de pago ni dependencias del proveedor. Manual breve para actualizar contenidos."],
 ["15 y 16. Propiedad y garantía","Todo lo desarrollado queda del CFT. Corregimos sin costo los errores detectados en la recepción."]],[4.4*cm,w-4.4*cm]))
E.append(PageBreak())
E+=section("03","Propuesta","Estructura de la página","Esquema referencial de la página principal; el diseño final se valida en la maqueta (etapa I)")
E.append(wire(w))
E.append(Spacer(1,8))
E.append(cards([("Navegación simple","Una idea por bloque y desplazamiento vertical. Los contenidos de apoyo y denuncia siempre a un clic."),
 ("Accesible","Contraste adecuado, textos legibles, botones grandes en celular y textos alternativos en imágenes."),
 ("Fácil de actualizar","Banners, noticias, campañas y documentos se cambian desde el administrador del sitio, sin rediseñar.")],w))
E.append(Spacer(1,10))
E+=section("04","Plan de trabajo","Etapas y plazos","30 días corridos desde la aceptación de la orden de compra; trabajo remoto con reuniones por videollamada")
E.append(table([["Días","Etapa","Entregables"],
 ["1–3","Inicio","Reunión de inicio, acceso al sitio, revisión de la plataforma, recepción de contenidos, fotos y manual de marca."],
 ["4–10","I · Propuesta de interfaz","Maqueta de escritorio y móvil: banners, accesos, noticias, campañas y banner de denuncia. Revisión y aprobación."],
 ["11–22","II · Desarrollo","Implementación de la página principal, carrusel, páginas interiores, noticias, campañas, denuncia y carga inicial de contenidos."],
 ["11–22","III · Recursos digitales","Diagramación de la cartilla y de la guía rápida (en paralelo al desarrollo), con revisión de la contraparte."],
 ["23–30","IV · Entrega final","Ajustes, revisión de enlaces y dispositivos, archivos editables, código y manual de actualización."]],[1.6*cm,3.6*cm,w-5.2*cm]))
E.append(PageBreak())
E+=section("05","Equipo","Equipo de trabajo",None)
E.append(cards([("María Inés Cisterna","Socia fundadora y directora creativa. Diseño de interfaz, ilustración, iconografía y diagramación de la cartilla y la guía. Full Stack Java (SENCE, 480 h)."),
 ("Kevin del Río","Socio fundador y director técnico. Desarrollo e implementación web, responsivo, optimización y pruebas. Ingeniero en Informática (Duoc UC 2023)."),
 ("Trabajo conjunto","Revisión de accesibilidad, carga de contenidos y coordinación con la Unidad de Inclusión, Género y Convivencia.")],w))
E.append(Spacer(1,10))
E+=section("06","Experiencia","Trabajos publicados del equipo",None)
E.append(table([["Trabajo","Enlace"],
 ["Sitio web de Studios Conari","<link href='https://studiosconari.cl'><u>studiosconari.cl</u></link>"],
 ["Sitio de cápsulas educativas en salud (diseño, desarrollo y 9 cápsulas animadas)","<link href='https://manecist.github.io/Matrona/capsula.html'><u>manecist.github.io/Matrona/capsula.html</u></link>"]],[w-6.5*cm,6.5*cm]))
E.append(Spacer(1,4))
E.append(Paragraph("<b>Nota:</b> Studios Conari SpA se constituyó en julio de 2026; los trabajos listados son del equipo fundador.",sty["small"]))
E.append(Spacer(1,10))
E+=section("07","Condiciones","Condiciones de la oferta",None)
E+=bullets(["Factura afecta a IVA; pago contra recepción conforme. Sin costos posteriores: no incluye plugins ni licencias de pago, ni mantención obligatoria.",
 "Trabajo remoto. Para implementar, el CFT entrega un usuario de administración del sitio; al terminar se puede desactivar.",
 "Si el sitio requiere un plugin o herramienta externa, se informa antes y se usan solo opciones gratuitas y con licencia libre.",
 "Todo lo desarrollado (diseños, gráficas, documentos, editables y código) queda de propiedad del CFT."])
E.append(signature("María Inés Cisterna Escobar","Socia fundadora y administradora","Studios Conari SpA · RUT 78.465.252-1",img=os.path.join(A,"firma_maria.png")))
doc.build(E); print(NETO,iva,total)
