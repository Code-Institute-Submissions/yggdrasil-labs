from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form linked to Order model for creating orders in the database.
    """

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "city",
            "postcode",
            "state",
            "country",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "city": "City",
            "postcode": "Postcode",
            "state": "State or locality",
        }
        self.fields["full_name"].widget.attrs["autofocus"] = True
        self.fields["country"].widget.attrs["aria-label"] = "country (required)"
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} (required)"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
                self.fields[field].widget.attrs["aria-label"] = placeholder
            self.fields[field].label = False
