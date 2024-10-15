from datetime import datetime, timedelta

from utils.check_token_expiration_date import check_token_expiration_date  
from api.profile.profile import get_profiles, open_profile_by_id  

from dotenv import load_dotenv
# Загружаем переменные окружения из .env файла
load_dotenv()

# Основная функция
def main():
    check_token_expiration_date()

    # Получаем все профили
    profiles = get_profiles()
        
    if not profiles:
        print("Нет доступных профилей.")
        return

    print(f"Найдено {len(profiles)} профилей.")

    for profile in profiles:
        
        id = profile["id"]
        open_profile_by_id(id)
        
        return
        
    return


if __name__ == "__main__":
    main()