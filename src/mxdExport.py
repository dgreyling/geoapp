# -*- coding: gb2312 -*-
#-------------------------------------------------------------------------------
# Name:        mxdExport
# Purpose:     导出 ArcGIS MXD 文档为地图图像
#
# Author:      Gerald Chen
#
# Created:     12/11/2012
# Copyright:   (c) Gerald 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# 注意：在路径及文件名含中文字符时，确保本脚本文件编码格式为 ANSI

# 导入处理模块
import arcpy

# 定义输入输出路径
inpath = r"L:\\Archiving\\粤水体要素库\\成果图集输出\\"
print "MXD文档位置：" + inpath
outpath = r"L:\\Archiving\\粤水体要素库\\"
print "输出图件位置：" + outpath + '\n'

# 列入输入文件清单
inmxd = ["CTD标准层数据AUT10m_密度", "CTD标准层数据AUT10m_声速", "CTD标准层数据AUT10m_水温", "CTD标准层数据AUT10m_盐度", "CTD标准层数据AUT10m_浊度"]

# 循环处理输出
for m in inmxd:
    print m + "...图件输出进行中..."
    mxd = arcpy.mapping.MapDocument(inpath + m + ".mxd")
    arcpy.mapping.ExportToPDF(mxd, outpath + m + ".pdf")
    # print "完成！"
    
print "所有图件处理完成，输出文件位置：" + outpath
del mxd
del inmxd