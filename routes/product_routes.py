from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from uuid import uuid4

from services.product_service import ProductService


# ============================================================
# Shared Templates & Service
# ============================================================
templates = Jinja2Templates(directory="templates")
product_service = ProductService()

# ============================================================
# Image Configuration (shared)
# ============================================================
PRODUCT_IMAGE_DIR = Path("static/images/products")
PRODUCT_IMAGE_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_IMAGE_TYPES = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp"
}
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB


async def save_product_image(image: UploadFile):
    if not image or not image.filename:
        return None
    if image.content_type not in ALLOWED_IMAGE_TYPES:
        raise ValueError("Only JPG, PNG and WEBP images are allowed.")
    contents = await image.read()
    if len(contents) > MAX_IMAGE_SIZE:
        raise ValueError("Image size must be less than 5 MB.")
    extension = ALLOWED_IMAGE_TYPES[image.content_type]
    filename = f"{uuid4().hex}{extension}"
    file_path = PRODUCT_IMAGE_DIR / filename
    with open(file_path, "wb") as f:
        f.write(contents)
    return f"/static/images/products/{filename}"


def delete_product_image(image_path):
    if not image_path:
        return
    prefix = "/static/images/products/"
    if not image_path.startswith(prefix):
        return
    filename = Path(image_path).name
    file_path = PRODUCT_IMAGE_DIR / filename
    if file_path.exists():
        try:
            file_path.unlink()
        except OSError:
            pass


def require_admin(request: Request):
    return request.session.get("admin_logged_in")


# ============================================================
# ADMIN ROUTER (prefix /admin/products)
# ============================================================
admin_router = APIRouter(prefix="/admin/products", tags=["Admin Products"])


@admin_router.get("", response_class=HTMLResponse)
async def products_page(request: Request):
    if not require_admin(request):
        return RedirectResponse(url="/admin/login", status_code=303)
    products = product_service.get_all_products()
    return templates.TemplateResponse(
        request=request,
        name="admin/products.html",
        context={"products": products}
    )


@admin_router.get("/add", response_class=HTMLResponse)
async def add_product_page(request: Request):
    if not require_admin(request):
        return RedirectResponse(url="/admin/login", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="admin/add_product.html",
        context={"message": None}
    )


@admin_router.post("/add", response_class=HTMLResponse)
async def add_product(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    price: float = Form(...),
    category: str = Form(...),
    image: UploadFile | None = File(None)
):
    if not require_admin(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    name = name.strip()
    description = description.strip()
    category = category.strip()

    if not name:
        return templates.TemplateResponse(
            request=request,
            name="admin/add_product.html",
            context={"message": "Product name is required."}
        )
    if not category:
        return templates.TemplateResponse(
            request=request,
            name="admin/add_product.html",
            context={"message": "Please select a category."}
        )
    if price < 0:
        return templates.TemplateResponse(
            request=request,
            name="admin/add_product.html",
            context={"message": "Price cannot be negative."}
        )

    image_path = None
    try:
        if image and image.filename:
            image_path = await save_product_image(image)
    except ValueError as error:
        return templates.TemplateResponse(
            request=request,
            name="admin/add_product.html",
            context={"message": str(error)}
        )

    try:
        product_id = product_service.create_product(
            name=name,
            description=description,
            image=image_path,
            price=price,
            category=category
        )
    except Exception:
        delete_product_image(image_path)
        return templates.TemplateResponse(
            request=request,
            name="admin/add_product.html",
            context={"message": "Could not add product. Please try again."}
        )

    if not product_id:
        delete_product_image(image_path)
        return templates.TemplateResponse(
            request=request,
            name="admin/add_product.html",
            context={"message": "Could not add product."}
        )

    return RedirectResponse(url="/admin/products", status_code=303)


@admin_router.get("/edit/{product_id}", response_class=HTMLResponse)
async def edit_product_page(request: Request, product_id: str):
    if not require_admin(request):
        return RedirectResponse(url="/admin/login", status_code=303)
    product = product_service.get_product_by_id(product_id)
    if not product:
        return RedirectResponse(url="/admin/products", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="admin/edit_product.html",
        context={"product": product, "message": None}
    )


@admin_router.post("/edit/{product_id}", response_class=HTMLResponse)
async def update_product(
    request: Request,
    product_id: str,
    name: str = Form(...),
    description: str = Form(""),
    price: float = Form(...),
    category: str = Form(...),
    image: UploadFile | None = File(None)
):
    if not require_admin(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    product = product_service.get_product_by_id(product_id)
    if not product:
        return RedirectResponse(url="/admin/products", status_code=303)

    name = name.strip()
    description = description.strip()
    category = category.strip()

    if not name:
        return templates.TemplateResponse(
            request=request,
            name="admin/edit_product.html",
            context={"product": product, "message": "Product name is required."}
        )
    if not category:
        return templates.TemplateResponse(
            request=request,
            name="admin/edit_product.html",
            context={"product": product, "message": "Please select a category."}
        )
    if price < 0:
        return templates.TemplateResponse(
            request=request,
            name="admin/edit_product.html",
            context={"product": product, "message": "Price cannot be negative."}
        )

    old_image_path = product.get("image")
    new_image_path = old_image_path
    new_image_uploaded = False

    try:
        if image and image.filename:
            new_image_path = await save_product_image(image)
            new_image_uploaded = True
    except ValueError as error:
        return templates.TemplateResponse(
            request=request,
            name="admin/edit_product.html",
            context={"product": product, "message": str(error)}
        )

    success = product_service.update_product(
        product_id=product_id,
        name=name,
        description=description,
        image=new_image_path,
        price=price,
        category=category
    )

    if not success:
        if new_image_uploaded:
            delete_product_image(new_image_path)
        return templates.TemplateResponse(
            request=request,
            name="admin/edit_product.html",
            context={"product": product, "message": "Could not update product. Please try again."}
        )

    if new_image_uploaded and old_image_path and old_image_path != new_image_path:
        delete_product_image(old_image_path)

    return RedirectResponse(url="/admin/products", status_code=303)


@admin_router.post("/delete/{product_id}")
async def delete_product(request: Request, product_id: str):
    if not require_admin(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    product = product_service.get_product_by_id(product_id)
    if not product:
        return RedirectResponse(url="/admin/products", status_code=303)

    success = product_service.delete_product(product_id)
    if success:
        delete_product_image(product.get("image"))
    return RedirectResponse(url="/admin/products", status_code=303)


# ============================================================
# PUBLIC SHOP ROUTER (prefix /shop)
# ============================================================
shop_router = APIRouter(prefix="/shop", tags=["Shop"])


@shop_router.get("", response_class=HTMLResponse)
async def shop_page(request: Request):
    """List all products for the public shop."""
    products = product_service.get_all_products()
    return templates.TemplateResponse(
        request=request,
        name="shop/shop.html",
        context={"products": products}
    )


@shop_router.get("/product/{product_id}", response_class=HTMLResponse)
async def product_details(request: Request, product_id: str):
    """Public product details page."""
    product = product_service.get_product_by_id(product_id)
    if not product:
        return RedirectResponse(url="/shop", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="product/product_details.html",
        context={"product": product}
    )