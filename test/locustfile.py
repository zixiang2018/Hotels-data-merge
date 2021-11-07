from locust import HttpUser, task

class TestUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/api/retrieve_all_hotels")