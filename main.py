from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="GiftAura+")

# ----------------------------
# Static Files
# ----------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# ----------------------------
# Templates
# ----------------------------
templates = Jinja2Templates(directory="templates")


# ----------------------------
# Home
# ----------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home/index.html",
    )


# ----------------------------
# Shop
# ----------------------------
@app.get("/shop", response_class=HTMLResponse)
async def shop(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="shop/shop.html",
    )


# ----------------------------
# About
# ----------------------------
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about/about.html",
    )


# ----------------------------
# Contact
# ----------------------------
@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact/contact.html",
    )


# ----------------------------
# Login
# ----------------------------
@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/login.html",
    )


# ----------------------------
# Register
# ----------------------------
@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/register.html",
    )