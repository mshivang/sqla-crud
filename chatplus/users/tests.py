from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

def getUser():
    return User.objects.create(
            username = "shivang",
            password = "QWERTY@1234",
            email = "shivangmishra0824@gmail.com",
        )

class UserIndexViewTests(TestCase):
    def test_returns_users_if_found(self):
        """
        Returns user list if users are found.
        """

        res = self.client.post("/dj-rest-auth/registration/", {
            "username": "dina",
            "password1": "QWERTY@ui",
            "password2": "QWERTY@ui",
            "email": "shivang@gmail.com",
        }, content_type="application/json")

        user = User.objects.get(username="dina")
        user.is_superuser = True
        user.save()

        access_token_res_json = res.json()
        access_token = access_token_res_json["access"]

        # Add the access token to the HTTP_AUTHORIZATION header
        headers = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)}

        response = self.client.get(reverse("users:index"), **headers)
        res_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(res_json["users"]), 0)

class UserDetailViewTests(TestCase):
    def test_user_fetch_by_id(self):
        """
        Returns user by given id.
        """
        res = self.client.post("/dj-rest-auth/registration/", {
            "username": "dina",
            "password1": "QWERTY@ui",
            "password2": "QWERTY@ui",
            "email": "shivang@gmail.com",
        }, content_type="application/json")

        user = User.objects.get(username="dina")
        user.is_superuser = True
        user.save()

        access_token_res_json = res.json()
        access_token = access_token_res_json["access"]

        # Add the access token to the HTTP_AUTHORIZATION header
        headers = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)}

        userCreated = getUser()

        url = reverse("users:detail", args=(userCreated.id,))
        response = self.client.get(url, **headers)
        res_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_json["status"], "success")

    def test_user_delete(self):
        """
        Deletes user by given id.
        """

        res = self.client.post("/dj-rest-auth/registration/", {
            "username": "dina",
            "password1": "QWERTY@ui",
            "password2": "QWERTY@ui",
            "email": "shivang@gmail.com",
        }, content_type="application/json")

        user = User.objects.get(username="dina")
        user.is_superuser = True
        user.save()

        access_token_res_json = res.json()
        access_token = access_token_res_json["access"]

        # Add the access token to the HTTP_AUTHORIZATION header
        headers = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)}

        userCreated = getUser()

        url = reverse("users:detail", args=(userCreated.id,))
        response = self.client.delete(url, **headers)

        self.assertEqual(response.status_code, 204)

    def test_does_not_delete_user_with_invalid_id(self):
        """
        Prevents user from deleting user with invalid id.
        """

        res = self.client.post("/dj-rest-auth/registration/", {
            "username": "dina",
            "password1": "QWERTY@ui",
            "password2": "QWERTY@ui",
            "email": "shivang@gmail.com",
        }, content_type="application/json")

        user = User.objects.get(username="dina")
        user.is_superuser = True
        user.save()

        access_token_res_json = res.json()
        access_token = access_token_res_json["access"]

        # Add the access token to the HTTP_AUTHORIZATION header
        headers = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)}

        getUser()

        url = reverse("users:detail", args=("random_id",))
        response = self.client.delete(url, **headers)
        res_json = response.json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(res_json["status"], "fail")


