import os

from fastapi import APIRouter
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from pygments import highlight
from pygments.lexers import PythonLexer, PhpLexer, JavascriptLexer, GoLexer, JavaLexer
from pygments.formatters import HtmlFormatter

from internal.utils import decode

from internal.settings import settings

from services.relationships import read_all_credentials

runtimes_router = APIRouter()

async def read_all_runtimes():
    for root, dirs, files in os.walk("./languages"):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        return dirs

@runtimes_router.get("/runtimes")
async def get_all_runtimes():
    all_runtimes = await read_all_runtimes()
    all_runtimes = {runtime: {'name': settings['rt_lookup'][runtime], "services": await read_all_service_examples(runtime)} for runtime in all_runtimes}
    return all_runtimes

async def read_all_service_examples(runtime):
    for root, dirs, files in os.walk("./languages/{0}".format(runtime)):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        files = {file.split(".")[0]: {"file": file, "name": settings['rel_lookup'][file.split(".")[0].lower()] } for file in files}                
        return files

@runtimes_router.get("/runtimes/{runtime}")
async def read_connection_examples(runtime: str):
    all_runtimes = await read_all_runtimes()
    all_services = await read_all_service_examples(runtime)
    if runtime not in all_runtimes:
        raise HTTPException(status_code=404, detail="No such runtime {0}".format(runtime))
    return {
        'runtime': runtime,
        'name': settings['rt_lookup'][runtime],
        'services': all_services
    }

@runtimes_router.get("/languages/{runtime}", response_class=HTMLResponse)
async def get_single_runtime(runtime: str):
    
    service_examples = ""
    runtime_services = await read_connection_examples(runtime)
    for service in runtime_services["services"]:
        data = runtime_services["services"][service]

        with open("./languages/{0}/{1}".format(runtime, data["file"]), 'r') as file:
            file_contents = file.read()

            extension = data["file"].split(".")[1]
            if extension == "py":
                lexer = PythonLexer()
            elif extension == "php":
                lexer = PhpLexer()
            elif extension == "js":
                lexer = JavascriptLexer()
            elif extension == "go":
                lexer = GoLexer()
            elif extension == "java":
                lexer = JavaLexer()

            file_contents = highlight(file_contents, lexer, HtmlFormatter())


        all_creds = await read_all_credentials()
        content_output = "No relationship defined in app."
        if service in all_creds:
            content_output = "FOUND"
            

        service_examples += """
        <details>
            <summary>{0} Sample Code</summary>

            <h2>Source</h2>
            {1}

            <h2>Output</h2>
            
            <p>{2}</p>
        </details>
""".format(data["name"], file_contents, content_output)

    # for 

    return """
<html>
    {0}
    <body>
        <h1>Service examples for {1}</h1>

        {2}

    </body>
</html>
    """.format(
        settings['content']['head'],
        settings['rt_lookup'][runtime],
        service_examples
    )