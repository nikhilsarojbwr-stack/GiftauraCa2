from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from routes.auth_routes import router as auth_router
from routes.admin_routes import router as admin_router
from routes.product_routes import admin_router as admin_product_router
from routes.product_routes import shop_router   # import the new shop router


app = FastAPI(title="GiftAura+")

# Session middleware
app.add_middleware(
    SessionMiddleware,
    secret_key="giftaura_super_secret_key_change_this",
    max_age=60 * 60 * 24,
    https_only=False,
    same_site="lax"
)

# Disable cache (optional but good for dev)
@app.middleware("http")
async def disable_browser_cache(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates (for home, about, contact)
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(auth_router)          # /auth (login, register)
app.include_router(admin_router)         # /admin (login, dashboard)
app.include_router(admin_product_router) # /admin/products (CRUD)
app.include_router(shop_router)          # /shop (public listing & details)

# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="home/index.html")

# About and Contact pages (you can also move them to separate routers)
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(request=request, name="about/about.html")

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(request=request, name="contact/contact.html")