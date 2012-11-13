# -*- coding: gb2312 -*-
#-------------------------------------------------------------------------------
# Name:        mxdExport
# Purpose:     ���� ArcGIS MXD �ĵ�Ϊ��ͼͼ��
#
# Author:      Gerald Chen
#
# Created:     12/11/2012
# Copyright:   (c) Gerald 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# ע�⣺��·�����ļ����������ַ�ʱ��ȷ�����ű��ļ������ʽΪ ANSI

# ���봦��ģ��
import arcpy

# �����������·��
inpath = r"L:\\Archiving\\��ˮ��Ҫ�ؿ�\\�ɹ�ͼ�����\\"
print "MXD�ĵ�λ�ã�" + inpath
outpath = r"L:\\Archiving\\��ˮ��Ҫ�ؿ�\\"
print "���ͼ��λ�ã�" + outpath + '\n'

# ���������ļ��嵥
inmxd = ["CTD��׼������AUT10m_�ܶ�", "CTD��׼������AUT10m_����", "CTD��׼������AUT10m_ˮ��", "CTD��׼������AUT10m_�ζ�", "CTD��׼������AUT10m_�Ƕ�"]

# ѭ���������
for m in inmxd:
    print m + "...ͼ�����������..."
    mxd = arcpy.mapping.MapDocument(inpath + m + ".mxd")
    arcpy.mapping.ExportToPDF(mxd, outpath + m + ".pdf")
    # print "��ɣ�"
    
print "����ͼ��������ɣ�����ļ�λ�ã�" + outpath
del mxd
del inmxd