import requests
import allure
from api_response import ImageData, UploadImage


api_url = "https://api.thedogapi.com/v1/images/"
api_key = "live_UFBPf2lhtmG9bMRlPFFdb14w8hdqnnVVM9x4aZncXaPec4btbNWFu73046eGz6Ct"

headers = {
    "x-api-key": api_key
}


@allure.step
def check_status_code(actual_status_code, expect_status_code):
    assert actual_status_code == expect_status_code


@allure.step
def get_image(img_id=""):
    url = api_url + img_id
    response = requests.get(url)
    if response.status_code == 200:
        response.status_code, ImageData(**response.json())
    return response.status_code, None


@allure.step
def upload_image():
    url = api_url + "upload"
    with open("images/dog.jpeg", "rb") as img_file:
        files = {
            "file": ("images/dog.jpeg", img_file, "image/jpeg")
        }
        response = requests.post(url, headers=headers, files=files)

        return UploadImage(**response.json()), response.status_code


@allure.step
def delete_image(image_id):
    url = api_url + image_id
    response = requests.delete(url, headers=headers)

    return response.status_code
