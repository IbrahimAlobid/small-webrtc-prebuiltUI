from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pipecat_ai_small_webrtc_prebuilt.frontend import SmallWebRTCPrebuiltUI

app = FastAPI()

# Mount the frontend at /prebuilt
app.mount("/prebuilt", SmallWebRTCPrebuiltUI)

@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/prebuilt/")