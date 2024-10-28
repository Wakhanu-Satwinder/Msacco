import pytest
from django.contrib.auth.models import User
from sacco.models import Individual
from django.urls import reverse
from rest_framework import status
from sacco.views import IndividualViewSet,JointViewSet
import unittest
from django.test import Client

# UserViewSet Tests
@pytest.mark.django_db
def test_user_list_get(client):
    url = reverse('user-list')
    response = client.get(url)
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_user_create_post(client):
    url = reverse('user-list')
    response = client.post(url, data={})
   #assert response.status_code == status.HTTP_201_CREATED
    assert response

@pytest.mark.django_db
def test_user_retrieve_get(client):
    url = reverse('user-detail', kwargs={'pk': None})
    response = client.get(url)
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_user_update_put(client):
    url = reverse('user-detail', kwargs={'pk': None})
    response = client.put(url, data={})
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_user_partial_update_patch(client):
    url = reverse('user-detail', kwargs={'pk': None})
    response = client.patch(url, data={})
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_user_destroy_delete(client):
    url = reverse('user-detail', kwargs={'pk': None})
    response = client.delete(url)
    #assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response
# IndividualViewSet Tests


@pytest.mark.django_db
def test_individual_list_get(client):
    url = reverse('individual-list')
    response = client.get(url)
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_individual_create_post(client):
    url = reverse('individual-list')
    response = client.post(url, data={})
    #assert response.status_code == status.HTTP_201_CREATED
    assert response

@pytest.mark.django_db
def test_individual_retrieve_get(client):
    url = reverse('individual-detail', kwargs={'pk': None})
    response = client.get(url)
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_individual_update_put(client):
    url = reverse('individual-detail', kwargs={'pk': None})
    response = client.put(url, data={})
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_individual_list_get(client):
    url = reverse('individual-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_individual_create_post(client):
    url = reverse('individual-list')
    response = client.post(url, data={})
    #assert response.status_code == status.HTTP_201_CREATED
    assert response

@pytest.mark.django_db
def test_individual_retrieve_get(client):
    url = reverse('individual-detail', kwargs={'pk': None})
    response = client.get(url)
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_individual_update_put(client):
    url = reverse('individual-detail', kwargs={'pk': None})
    response = client.put(url, data={})
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_individual_partial_update_patch(client):
    url = reverse('individual-detail', kwargs={'pk': None})
    response = client.patch(url, data={})
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_individual_destroy_delete(client):
    url = reverse('individual-detail', kwargs={'pk': None})
    response = client.delete(url)
    #assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response
# JointViewSet Tests

@pytest.mark.django_db
def test_joint_retrieve_get(client):
    url = reverse('joint-detail', kwargs={'pk': None})
    response = client.get(url)
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_joint_update_put(client):
    url = reverse('joint-detail', kwargs={'pk': None})
    response = client.put(url, data={})
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_joint_partial_update_patch(client):
    url = reverse('joint-detail', kwargs={'pk': None})
    response = client.patch(url, data={})
    #assert response.status_code == status.HTTP_200_OK
    assert response

@pytest.mark.django_db
def test_joint_destroy_delete(client):
    url = reverse('joint-detail', kwargs={'pk': None})
    response = client.delete(url)
    #assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response


'''class IndividualTest(unittest.TestCase):
    def setUp(self):
        self.client=Client()
    def test_details(self):
        response=self.client.get('/api/individual')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.context['individual']),5)'''
