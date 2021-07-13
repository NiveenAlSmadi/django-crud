  
from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

class SnacksCRUDTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'niveen',
            email = 'niv98@gmail.com',
            password = '112233ni'
        )
        self.snack = Snack.objects.create(
            title = 'Marshmello',
            description  = 'sweet',
            purchaser = self.user
        )


    def test_snack_list_view(self):
        url = reverse('snack_list')
        actual_status_code = self.client.get(url).status_code
        self.assertEqual(actual_status_code, 200)

    def test_snack_details_view(self):
        response = self.client.get(reverse('snack_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_update_view(self):
        response = self.client.post(reverse('snack_update', args='1'), {
            'title':'Bonda' ,
        })
        self.assertContains(response, 'Bonda')
        
   
    def test_snack_create_view(self):
        response = self.client.post(reverse("snack_create"),
            {
                "title": "Nuts",
                "description": "Nuts are an ideal nutritious snack.",
                "purchaser": self.user
            })

     
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nuts')
        self.assertContains(response, 'Nuts are an ideal nutritious snack.')
        self.assertContains(response, 'niveen')


    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)
   
