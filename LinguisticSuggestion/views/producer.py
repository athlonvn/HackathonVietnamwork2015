from __future__ import absolute_import
from rest_framework.views import APIView
from django.http import JsonResponse


class Index(APIView):
    """
    <b>Index</b>
    <p>Index</p>
    <h3>Get parameter:</h3>
    <ul>
        <li><p><u></u>:</p></li>
    </ul>
    <h1>Response info</h1>
    <p>A json string</p>
    <h3>In case success</h3>
    <ul>
        <li><u>error</u>: 0</li>
        <li><u>message</u>: a complete description string</li>
        <li><u>data</u>: None</li>
    </ul>
    <h3>In case failed</h3>
    <ul>
        <li><u>error</u>: 1</li>
        <li><u>message</u>: a complete description string</li>
        <li><u>data</u>: None</li>
    </ul>
    """

    def get(self, request, *args, **kwargs):
        return JsonResponse({"hello":"hackathon"})



class BuildSuggestFromOperator(APIView):
    """
    <b>Build Suggest From Operator</b>
    <p></p>
    <h3>Get parameter:</h3>
    <ul>
        <li><p><u></u>:</p></li>
    </ul>
    <h1>Response info</h1>
    <p>A json string</p>
    <h3>In case success</h3>
    <ul>
        <li><u>error</u>: 0</li>
        <li><u>message</u>: a complete description string</li>
        <li><u>data</u>: None</li>
    </ul>
    <h3>In case failed</h3>
    <ul>
        <li><u>error</u>: 1</li>
        <li><u>message</u>: a complete description string</li>
        <li><u>data</u>: None</li>
    </ul>
    """

    def get(self, request, *args, **kwargs):
        return JsonResponse({"hello":"hackathon"})