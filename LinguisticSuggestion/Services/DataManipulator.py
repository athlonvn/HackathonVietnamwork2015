#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Based on pythonized vietnamwork data - build to a suggester elasticsearch index

from LinguisticSuggestion.Services.DataImporter import getSearchDataVietnamWork
from LinguisticSuggestion.Services.Operater import getMappingOperators , getGeneralMappingData
import json

def buildSuggestionIndex(dataInput):
    operatorConfig = getMappingOperators()
    indexData = {}
    for operatorKey , operatorValue in operatorConfig.iteritems():
        docData = {}
        # Get operator key as document type
        indexData[operatorKey] = docData
        docData['title'] = operatorKey
        docData['description'] = operatorKey
        docData['tag_suggest'] = []
        if isinstance(operatorValue, str):
            isMultilevel = len(operatorValue.split(".")) > 1
            if isMultilevel:
                keyName = operatorValue.split('.')[0]
                levelName = operatorValue.split('.')[1]
                for doc in dataInput[keyName]:
                    docData['tag_suggest'].append(doc[levelName])
            else:
                try:
                    tags = dataInput[operatorValue].split(",")
                    if len(tags) > 1:
                        for t in tags:
                            try:
                                tag = getGeneralMappingData(operatorKey , t)
                            except:
                                tag = "Ho Chi Minh"
                            docData['tag_suggest'].append(tag)
                    else:
                        docData['tag_suggest'].append(tags[0])
                except:
                    tags = dataInput[operatorValue]
                    docData['tag_suggest'].append(tags)
        else:
            for docAttribute in operatorValue:
                try:
                    attributes = docAttribute.split(".")
                    if len(attributes) == 1:
                        attributes = attributes[0]
                except:
                    attributes = docAttribute

                if not isinstance(attributes, str):
                    extractData = dataInput[attributes[0]]
                    for doc in extractData:
                        docData['tag_suggest'].append(doc[attributes[1]])
                else:
                    extractData = dataInput[attributes]
                    docData['tag_suggest'].append(extractData)
    return indexData

def build():
    jobs = getSearchDataVietnamWork()
    for job in jobs[15:]:
        print buildSuggestionIndex(job)
        print '++++++++++++++++++++++++++++++++++'
    return None

build()

# dataInput =   {
#         "job_id": 577975,
#         "job_title": "Lập Trình Dot Net",
#         "job_company": "Vietnamworks",
#         "posted_date": "21/11/2015",
#         "job_location": "29,56,71",
#         "job_industry": "3,47,24",
#         "bold_red": "1",
#         "top_level": "1",
#         "job_detail_url": "http://staging.vietnamworks.com/lap-trinh-dot-net-2-577975-jd",
#         "is_show_job_logo": "1",
#         "logo_search_results": "1",
#         "job_logo_url": "http://images.staging.vietnamworks.com/pictureofcompany/c3/10214302.png",
#         "job_video_url": None,
#         "is_show_job_image": 1,
#         "job_image_url": [
#           "http://images.staging.vietnamworks.com/company_profile/22848.jpg",
#           "http://images.staging.vietnamworks.com/company_profile/22847.jpg"
#         ],
#         "salary": "Thương lượng",
#         "salary_min": 50,
#         "salary_max": 100,
#         "skills": [
#           {
#             "skillName": "QC",
#             "skillWeight": 100,
#             "skillId": 29
#           },
#           {
#             "skillName": "QA",
#             "skillWeight": 100,
#             "skillId": 5
#           },
#           {
#             "skillName": "Test",
#             "skillWeight": 100,
#             "skillId": 10
#           }
#         ],
#         "benefits": [
#           {
#             "benefitValue": "10 days full paid leave",
#             "benefitId": 1
#           }
#         ],
#         "salary_visible": False,
#         "featured_job": "1",
#         "job_level": "Nhân viên",
#         "is_show_job_tags": "1",
#         "job_tag": [
#           {
#             "skill_id": 10,
#             "tag_name": "Test",
#             "percent": 100
#           },
#           {
#             "skill_id": 5,
#             "tag_name": "QA",
#             "percent": 100
#           },
#           {
#             "skill_id": 29,
#             "tag_name": "QC",
#             "percent": 100
#           }
#         ],
#         "bold_red_categories": [],
#         "top_level_categories": [],
#         "job_post_plus": 0,
#         "top_level_tech": 0,
#         "views": 14,
#         "saved": "0",
#         "applied": "0"
# }
#
#
# print json.dumps(buildSuggestionIndex(dataInput))