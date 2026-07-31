# 🎁 GiftAura – Premium Customized Gifts

**GiftAura** is a modern, fully responsive e‑commerce website that offers **handcrafted, personalized gifts** for every occasion. The platform allows users to browse best‑selling products, shop by category or occasion, and submit a custom gift request – all within a beautifully designed interface.

---

## ✨ Features

- **Hero Section** – Engaging headline, call‑to‑action buttons, and a trust bar highlighting key benefits.
- **Best Sellers Carousel** – Showcases top products with “bestseller” badges, wishlist icons, and quick‑view hover actions.
- **Shop by Category** – Visual grid with overlays for gift categories (For Her, For Him, Couples, etc.).
- **Shop by Occasion** – Icon‑based cards for Birthday, Anniversary, Valentine’s, Christmas, etc.
- **Design Your Dream Gift** – A custom order form with fields for name, email, occasion, delivery date, and file upload.
- **Why Choose Us** – Feature grid highlighting core values (handmade, personalised, free shipping, 24/7 support).
- **Customer Testimonials** – Scrollable cards with real reviews and star ratings.
- **FAQ Accordion** – Clean, two‑column list of frequently asked questions.
- **Responsive Navigation** – Sticky header with search bar, wishlist, cart badge, and mobile hamburger menu.
- **Footer** – Brand info, quick links, customer service, newsletter signup, and social icons.

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Frontend**: HTML5, CSS3 (custom), JavaScript (vanilla)
- **Templating**: [Jinja2](https://jinja.palletsprojects.com/)
- **Fonts**: Google Fonts (Playfair Display, Poppins, Great Vibes)
- **Icons**: Embedded SVG & Unicode symbols

---

## 📁 Project Structure

```
gap/
├── static/
│   ├── css/
│   │   └── style.css          # All global styles
│   ├── images/                # (optional) product/avatar images
│   └── js/                    # (optional) external JavaScript
├── templates/
│   ├── about/
│   │   └── about.html
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── components/
│   │   ├── best_sellers_section.html
│   │   ├── breadcrumb.html
│   │   ├── category_card.html
│   │   ├── category_section.html
│   │   ├── dream_gift_form.html
│   │   ├── faq.html
│   │   ├── feature_card.html
│   │   ├── hero.html
│   │   ├── newsletter.html
│   │   ├── occasion_card.html
│   │   ├── occasion_section.html
│   │   ├── pagination.html
│   │   ├── product_card.html
│   │   ├── search_bar.html
│   │   ├── testimonial_card.html
│   │   ├── testimonials_section.html
│   │   ├── trust_bar.html
│   │   └── why_choose.html
│   ├── contact/
│   │   └── contact.html
│   ├── home/
│   │   └── index.html         # Homepage (includes all sections)
│   ├── product/
│   │   └── product_details.html
│   ├── shared/
│   │   ├── base.html          # Main layout with navbar, footer, scripts
│   │   ├── footer.html
│   │   └── navbar.html
│   └── shop/
│       └── shop.html
├── .gitignore
├── main.py                     # FastAPI application entry point
├── requirements.txt
├── README.md
└── PROJECT_STRUCTURE.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd gap
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

### 5. Open your browser

Visit [http://localhost:8000](http://localhost:8000) – you should see the GiftAura homepage.

---

## 🧩 How It Works

- **Templates** are rendered using **Jinja2** with a modular component approach.
- Each section (Hero, Best Sellers, Categories, etc.) lives in its own file under `templates/components/`.
- The `base.html` provides the common layout (navbar, footer, styles, scripts).
- All static assets (CSS, images, JS) are served from the `/static` folder.
- The homepage (`index.html`) simply includes all section components – making it clean and easy to maintain.

---

## 🧪 Customisation

- **Styles**: All CSS variables are defined in `static/css/style.css` – you can easily change colours, fonts, spacing, etc.
- **Content**: Replace static product cards, category items, testimonials, and FAQ entries with your own data (or connect to a database).
- **Forms**: The “Design Your Dream Gift” form currently shows an alert on submit; you can connect it to an email endpoint or a database.

---

## 📦 Deployment

For production deployment:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Consider using `gunicorn` with `uvicorn.workers.UvicornWorker` for better concurrency, or deploy on platforms like **Render**, **Heroku**, or **AWS**.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- Built with ❤️ using FastAPI and Jinja2.
- Design inspired by modern gift‑shop aesthetics.
- Special thanks to all the open‑source libraries that made this possible.

---

**GiftAura** – *Every Gift Becomes A Beautiful Memory* ✦