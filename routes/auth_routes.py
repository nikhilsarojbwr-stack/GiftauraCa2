from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.user import User
from services.auth_service import AuthService


router = APIRouter()

templates = Jinja2Templates(
    directory="templates"
)

auth_service = AuthService()


# =====================================================
# REGISTER PAGE
# =====================================================

@router.get(
    "/register",
    response_class=HTMLResponse
)
async def register_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="auth/register.html"
    )


# =====================================================
# REGISTER
# =====================================================

@router.post("/register")
async def register_user(

    request: Request,

    full_name: str = Form(...),

    email: str = Form(...),

    phone: str = Form(...),

    password: str = Form(...),

    confirm_password: str = Form(...)

):

    # Check password confirmation

    if password != confirm_password:

        return templates.TemplateResponse(

            request=request,

            name="auth/register.html",

            context={
                "message": "Passwords do not match.",
                "full_name": full_name,
                "email": email,
                "phone": phone
            },

            status_code=400
        )

    # Create user

    user = User(

        full_name=full_name,

        email=email,

        phone=phone,

        password=password

    )

    # Register

    result = auth_service.register_user(user)

    if not result["success"]:

        return templates.TemplateResponse(

            request=request,

            name="auth/register.html",

            context={
                "message": result["message"],
                "full_name": full_name,
                "email": email,
                "phone": phone
            },

            status_code=400
        )

    # Registration successful

    return RedirectResponse(

        url="/login",

        status_code=303

    )


# =====================================================
# LOGIN PAGE
# =====================================================

@router.get(
    "/login",
    response_class=HTMLResponse
)
async def login_page(request: Request):

    # If already logged in
    if request.session.get("user_id"):

        return RedirectResponse(
            url="/",
            status_code=303
        )

    return templates.TemplateResponse(

        request=request,

        name="auth/login.html"

    )


# =====================================================
# LOGIN
# =====================================================

@router.post("/login")
async def login_user(

    request: Request,

    email: str = Form(...),

    password: str = Form(...)

):

    result = auth_service.login_user(

        email,

        password

    )

    # Login failed

    if not result["success"]:

        return templates.TemplateResponse(

            request=request,

            name="auth/login.html",

            context={
                "message": result["message"],
                "email": email
            },

            status_code=401

        )

    # =================================================
    # CREATE SESSION
    # =================================================

    user = result["user"]

    # Clear old session first

    request.session.clear()

    # Store only required information

    request.session["user_id"] = str(
        user["_id"]
    )

    request.session["user_name"] = (
        user["full_name"]
    )

    request.session["user_email"] = (
        user["email"]
    )

    # Login successful

    return RedirectResponse(

        url="/",

        status_code=303

    )


# =====================================================
# LOGOUT
# =====================================================

@router.get("/logout")
async def logout(request: Request):

    # Clear session

    request.session.clear()

    # Redirect to login

    response = RedirectResponse(

        url="/login",

        status_code=303

    )

    # Prevent cached authenticated page

    response.headers["Cache-Control"] = (
        "no-store, no-cache, must-revalidate, max-age=0"
    )

    response.headers["Pragma"] = "no-cache"

    response.headers["Expires"] = "0"

    return response