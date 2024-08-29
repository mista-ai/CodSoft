from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


# View for the contact list
def contact_list(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 4)  # Show 4 contacts per page

    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)

    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


# View for adding a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})


# View for updating a contact
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update_contact.html', {'form': form})


# View for deleting a contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})


# View for searching contacts
def search_contact(request):
    query = request.GET.get('q', '')

    if query:
        contact_list = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(
            phone_number__icontains=query)
    else:
        contact_list = Contact.objects.all()  # If no query, show all contacts (or you can use .none() to show no contacts)

    paginator = Paginator(contact_list, 4)  # Show 4 contacts per page
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)

    return render(request, 'contacts/contact_list.html', {'contacts': contacts, 'query': query})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})
