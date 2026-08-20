# routes/admin_routes.py

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from services.admin_service import AdminService
from services.product_service import ProductService


router = APIRouter(prefix="/admin", tags=["Admin"])
templates = Jinja2Templates(directory="templates")

admin_service = AdminService()
product_service = ProductService()


def require_admin(request: Request):
    return request.session.get("admin_logged_in")


@router.get("/login", response_class=HTMLResponse)
async def admin_login_page(request: Request):
    if require_admin(request):
        return RedirectResponse(url="/admin/dashboard", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="admin/login.html",
        context={"message": None}
    )


@router.post("/login", response_class=HTMLResponse)
async def admin_login(
    request: Request,
    login: str = Form(...),
    password: str = Form(...)
):
    admin = admin_service.authenticate_admin(login=login, password=password)
    if not admin:
        return templates.TemplateResponse(
            request=request,
            name="admin/login.html",
            context={"message": "Invalid username/email or password."},
            status_code=401
        )
    request.session.clear()
    request.session["admin_logged_in"] = True
    request.session["admin_id"] = str(admin["_id"])
    request.session["admin_username"] = admin.get("username", "Admin")
    request.session["admin_role"] = admin.get("role", "admin")
    return RedirectResponse(url="/admin/dashboard", status_code=303)


@router.get("/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    if not require_admin(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    admin_username = request.session.get("admin_username", "Admin")

    try:
        total_products = product_service.count_products()          # ✅ fixed method
        category_counts_list = product_service.get_category_counts()  # returns list of dicts
        total_categories = product_service.count_categories()      # ✅ fixed method

        # Convert list to dict for template
        category_counts = {item["_id"]: item["count"] for item in category_counts_list}
    except Exception as e:
        print(f"❌ Dashboard product statistics error: {e}")
        total_products = 0
        total_categories = 0
        category_counts = {}

    return templates.TemplateResponse(
        request=request,
        name="admin/dashboard.html",
        context={
            "admin_username": admin_username,
            "total_products": total_products,
            "total_categories": total_categories,
            "category_counts": category_counts
        }
    )


@router.post("/logout")
async def admin_logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/admin/login", status_code=303)