from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import *
from institutions.models import *
from auth_system.models import *
from institutions.forms import *
from institutions.mixing import *
from django.http import JsonResponse

# Create your views here.


from django.http import JsonResponse

class InstitutionListView(ListView):
    model = Institution
    template_name = "ins/ins-list.html"
    context_object_name = "institutions"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        institution_type = self.request.GET.get('type', '')
        if institution_type:
            queryset = queryset.filter(type=institution_type)
        return queryset

    def get(self, request):
        super().get(request)

        if request.headers.get('x-requested-with') == "XMLHttpRequest":
            return render(request, 'ins/list-new.html', context=self.get_context_data())

        return render(request, self.template_name, context=self.get_context_data())

class SearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        if query:
            results = Institution.objects.filter(name__icontains=query)[:10]  # Пошук за ім'ям
            data = [{"id": ins.id, "name": ins.name} for ins in results]
        else:
            data = []

        return JsonResponse({"results": data})

class InstitutionDetailView(DetailView):
    model = Institution
    context_object_name = "ins"
    template_name = "ins/ins-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        institution = self.get_object()
        reviews = Review.objects.filter(institution=institution)
        ins_rates = [review.rate for review in reviews]
        if ins_rates:
            institution.rating = sum(ins_rates) / len(ins_rates)
            institution.save()
        else:
            institution.save()
        context["reviews"] = reviews
        context["review_form"] = ReviewForm(self.request.GET)
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.institution = self.get_object()
            review.save()
            return redirect('ins:ins-detail', pk=review.institution.pk)
        else:
            # Тут можна обробити випадок з невалідною формою
            pass



class ReviewUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Review
    template_name = "ins/review_update.html"
    form_class = ReviewForm
    context_object_name = "review"

    def get_success_url(self):
        return reverse_lazy("ins:ins-detail", kwargs={'pk': self.object.institution.pk})



class ReviewDeleteView(LoginRequiredMixin, UserIsOwnerAndAdminMixin, DeleteView):
    model = Review
    context_object_name = "review"

    def get_success_url(self):
        return reverse_lazy("ins:ins-detail", kwargs={'pk': self.object.institution.pk})

class InstitutionCreateView(LoginRequiredMixin, CreateView):
    model = Institution
    template_name = "ins/ins-create.html"
    form_class = InsForm
    success_url = reverse_lazy("ins:ins-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class InstitutionUpdateView(LoginRequiredMixin, UserIsAdminOrModerMixin, UpdateView):
    model = Institution
    template_name = "ins/ins_update.html"
    form_class = InsForm
    context_object_name = "ins"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ins:ins-detail", kwargs={'pk': self.object.pk})

class InstitutionDeleteView(LoginRequiredMixin, UserIsAdminOrModerMixin, DeleteView):
    model = Institution
    context_object_name = "ins"

    def get_success_url(self):
        return reverse_lazy("ins:ins-list")

