from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from services.relationships import relationships_router, read_all_credentials
from languages.runtime import runtimes_router, read_all_runtimes
from internal.settings import settings
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(relationships_router, prefix=settings['API_STR'])
app.include_router(runtimes_router, prefix=settings['API_STR'])

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_items():

    # List available service/relationships.
    all_rels = await read_all_credentials()
    content_rels = ""
    for relationship in all_rels:
        content_rels += "<li><a href=\"{0}/relationships/{1}\">{2}</a></li>".format(
            settings['API_STR'], 
            relationship, 
            settings['rel_lookup'][relationship])

    # List available runtimes.
    all_runtimes = await read_all_runtimes()
    content_runtimes = ""
    for runtime in all_runtimes:
        content_runtimes += "<li><a href=\"{0}/languages/{1}\">{2}</a></li>".format(
            settings['API_STR'], 
            runtime, 
            settings['rt_lookup'][runtime])        


    return """
<html>
    {0}
    <body>
        <h1>Upsun examples</h1>
        <h2>What relationships look like</h2>
        <ul>
            {1}
        </ul>

        <h2>Languages</h2>
        <ul>
            {2}
        </ul>

        <!-- <ul>
            <li><a href="/golang">Go</a></li>
            <li><a href="/java">Java</a></li>
            <li><a href="/nodejs">Node.js</a></li>
            <li><a href="/php">PHP</a></li>
            <li><a href="/python">Python</a></li>
        </ul> -->

    </body>
</html>
    """.format(
        settings['content']['head'],
        content_rels,
        content_runtimes
    )
