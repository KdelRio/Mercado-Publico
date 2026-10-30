import sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from conari_pdf import *
OUT=sys.argv[1]; COD="1214103-276-COT26"
COMP=[("a","Mantención operativa y modificaciones básicas del sitio web actual","Durante la transición, hasta la puesta en funcionamiento del nuevo sitio",150000),
      ("b","Creación del nuevo sitio en WordPress, plantilla premium y capacitación","Un servicio",300000),
      ("c","Hosting","Doce meses",50000),
      ("d","Mantenciones de la nueva plataforma","Tres mantenciones (meses 2, 4 y 6)",220000)]
NETO=sum(c[3] for c in COMP); iva=round(NETO*0.19); total=NETO+iva
f=lambda v:"$"+f"{v:,}".replace(",",".")
FIRMA=lambda: signature("María Inés Cisterna Escobar","Socia fundadora y administradora","Studios Conari SpA · RUT 78.465.252-1",img=os.path.join(A,"firma_maria.png"))
H=lambda t:Paragraph(t.upper(),sty["h"])

doc=Doc(os.path.join(OUT,f"Cotizacion_Propuesta_{COD}_StudiosConari.pdf"),f"Cotización y propuesta · {COD}","Studios Conari · Cotización y propuesta")
w=doc.width; E=[]
E+=cover("Cotización formal y propuesta","SITIO WEB INSTITUCIONAL<br/>MANTENCIÓN Y NUEVA PLATAFORMA WORDPRESS",
 f"Compra Ágil {COD} · Corporación Cultural Municipal de Puente Alto · Dirección de Comunicaciones",
 [("Oferente","Studios Conari SpA<br/>RUT 78.465.252-1<br/>Empresa de menor tamaño · Sello Empresa Mujer"),
  ("Servicio","Mantención del sitio actual, nuevo<br/>sitio WordPress, plantilla premium,<br/>capacitación, hosting y 3 mantenciones"),
  ("Oferta",f"{f(NETO)} neto<br/>{f(total)} IVA incluido<br/>Sitio nuevo: 30 días hábiles")],
 ("Contacto y responsable de coordinación","María Inés Cisterna Escobar, socia fundadora y administradora · postulaciones@studiosconari.cl · +56 9 8759 8952 · Colo Colo 379, oficina 706, Concepción, Región del Biobío."),
 "30 de octubre de 2026 · Validez de la oferta: 30 días corridos<br/><font color='#a8780f'>studiosconari.cl</font>",w)

E+=section("01","Oferta económica","Valor por componente","Valores netos, IVA y total a pagar; incluyen todos los costos para ejecutar lo comprometido (plantilla, licencia y hosting incluidos)")
rows=[["","Servicio","Cantidad o período","Valor neto","IVA 19 %","Total"]]
for k,s,p,v in COMP: rows.append([k,s,p,f(v),f(round(v*0.19)),f(v+round(v*0.19))])
rows.append(["","Total","",f(NETO),f(iva),f(total)])
E.append(table(rows,[0.6*cm,w-11.4*cm,3.6*cm,2.4*cm,2.2*cm,2.6*cm],bold_last=1,right_cols=(3,4,5)))
E.append(Spacer(1,6))
E.append(callout("Facturación y pago","Factura afecta a IVA por componente, después de su recepción conforme, según el numeral 10 de los términos de referencia. Las mantenciones se facturan una vez ejecutadas, sin anticipos. Validez de la oferta: 30 días corridos.",w))
E.append(Spacer(1,10))
E+=section("02","Aceptación","Aceptación de los términos de referencia",None)
E.append(Paragraph("Studios Conari SpA <b>acepta expresamente</b> los alcances, entregables, plazos y condiciones económicas establecidos en los Términos de Referencia de esta compra, sin observaciones ni exclusiones. Cualquier prestación adicional se ejecutará solo con autorización previa y escrita de la Corporación.",sty["body"]))
E.append(PageBreak())
E+=section("03","Propuesta","Cómo lo haremos","Según los numerales 3.1 a 3.6 de los términos de referencia")
E.append(table([["Componente","Cómo lo cumplimos"],
 ["3.1 Sitio actual","Revisión inicial y respaldo de archivos y base de datos antes de intervenir. Modificaciones básicas de textos, imágenes, enlaces, menús y páginas a solicitud de Comunicaciones, con registro escrito de cada solicitud, su evaluación técnica y su fecha. Si algo no es viable en la plataforma vigente, lo informamos por escrito con una alternativa."],
 ["3.2 Sitio nuevo","Inventario del sitio actual y propuesta de mapa en los primeros 5 días hábiles. Desarrollo en un entorno de pruebas, sin tocar el sitio vigente. Estructura, menús, identidad institucional, páginas y publicaciones, migración del inventario aprobado y diseño responsivo. Actualización final de contenidos y respaldo previo antes de publicar, con autorización escrita."],
 ["3.3 Plantilla premium","<b>GeneratePress Premium</b> (desarrollador: GeneratePress / Tom Usborne), con GenerateBlocks. Licencia anual legítima con actualizaciones y soporte por 12 meses, registrada con correo institucional. Al vencer, el sitio sigue funcionando con la versión instalada; la renovación es opcional (valor referencial de lista: US$59 al año, a confirmar al momento de la compra)."],
 ["3.4 Capacitación","Una sesión por videollamada (o presencial si se coordina) antes de la recepción conforme: administración, páginas y publicaciones, imágenes y documentos, menús, usuarios y roles, y buenas prácticas de seguridad. Guía digital de uso del sitio implementado."],
 ["3.5 Hosting","Plan compartido para WordPress, contratado a nombre de la Corporación y con acceso de administración para ella: mínimo 10 GB SSD, transferencia suficiente para el sitio, PHP 8 y MySQL, SSL activo todo el período, respaldos automáticos al menos semanales con retención de 4 semanas, descarga de archivos y base de datos, y soporte técnico del proveedor. Aviso de vencimiento con 30 días de anticipación."],
 ["3.6 Mantenciones","A los 2, 4 y 6 meses: respaldo previo, actualización de WordPress, plantilla y complementos, verificación de navegación y enlaces, revisión básica de seguridad y SSL, corrección de fallas causadas por las actualizaciones e informe de cada mantención."]],[3.2*cm,w-3.2*cm]))
E.append(Spacer(1,10))
E+=section("04","Plazos","Hitos","El plazo de 30 días hábiles corre desde la formalización y la entrega de accesos y materiales")
E.append(table([["Hito","Plazo"],
 ["Diagnóstico del sitio actual, inventario y propuesta de mapa","Primeros 5 días hábiles"],
 ["Versión navegable del nuevo sitio","Hasta el día hábil 20"],
 ["Ajustes, actualización final, capacitación, accesos y publicación aprobada","Hasta el día hábil 30"],
 ["Mantención y actualización del sitio actual","Toda la transición"],
 ["Mantenciones de la nueva plataforma","Meses 2, 4 y 6 desde la recepción conforme"],
 ["Hosting","12 meses según el numeral 3.5"]],[w-6*cm,6*cm]))
E.append(PageBreak())
E+=section("05","Equipo","Equipo y responsable",None)
E.append(cards([("Kevin del Río","Socio fundador y director técnico. Instalación, configuración, migración, hosting, seguridad y mantenciones. Ingeniero en Informática (Duoc UC 2023), con experiencia en administración de servidores y plataformas web."),
 ("María Inés Cisterna","Socia fundadora y directora creativa. Responsable de coordinación con la Dirección de Comunicaciones, identidad visual, diseño de páginas, capacitación y guía."),
 ("Portafolio","<link href='https://studiosconari.cl'><u>studiosconari.cl</u></link><br/><link href='https://kdelrio.github.io'><u>kdelrio.github.io</u></link><br/><link href='https://manecist.github.io/Matrona/capsula.html'><u>manecist.github.io/Matrona</u></link>")],w))
E.append(Spacer(1,10))
E+=section("06","Entregables","Lo que recibe la Corporación",None)
E+=bullets(["Registro de modificaciones del sitio vigente durante la transición.",
 "Nuevo sitio publicado y operativo, con inventario de contenidos migrados.",
 "Acceso de administrador de WordPress y accesos del hosting bajo control de la Corporación, entregados por un canal seguro.",
 "Identificación de plantilla, complementos y licencias; respaldo completo de archivos y base de datos.",
 "Guía digital de administración y registro de la capacitación.",
 "Fechas de inicio y vencimiento del hosting, calendario de las tres mantenciones e informe de cada una."])
E.append(Spacer(1,8))
E+=section("07","Garantía","Calidad y continuidad",None)
E+=bullets(["Garantía técnica de 30 días corridos desde la recepción conforme del nuevo sitio.",
 "Corrección sin costo de los errores atribuibles a nuestras intervenciones.",
 "La Corporación queda con control total del sitio: puede administrarlo o trasladarlo sin depender de Studios Conari."])
E.append(FIRMA()); doc.build(E)

doc=Doc(os.path.join(OUT,f"Acuerdo_Confidencialidad_{COD}_StudiosConari.pdf"),f"Acuerdo de confidencialidad · {COD}","Studios Conari · Acuerdo de confidencialidad",footer_right="Declaración"); w=doc.width; E=[]
E+=section("Anexo","Compra Ágil "+COD,"Acuerdo de confidencialidad","Corporación Cultural Municipal de Puente Alto · Sitio web institucional")
E.append(Paragraph("Studios Conari SpA, RUT 78.465.252-1, representada por María Inés Cisterna Escobar, se compromete a lo siguiente respecto de la información, accesos y materiales que reciba de la Corporación Cultural Municipal de Puente Alto con ocasión de este servicio:",sty["body"]))
E.append(Spacer(1,6))
E+=bullets(["Usar la información y los accesos solo para ejecutar el servicio contratado.",
 "No divulgar, copiar ni entregar a terceros contraseñas, bases de datos, archivos ni información de la Corporación o de las personas registradas en el sitio, conforme a la Ley N.º 19.628 sobre Protección de la Vida Privada.",
 "Resguardar los accesos en un gestor de contraseñas, con autenticación de dos factores cuando el servicio lo permita, y limitar su uso a los integrantes del equipo que ejecutan el servicio.",
 "Realizar respaldos antes de cada intervención y no modificar servicios ajenos al alcance contratado.",
 "Informar de inmediato a la contraparte técnica cualquier incidente que afecte la seguridad o la continuidad del sitio.",
 "Al término del servicio, entregar todos los accesos a la Corporación y eliminar las copias de información que no sean necesarias, informándolo por escrito."])
E.append(Spacer(1,6))
E.append(Paragraph("Esta obligación se mantiene vigente durante el contrato y después de su término.",sty["body"]))
E.append(Spacer(1,14)); E.append(Paragraph("Concepción, 30 de octubre de 2026",sty["body"])); E.append(FIRMA()); doc.build(E)
print(NETO,iva,total)
