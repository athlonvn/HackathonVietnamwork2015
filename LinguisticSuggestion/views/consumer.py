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

class GetResult(APIView):
    """
    <b>Get search result</b>
    <p>Fetch in the search phrase for the result</p>
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


class GetSuggestions(APIView):
    """
    <b>Get suggestions</b>
    <p>Get search suggestion</p>
    <h3>Get parameter:</h3>
    <ul>
        <li><p><u>operator</u>:</p>name of the operator</li>
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


class GetOperators(APIView):
    """
    <b>Get list of operator</b>
    <p>Get list of operators</p>
    <h3>Get parameter:</h3>
    <ul>
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