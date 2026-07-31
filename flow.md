Start with the **shared components**, not the pages.

A professional website is built from the **outside in**:

* Build the global layout first.
* Then build reusable UI components.
* Finally assemble the pages from those components.

## Phase 1 – Shared Layout

Build these files first:

```text
templates/shared/

base.html
navbar.html
footer.html
```

These will be used on every page.

---

## Phase 2 – Core Components

Build these reusable components next.

```text
hero.html
trust_bar.html
product_card.html
category_card.html
occasion_card.html
feature_card.html
testimonial_card.html
faq.html
dream_gift_form.html
```

These are the main building blocks of your homepage.

---

## Phase 3 – Home Page

Now create the homepage by including the components.

```text
home/index.html

Navbar

↓

Hero

↓

Trust Bar

↓

Best Sellers (product_card)

↓

Categories (category_card)

↓

Occasions (occasion_card)

↓

Dream Gift Form

↓

Why Choose Us (feature_card)

↓

Testimonials

↓

FAQ

↓

Footer
```

At this stage, your homepage should look almost identical to the design mockup.

---

## Phase 4 – Shop

```text
shop/shop.html

Navbar

↓

Search Bar

↓

Category Cards

↓

Product Cards

↓

Pagination

↓

Footer
```

---

## Phase 5 – Product Details

```text
product/product_details.html

Navbar

↓

Breadcrumb

↓

Product Images

↓

Product Information

↓

Related Products (product_card)

↓

FAQ

↓

Footer
```

---

## Phase 6 – Remaining Pages

Build the simpler pages after the main shopping experience is complete:

```text
about/about.html

contact/contact.html

auth/login.html

auth/register.html
```

---

# Recommended Development Order

```text
1. base.html ⭐⭐⭐⭐⭐

2. navbar.html ⭐⭐⭐⭐⭐

3. footer.html ⭐⭐⭐⭐⭐

4. hero.html

5. trust_bar.html

6. product_card.html

7. category_card.html

8. occasion_card.html

9. feature_card.html

10. testimonial_card.html

11. faq.html

12. dream_gift_form.html

13. home/index.html

14. shop/shop.html

15. product/product_details.html

16. about/about.html

17. contact/contact.html

18. login.html

19. register.html
```

### Why this order?

By the time you reach `home/index.html`, almost everything is already built. The homepage becomes mostly a matter of assembling reusable components, for example:

```html
{% extends "shared/base.html" %}

{% block content %}

{% include "components/hero.html" %}
{% include "components/trust_bar.html" %}
{% include "components/product_card.html" %}
{% include "components/category_card.html" %}
{% include "components/occasion_card.html" %}
{% include "components/dream_gift_form.html" %}
{% include "components/feature_card.html" %}
{% include "components/testimonial_card.html" %}
{% include "components/faq.html" %}

{% endblock %}
```

This is how Flask projects are commonly structured: **shared layout → reusable components → pages**. It keeps the code organized and makes future changes much easier because you only update a component once instead of editing multiple pages.
