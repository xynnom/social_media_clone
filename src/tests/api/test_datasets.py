"""Test for Datasets"""
from fastapi.testclient import TestClient


def test_get_datasets(client: TestClient):
    response = client.get('/datasets')
    assert response.status_code == 200


def test_get_dataset_files(client: TestClient):
    response = client.get('/datasets/101/files')
    assert response.status_code == 404


def test_get_file_detail_not_exist(client: TestClient):
    response = client.get('/datasets/101/files/1')
    assert response.status_code == 404


def test_get_dataset_not_exist(client: TestClient):
    response = client.get('/datasets/101')
    assert response.status_code == 404
