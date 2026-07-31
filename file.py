from pathlib import Path

# Root project folder
ROOT = Path("gap")

# Folder structure
folders = [
    "templates/shared",
    "templates/components",
    "templates/home",
    "templates/shop",
    "templates/product",
    "templates/about",
    "templates/contact",
    "templates/auth",
]

# Files to create
files = [
    # Shared
    "templates/shared/base.html",
    "templates/shared/navbar.html",
    "templates/shared/footer.html",

    # Components
    "templates/components/hero.html",
    "templates/components/trust_bar.html",
    "templates/components/product_card.html",
    "templates/components/category_card.html",
    "templates/components/occasion_card.html",
    "templates/components/feature_card.html",
    "templates/components/testimonial_card.html",
    "templates/components/faq.html",
    "templates/components/newsletter.html",
    "templates/components/search_bar.html",
    "templates/components/breadcrumb.html",
    "templates/components/pagination.html",
    "templates/components/dream_gift_form.html",

    # Pages
    "templates/home/index.html",
    "templates/shop/shop.html",
    "templates/product/product_details.html",
    "templates/about/about.html",
    "templates/contact/contact.html",
    "templates/auth/login.html",
    "templates/auth/register.html",
]

# Create folders
for folder in folders:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

# Create files
for file in files:
    path = ROOT / file
    path.touch(exist_ok=True)

print("=" * 50)
print(" GiftAura+ Template Structure Created Successfully!")
print("=" * 50)
print(f"Project Location: {ROOT.resolve()}")