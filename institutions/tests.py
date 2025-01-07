from django.test import TestCase, RequestFactory
from django.urls import reverse
from institutions.views import InstitutionListView
from institutions.models import Institution

# Create your tests here.

class InsListTest(TestCase):
    def test_ping(self):
        url = reverse('ins:ins-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ins_list_ajax(self):
        url = reverse('ins:ins-list')
        factory = RequestFactory()
        request = factory.get(url, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        response = InstitutionListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_ins_template(self):
        url = reverse('ins:ins-list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "ins/list-new.html")

class InsModelTest(TestCase):
    def test_create_ins(self):
        ins = Institution.objects.create(
            name = 'Test INS 1',
            type = "Sport",
            location = 'any_loc',
            description = 'dwdadawdawdawda',
            rating = '50',
            media = "dadwadawd"
        )
        self.assertEqual(ins.name, 'Test INS 1')
