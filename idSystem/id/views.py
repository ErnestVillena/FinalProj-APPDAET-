from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import IdCredentials, IdType
from .forms import IdCredentialsForm, IdTypeForm

@login_required
def id_list(request):
    search_query = request.GET.get('q', '')
    selected_category = request.GET.get('category', 'all')

    id_types = IdType.objects.all()
    #credentials = IdCredentials.objects.all()
    #id_types = IdType.objects.filter(owner_id=request.user.id)
    credentials = IdCredentials.objects.filter(owner_id=request.user.id)

    if search_query:
        credentials = credentials.filter(idCred_name__icontains=search_query)

    if selected_category != 'all':
        credentials = credentials.filter(id_types__id=selected_category)

    context = {
        'credentials': credentials,
        'id_types': id_types,
        'search_query': search_query,
        'selected_category': selected_category,
    }
    return render(request, 'id_list.html', context)


def id_add(request):
    if request.method == 'POST':

        if 'confirm_save' in request.POST:

            cred_form = IdCredentialsForm(request.POST)
            type_form = IdTypeForm(request.POST)

            if cred_form.is_valid() and type_form.is_valid():
                id_cred = cred_form.save()
                id_type = type_form.save(commit=False)
                id_type.owner = id_cred
                id_type.save()
                messages.success(request, "ID and details saved!")
                return redirect('id:id-list')
            else:
                messages.error(request, "Error saving data. Please try again.")

        else:
            cred_form = IdCredentialsForm(request.POST, request.FILES)
            type_form = IdTypeForm(request.POST, request.FILES)

            if 'preview' in request.POST:
                if cred_form.is_valid() and type_form.is_valid():
                    return render(request, 'id_preview.html', {
                        'credential': cred_form.save(commit=False),
                        'id_types': [type_form.save(commit=False)],
                    })

            if cred_form.is_valid() and type_form.is_valid():
                id_cred = cred_form.save()
                id_type = type_form.save(commit=False)
                id_type.owner = id_cred
                id_type.save()
                messages.success(request, "ID and details saved!")
                return redirect('id:id-list')
    else:
        cred_form = IdCredentialsForm()
        type_form = IdTypeForm()

    return render(request, 'id_add.html', {
        'cred_form': cred_form,
        'type_form': type_form
    })


def id_edit(request, pk):
    credential = get_object_or_404(IdCredentials, pk=pk)
    id_type_qs = IdType.objects.filter(owner=credential)
    id_type = id_type_qs.first() if id_type_qs.exists() else IdType(owner=credential)

    if request.method == 'POST':
        if 'confirm_save' in request.POST:
            cred_form = IdCredentialsForm(request.POST, request.FILES, instance=credential)
            type_form = IdTypeForm(request.POST, request.FILES, instance=id_type)

            if cred_form.is_valid() and type_form.is_valid():
                cred_form.save()
                type_form.save()
                messages.success(request, "ID and details updated successfully!")
                return redirect('id:id-detail', pk=credential.pk)
            else:
                messages.error(request, "Error saving data. Please fix errors and try again.")
                return render(request, 'id_edit.html', {
                    'cred_form': cred_form,
                    'type_form': type_form,
                    'credential': credential,
                })

        elif 'preview' in request.POST:
            cred_form = IdCredentialsForm(request.POST, request.FILES, instance=credential)
            type_form = IdTypeForm(request.POST, request.FILES, instance=id_type)

            if cred_form.is_valid() and type_form.is_valid():
                credential_preview = cred_form.save(commit=False)
                id_type_preview = type_form.save(commit=False)
                id_type_preview.owner = credential_preview

                return render(request, 'id_preview.html', {
                    'credential': credential_preview,
                    'id_types': [id_type_preview],
                    'edit_mode': True,
                    'credential_pk': credential.pk,
                })
            else:
                messages.warning(request, "Please fix the errors before previewing.")
                return render(request, 'id_edit.html', {
                    'cred_form': cred_form,
                    'type_form': type_form,
                    'credential': credential,
                })

        elif 'save' in request.POST:
            cred_form = IdCredentialsForm(request.POST, request.FILES, instance=credential)
            type_form = IdTypeForm(request.POST, request.FILES, instance=id_type)

            if cred_form.is_valid() and type_form.is_valid():
                cred_form.save()
                type_form.save()
                messages.success(request, "ID and details updated successfully!")
                return redirect('id:id-detail', pk=credential.pk)
            else:
                return render(request, 'id_edit.html', {
                    'cred_form': cred_form,
                    'type_form': type_form,
                    'credential': credential,
                })

        else:
            cred_form = IdCredentialsForm(instance=credential)
            type_form = IdTypeForm(instance=id_type)
            return render(request, 'id_edit.html', {
                'cred_form': cred_form,
                'type_form': type_form,
                'credential': credential,
            })

    else:
        cred_form = IdCredentialsForm(instance=credential)
        type_form = IdTypeForm(instance=id_type)
        return render(request, 'id_edit.html', {
            'cred_form': cred_form,
            'type_form': type_form,
            'credential': credential,
        })

def id_delete(request, pk):
    credential = get_object_or_404(IdCredentials, pk=pk)
    if request.method == 'POST':
        credential.delete()
        messages.success(request, "ID deleted successfully!")
        return redirect('id:id-list')
    return render(request, 'id_confirm_delete.html', {'credential': credential})


def id_detail(request, pk):
    credential = get_object_or_404(IdCredentials, pk=pk)
    return render(request, 'id_detail.html', {'credential': credential})


def id_preview(request):
    """Show preview of new ID before saving."""

    if request.method == 'POST':
        cred_form = IdCredentialsForm(request.POST, request.FILES)
        type_form = IdTypeForm(request.POST, request.FILES)

        if cred_form.is_valid() and type_form.is_valid():
            credential = cred_form.save(commit=False)
            id_type = type_form.save(commit=False)
            id_type.owner = credential  

            return render(request, 'id_preview.html', {
                'credential': credential,
                'id_types': [id_type], 
            })

        else:
            messages.warning(request, "Please fix the errors before previewing.")
            return render(request, 'id_add.html', {
                'cred_form': cred_form,
                'type_form': type_form
            })

    return redirect('id:id-add')
