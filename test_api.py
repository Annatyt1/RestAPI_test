import allure
from api_func import check_status_code, get_image, upload_image, delete_image


@allure.title("Get image no id")
@allure.description("This test is for getting an image without id")
def test_get_image_no_id():
    status_code, response = get_image()
    check_status_code(status_code, 400)


@allure.title("Image upload success")
@allure.description("This test is for uploading image success")
def test_upload_image():
    response, status_code = upload_image()

    check_status_code(status_code, 201)


@allure.title("Delete image success")
@allure.description("This test is for deleting image success")
def test_delete_image():
    upload_response, status_code = upload_image()
    status_code = delete_image(upload_response.id)

    check_status_code(status_code, 204)


@allure.title("Check delete image success")
@allure.description("This test is for check image deleted successfully")
def test_check_delete_image():
    upload_response, status_code = upload_image()
    delete_image(upload_response.id)
    status_code, response = get_image(upload_response.id)

    check_status_code(status_code, 400)
