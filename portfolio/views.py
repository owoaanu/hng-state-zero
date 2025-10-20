from datetime import datetime, timezone

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
import requests
import logging

logger = logging.getLogger(__name__)
# Create your views here.
@api_view(['GET'])
def my_profile(request):
    cat_fact = ''

    try:
        result = requests.get(settings.CATFACT_API_URL, timeout=10)

        if result.status_code == 200:
            cat_data = result.json()
            cat_fact = cat_data['fact']
            logger.info("Fetched cat fact successfully")
        else:
            logger.error(f"Error: {result.status_code} - {result.text}")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection Error - Failed to fetch cat fact: {e}")
        cat_fact = "Could not fetch cat fact at the moment"
    except requests.exceptions.Timeout as e:
        logger.error(f"Connection Timeout - Failed to fetch cat fact: {e}")
        cat_fact = "Could not fetch cat fact at the moment"

    user = {
        "email": settings.EMAIL,
        "name": settings.NAME,
        "stack": settings.STACK
    }

    response = {
        "status":"success",
        "user": user,
        "timestamp": datetime.now(timezone.utc),
        "fact" : cat_fact
    }


    return Response(response)