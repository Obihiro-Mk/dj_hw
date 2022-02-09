import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student
from django.urls import reverse
import random


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_course(client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    response = client.get(url)
    assert response.status_code == 200
    assert course.id == response.data['id']


@pytest.mark.django_db
def test_list_course(client, course_factory):
    course_list = course_factory(_quantity=10)
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(course_list) == 10


@pytest.mark.django_db
def test_filter_id_course(client, course_factory):
    course_list = course_factory(_quantity=10)
    random_id = random.choice(course_list).id
    url = reverse('courses-list')
    response = client.get(url, {'id': random_id})
    assert response.status_code == 200
    assert random_id == response.data[0]['id']


@pytest.mark.django_db
def test_filter_name_course(client, course_factory):
    course_list = course_factory(_quantity=10)
    random_course = random.choice(course_list)
    url = reverse('courses-list')
    response = client.get(url, {'name': random_course.name})
    assert response.status_code == 200
    assert random_course.name == response.data[0]['name']


@pytest.mark.django_db
def test_create_course(client):
    url = reverse('courses-list')
    payload = {'name': 'AAA'}
    response = client.post(url, data=payload)
    assert response.status_code == 201
    assert response.data['name'] == payload['name']


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    payload = {'name': 'BBB'}
    response = client.patch(url, data=payload)
    assert response.status_code == 200
    assert response.data['name'] == payload['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    response = client.delete(url)
    assert response.status_code == 204
