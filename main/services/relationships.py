import os

from fastapi import APIRouter
from fastapi import FastAPI, HTTPException

from internal.utils import decode

relationships_router = APIRouter()

async def sanitize_credentials(credentials, relationship):
    # credentials['password'] = "_".join([relationship.upper(), 'PASSWORD'])
    return credentials

@relationships_router.get("/relationships")
async def read_all_credentials():
    return decode(os.environ['PLATFORM_RELATIONSHIPS'])

@relationships_router.get("/relationships/{relationship}")
async def read_service_credentials(relationship: str):
    all_creds = await read_all_credentials()

    if relationship not in all_creds:
        raise HTTPException(status_code=404, detail="No such service {0}".format(relationship))
    return await sanitize_credentials(
        all_creds[relationship][0], 
        relationship)

@relationships_router.get("/variables/{relationship}")
async def read_service_variables(relationship: str):
    all_creds = await read_all_credentials()

    if relationship not in all_creds:
        raise HTTPException(status_code=404, detail="No such service {0}".format(relationship))
    
    creds = await sanitize_credentials(
        all_creds[relationship][0], 
        relationship)

    vars = {"{0}_{1}".format(relationship.upper(), key.upper()): creds[key] for key in creds}

    return vars
