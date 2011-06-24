from django.shortcuts import render_to_response
from django.template.context import RequestContext
import demo.forms

def echo(request):
    form_number = int(request.POST.get('form_number', 0))
    context = {
        'form_number': form_number
    }

    form_instances = []
    form_names = ['EchoForm0', 'EchoForm1', 'EchoForm2', 'EchoForm3', 'EchoForm4']
    for form_name in form_names:
        form_class = getattr(demo.forms, form_name)
        form_instances.append(form_class())

    if request.method == 'POST':
        form_instance = form_instances[form_number].__class__(request.POST)
        form_instances[form_number] = form_instance
        context['has_error'] = not form_instance.is_valid()

    context['forms'] = form_instances

    return render_to_response('index.html', context_instance=RequestContext(request, context))
