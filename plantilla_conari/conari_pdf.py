"""Plantilla PDF con el estilo Studios Conari (según Dossier Blanco)."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                Image, KeepTogether, PageBreak, NextPageTemplate)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
A=os.path.join(os.path.dirname(__file__),"..","conari")
pdfmetrics.registerFont(TTFont("NS",os.path.join(A,"NotoSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("NSB",os.path.join(A,"NotoSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("NSI",os.path.join(A,"NotoSans-Italic.ttf")))
from reportlab.lib.fonts import addMapping
addMapping("NS",0,0,"NS"); addMapping("NS",1,0,"NSB"); addMapping("NS",0,1,"NSI"); addMapping("NS",1,1,"NSB")
LOGO=os.path.join(A,"logo.png")
NAVY=colors.HexColor("#15294a"); NAVY2=colors.HexColor("#233d63"); GOLD=colors.HexColor("#a8780f")
GRAY=colors.HexColor("#58657a"); CREAM=colors.HexColor("#f7efd8"); LINEG=colors.HexColor("#eadcb4"); LGRAY=colors.HexColor("#c4c9d1")
W,H=A4
sty=dict(
 body=ParagraphStyle("body",fontName="NS",fontSize=9,leading=13,textColor=NAVY2),
 small=ParagraphStyle("small",fontName="NS",fontSize=8,leading=11,textColor=NAVY2),
 label=ParagraphStyle("label",fontName="NSB",fontSize=8,leading=11,textColor=GOLD),
 sec=ParagraphStyle("sec",fontName="NSB",fontSize=8.5,leading=11,textColor=GOLD,spaceBefore=4),
 title=ParagraphStyle("title",fontName="NSB",fontSize=17,leading=21,textColor=GOLD),
 sub=ParagraphStyle("sub",fontName="NS",fontSize=9,leading=12,textColor=GRAY,spaceAfter=8),
 h=ParagraphStyle("h",fontName="NSB",fontSize=9.5,leading=13,textColor=GOLD,spaceBefore=6,spaceAfter=4),
 ctitle=ParagraphStyle("ct",fontName="NSB",fontSize=20,leading=25,textColor=NAVY,alignment=TA_CENTER),
 csub=ParagraphStyle("cs",fontName="NS",fontSize=10,leading=14,textColor=GRAY,alignment=TA_CENTER),
 ckick=ParagraphStyle("ck",fontName="NSB",fontSize=10,leading=14,textColor=GOLD,alignment=TA_CENTER),
 cfoot=ParagraphStyle("cf",fontName="NS",fontSize=9,leading=13,textColor=GRAY,alignment=TA_CENTER),
 bullet=ParagraphStyle("bul",fontName="NS",fontSize=9,leading=13,textColor=NAVY2,leftIndent=10,bulletIndent=0),
)
def frame_deco(c):
    c.setStrokeColor(NAVY); c.setLineWidth(0.8); c.rect(0.9*cm,0.9*cm,W-1.8*cm,H-1.8*cm)
    c.setStrokeColor(GOLD); c.setLineWidth(0.6); c.rect(1.05*cm,1.05*cm,W-2.1*cm,H-2.1*cm)
def diamond(c,x,y,s=3):
    p=c.beginPath(); p.moveTo(x,y+s); p.lineTo(x+s,y); p.lineTo(x,y-s); p.lineTo(x-s,y); p.close()
    c.setFillColor(colors.white); c.setStrokeColor(GOLD); c.setLineWidth(0.6); c.drawPath(p,fill=1,stroke=1)
class Doc(BaseDocTemplate):
    def __init__(self,path,header_text,footer_text,footer_right="Documento de oferta",**kw):
        super().__init__(path,pagesize=A4,leftMargin=2.2*cm,rightMargin=2.2*cm,topMargin=3.6*cm,bottomMargin=2.6*cm,**kw)
        self.header_text=header_text; self.footer_text=footer_text; self.footer_right=footer_right
        fr=Frame(self.leftMargin,self.bottomMargin,self.width,self.height,id="f",leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        cfr=Frame(self.leftMargin,2.4*cm,self.width,H-4.8*cm,id="c",leftPadding=0,rightPadding=0)
        self.addPageTemplates([PageTemplate(id="cover",frames=[cfr],onPage=self._cover),PageTemplate(id="page",frames=[fr],onPage=self._page)])
    def _cover(self,c,d): frame_deco(c)
    def _page(self,c,d):
        frame_deco(c)
        lw=3.0*cm; lh=lw*362/620; x=(W-lw)/2; y=H-1.55*cm-lh
        c.drawImage(LOGO,x,y,lw,lh,mask="auto")
        c.setStrokeColor(LGRAY); c.setLineWidth(0.5)
        ym=y+lh*0.42; c.line(2.2*cm,ym,x-0.3*cm,ym); c.line(x+lw+0.3*cm,ym,W-2.2*cm,ym)
        c.setFont("NSB",7.5); c.setFillColor(GRAY); c.drawRightString(W-2.2*cm,ym+3,self.header_text.upper())
        yf=2.05*cm; c.setStrokeColor(LGRAY); c.line(2.2*cm,yf,W/2-6,yf); c.line(W/2+6,yf,W-2.2*cm,yf); diamond(c,W/2,yf)
        c.setFont("NSB",7.5); c.setFillColor(GRAY); c.drawString(2.2*cm,yf-0.5*cm,self.footer_text.upper())
        c.setFont("NS",7.5); c.drawRightString(W-2.2*cm,yf-0.75*cm,f"{self.footer_right}     Página {d.page}")
def section(num,kick,title,sub=None):
    out=[Paragraph(f"{num} · {kick.upper()}",sty["sec"]),Paragraph(title.upper(),sty["title"])]
    if sub: out.append(Paragraph(sub,sty["sub"]))
    else: out.append(Spacer(1,6))
    return out
def callout(label,text,width):
    inner=[Paragraph(label.upper(),sty["label"]),Spacer(1,3),Paragraph(text,sty["body"])]
    t=Table([["",inner]],colWidths=[0.45*cm,width-0.45*cm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(0,0),CREAM),("BOX",(0,0),(-1,-1),0.6,LINEG),
        ("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(1,0),(1,0),10),("RIGHTPADDING",(1,0),(1,0),10),
        ("TOPPADDING",(1,0),(1,0),9),("BOTTOMPADDING",(1,0),(1,0),9)]))
    return t
def cards(items,width,cols=3,minh=None):
    rows=[]; row=[]
    for lab,txt in items:
        row.append([Paragraph(lab.upper(),sty["label"]),Spacer(1,3),Paragraph(txt,sty["small"])])
        if len(row)==cols: rows.append(row); row=[]
    if row: rows.append(row+[""]*(cols-len(row)))
    t=Table(rows,colWidths=[width/cols]*cols,rowHeights=minh)
    t.setStyle(TableStyle([("GRID",(0,0),(-1,-1),0.6,LINEG),("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9)]))
    return t
def table(data,widths,head=True,bold_last=0,right_cols=()):
    P=lambda v,s: v if not isinstance(v,str) else Paragraph(v,s)
    rows=[]
    for i,r in enumerate(data):
        s=sty["label"] if (head and i==0) else sty["small"]
        if bold_last and i>=len(data)-bold_last: s=ParagraphStyle("bl",parent=sty["small"],fontName="NSB",textColor=NAVY)
        rows.append([P(v,ParagraphStyle("r",parent=s,alignment=TA_RIGHT) if j in right_cols else s) for j,v in enumerate(r)])
    t=Table(rows,colWidths=widths,repeatRows=1 if head else 0)
    st=[("GRID",(0,0),(-1,-1),0.6,LINEG),("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]
    if head: st.append(("BACKGROUND",(0,0),(-1,0),CREAM))
    if bold_last: st.append(("BACKGROUND",(0,len(data)-1),(-1,len(data)-1),CREAM))
    t.setStyle(TableStyle(st)); return t
def bullets(items): return [Paragraph(i,sty["bullet"],bulletText="•") for i in items]
def cover(kicker,title,subtitle,info,uso,foot,width):
    lw=12*cm; lh=lw*362/620
    out=[Spacer(1,1.2*cm),Image(LOGO,lw,lh),Spacer(1,0.4*cm),Paragraph(kicker.upper(),sty["ckick"]),Spacer(1,4),
         Paragraph(title,sty["ctitle"]),Spacer(1,6),Paragraph(subtitle,sty["csub"]),Spacer(1,1.6*cm),
         cards(info,width,cols=len(info)),Spacer(1,1.2*cm),callout(uso[0],uso[1],width),Spacer(1,1.2*cm),
         Paragraph(foot,sty["cfoot"]),NextPageTemplate("page"),PageBreak()]
    return out
def signature(name,role,company,img=None):
    head=[Spacer(1,0.6*cm)]
    if img:
        from PIL import Image as PI
        iw,ih=PI.open(img).size; w=3.4*cm; im=Image(img,w,w*ih/iw); im.hAlign="LEFT"; head+=[im,Spacer(1,-4)]
    else: head=[Spacer(1,1.4*cm)]
    return KeepTogether(head+[Paragraph("_______________________________",sty["body"]),
        Paragraph(f"<b>{name}</b>",sty["body"]),Paragraph(role,sty["small"]),Paragraph(company,sty["small"])])
