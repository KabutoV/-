from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, KeepTogether, PageTemplate, Paragraph,
    Spacer, Table, TableStyle
)

HERE = Path(__file__).resolve().parent
OUT = str(HERE / "Zhang_Yuanmin_Resume.pdf")
PHOTO = str(HERE / "portrait.png")

pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
FONT = "STSong-Light"
BLUE = colors.HexColor("#164E78")
MID_BLUE = colors.HexColor("#356986")
TEXT = colors.HexColor("#253746")
MUTED = colors.HexColor("#5A6875")
PALE = colors.HexColor("#F4F7F9")

doc = BaseDocTemplate(
    OUT, pagesize=A4,
    leftMargin=15*mm, rightMargin=15*mm,
    topMargin=12*mm, bottomMargin=10*mm,
    title="张远民｜数据处理与运营支持简历",
    author="张远民",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates(PageTemplate(id="resume", frames=frame))

styles = getSampleStyleSheet()
name = ParagraphStyle("name", fontName=FONT, fontSize=24, leading=28, textColor=colors.HexColor("#102B45"), spaceAfter=2*mm)
role = ParagraphStyle("role", fontName=FONT, fontSize=10.6, leading=14, textColor=MID_BLUE, spaceAfter=2.2*mm)
contact = ParagraphStyle("contact", fontName=FONT, fontSize=9.2, leading=12, textColor=MUTED)
heading = ParagraphStyle("heading", fontName=FONT, fontSize=12.3, leading=15, textColor=BLUE, spaceBefore=4.1*mm, spaceAfter=2.1*mm)
body = ParagraphStyle("body", fontName=FONT, fontSize=9.25, leading=14.7, textColor=TEXT, alignment=TA_LEFT)
small = ParagraphStyle("small", fontName=FONT, fontSize=9.05, leading=14.1, textColor=TEXT)
entry = ParagraphStyle("entry", fontName=FONT, fontSize=9.7, leading=13, textColor=colors.HexColor("#172D40"))
date = ParagraphStyle("date", fontName=FONT, fontSize=8.7, leading=12, textColor=MUTED, alignment=2)

def H(title):
    return Paragraph(f'<font color="#1F739B">▌</font> <b>{title}</b>', heading)

def bullet(text):
    return Paragraph(text, small, bulletText="•")

story = []
photo = Image(PHOTO, width=31.5*mm, height=42*mm)
photo.hAlign = "RIGHT"
left_header = [
    Paragraph("<b>张远民</b>", name),
    Paragraph("数据处理｜运营支持｜报表分析", role),
    Paragraph("男｜23岁　　z18523365370@163.com", contact),
]
header = Table([[left_header, photo]], colWidths=[doc.width-41.5*mm, 31.5*mm], hAlign="LEFT")
header.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 0),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3*mm),
    ("LINEBELOW", (0,0), (-1,-1), 1.3, BLUE),
]))
story += [header]

story += [H("个人优势"), Paragraph(
    "具备数据整理、异常核对与报表输出经验，熟悉从数据采集、清洗、统计到复盘输出的完整流程。能够使用 Python、Excel 与 Power Query 处理业务数据，并借助 AI 编程工具提升脚本编写和信息整理效率。", body)]

story += [H("专业技能")]
skills = [
    ("数据处理", "清洗、字段标准化、重复值与异常值核对"),
    ("Excel", "VLOOKUP/XLOOKUP、SUMIFS、COUNTIFS、数据透视表"),
    ("Python", "Pandas、OpenPyXL，批量处理与自动化报表"),
    ("分析工具", "Power Query、基础数据可视化与统计模板"),
    ("业务分析", "曝光、点击、转化、销量与库存指标整理"),
    ("效率工具", "ChatGPT、Kimi、Codex 等 AI 辅助工具"),
]
skill_rows = []
for i in range(0, len(skills), 2):
    skill_rows.append([
        Paragraph(f"<b>{skills[i][0]}：</b>{skills[i][1]}", small),
        Paragraph(f"<b>{skills[i+1][0]}：</b>{skills[i+1][1]}", small),
    ])
skill_table = Table(skill_rows, colWidths=[doc.width/2-2.5*mm]*2, hAlign="LEFT")
skill_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 2*mm),
    ("TOPPADDING", (0,0), (-1,-1), .5*mm), ("BOTTOMPADDING", (0,0), (-1,-1), .5*mm),
]))
story.append(skill_table)

story += [H("项目经历")]
project = [
    Paragraph("<b>Python 商品数据清洗分析</b>｜模拟业务项目", entry),
    bullet("使用 Python/Pandas 对商品明细、库存、曝光、点击与成交等字段进行清洗、合并和统计，建立标准化数据台账。"),
    bullet("结合 Excel 高级函数与数据透视表处理异常价格、空字段、重复 SKU 和标题关键词，按商品、类目及周期输出汇总表。"),
    bullet("拆解点击率、转化率、客单价等指标，形成页面内容、活动资源位和价格策略的优化建议。"),
]
proj_table = Table([[project]], colWidths=[doc.width], hAlign="LEFT")
proj_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), PALE), ("LINEBEFORE", (0,0), (0,-1), 2.5, colors.HexColor("#3F7F9E")),
    ("LEFTPADDING", (0,0), (-1,-1), 3*mm), ("RIGHTPADDING", (0,0), (-1,-1), 3*mm),
    ("TOPPADDING", (0,0), (-1,-1), 2*mm), ("BOTTOMPADDING", (0,0), (-1,-1), 1.5*mm),
]))
story.append(proj_table)

story += [H("工作经历")]
def job(company, position, dates, bullets):
    head = Table([[Paragraph(f"<b>{company}</b>｜{position}", entry), Paragraph(dates, date)]], colWidths=[doc.width-37*mm, 37*mm])
    head.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "BASELINE"), ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0), ("TOPPADDING", (0,0), (-1,-1), 0), ("BOTTOMPADDING", (0,0), (-1,-1), .8*mm)]))
    return KeepTogether([head] + [bullet(x) for x in bullets])

story.append(job("峨边康源农业科技发展有限公司", "技术员", "2025.06—至今", [
    "负责生产数据的日常录入、核对与台账维护，整理产仔数、存活率、断奶率及健康巡检等关键指标，保障数据准确完整。",
    "使用 Excel 搭建生产日报/周报模板，完成筛选、分类汇总、异常标记和基础统计，提高报表整理与数据追踪效率。",
    "标准化处理历史生产记录，核对漏填、重复及口径不一致数据；协助补充电子档案并沉淀常用登记模板。",
    "参与部门电脑资料、生产文件和流程表单整理，减少重复录入与后续查询成本。",
]))
story.append(Spacer(1, 1.6*mm))
story.append(job("深圳市笛曼科技有限公司", "运营技术助理", "2024.07—2024.12", [
    "维护业务后台商品数据，完成商品上架、标题/卖点整理、详情页信息校对、SKU 属性核验及基础数据更新。",
    "整理商品曝光、点击、转化、销量及库存数据，使用 Excel 进行清洗、筛选、汇总与异常标记。",
    "按活动、商品和渠道维度输出运营报表，为商品优化、活动复盘与库存调整提供数据支持。",
]))

story += [H("教育经历")]
edu = Table([[Paragraph("<b>深圳职业技术大学</b>｜AI 技术应用专业", entry), Paragraph("2021—2024", date)]], colWidths=[doc.width-37*mm, 37*mm])
edu.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0), ("TOPPADDING", (0,0), (-1,-1), 0), ("BOTTOMPADDING", (0,0), (-1,-1), 0)]))
story.append(edu)

doc.build(story)
print(OUT)
