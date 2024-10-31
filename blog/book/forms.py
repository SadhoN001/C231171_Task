from django import forms
from book.models import Book

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_email(self):
        email= self.cleaned_data.get("email")
        if not email.endswith("@example.com"):
            raise forms.ValidationError("Email must be form example.com domain.")
        return email 
    
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','publication_date','price','description','author','publisher']
    
    def clean_price(self):
        price=self.cleaned_data.get('price')
        if price <=0:
            raise forms.ValidationError("the price must be positive !")
        return price
    

# class LogInForm(forms.Form):
#     username=forms.CharField(max_length=200)
#     password=forms.CharField(widget=forms.PasswordInput)