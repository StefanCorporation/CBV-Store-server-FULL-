from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse

class IndexViewTestCase(TestCase):
    
    def test_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'Establishment-Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):

    def test_list(self):
        path = reverse('products:products')
        response = self.client.get(path)
        print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'Products')
        self.assertEqual(response, 'products/products.html')
        
        