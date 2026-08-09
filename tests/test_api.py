from fastapi.testclient import TestClient

from decision_support_platform.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_profile_endpoint() -> None:
    response = client.post(
        "/api/v1/datasets/profile",
        files={"file": ("sample.csv", b"id,value\n1,10\n2,20\n", "text/csv")},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["row_count"] == 2
    assert body["overall_passed"] is True


def test_rejects_non_csv_file() -> None:
    response = client.post(
        "/api/v1/datasets/profile",
        files={"file": ("sample.txt", b"hello", "text/plain")},
    )
    assert response.status_code == 415
