import sender_stand_request
import configuration
import data

def test_create_and_get_order():
    create_order_response = sender_stand_request.create_order()
    
    assert create_order_response.status_code == 201, f"Ошибка: {create_order_response.status_code}"
    
    track_number = create_order_response.json()["track"]
    print(f"Создан заказ с трек-номером: {track_number}")
    
    get_order_response = sender_stand_request.get_order_by_track(track_number)
    
    assert get_order_response.status_code == 200, f"Ошибка: {get_order_response.status_code}"
    print("Заказ успешно получен по трек-номеру")
    
    order_info = get_order_response.json()
    assert order_info["order"]["firstName"] == data.order_data["firstName"], "Имя не совпадает"
    assert order_info["order"]["phone"] == data.order_data["phone"], "Телефон не совпадает"
    
    print("Тест успешно пройден!")

    test_create_and_get_order()