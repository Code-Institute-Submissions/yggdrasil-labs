from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages

from yggdrasil_labs.utils.check_internet_explorer import check_internet_explorer
from products.models import Product
from .forms import ContactForm


def index(request):
    """
    Renders the index view.
    """
    products = Product.objects.filter(featured=True)
    if check_internet_explorer(request):
        return render(request, "pages/internet-explorer.html")
    context = {
        "products": products,
        "body_class": "body-index",
    }
    return render(request, "pages/index.html", context)


def contact(request):
    """
    Renders a view with a form to contact the business.
    """
    form = ContactForm()
    user = request.user
    if request.user.is_authenticated:
        form = ContactForm(initial={"email": user.email})

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            reply_email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            email_template = get_template("pages/contact-email.txt")
            email_content = email_template.render({"content": content})
            email = EmailMessage(
                "Contact Form",
                email_content,
                to=["contact@yggdrasillabs.com"],
                headers={"Reply-to": reply_email},
            )
            try:
                email.send()
                messages.success(
                    request,
                    "Message sent. We will get back to you as soon as possible.",
                )
                return redirect("index")
            except Exception as e:
                messages.error(request, f"Message not sent, error! {e}")
                return redirect("contact")

    context = {
        "page_title": "Contact Us",
        "form": form,
    }
    return render(request, "pages/contact.html", context)


def about(request):
    """
    Renders a view with information about the business.
    """
    context = {
        "page_title": "About Us",
        "body_class": "body-about",
    }
    return render(request, "pages/about.html", context)
