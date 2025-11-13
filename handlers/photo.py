from aiogram import Dispatcher, F
from aiogram.types import Message


async def handle_photo(message: Message):
    """Обработчик фотографий - возвращает file_id"""
    if message.photo:
        # Берем самое большое фото (последнее в списке)
        photo = message.photo[-1]
        file_id = photo.file_id
        file_unique_id = photo.file_unique_id
        
        response_text = f"""
📸 Информация о фото:

🆔 File ID: `{file_id}`
🔑 File Unique ID: `{file_unique_id}`
📏 Размер: {photo.width}x{photo.height}
📦 Размер файла: {photo.file_size or 'неизвестно'} байт
"""
        await message.answer(response_text, parse_mode="Markdown")
    elif message.document:
        # Если это документ (может быть изображение)
        file_id = message.document.file_id
        file_unique_id = message.document.file_unique_id
        
        response_text = f"""
📄 Информация о документе:

🆔 File ID: `{file_id}`
🔑 File Unique ID: `{file_unique_id}`
📝 Имя файла: {message.document.file_name or 'неизвестно'}
📦 Размер файла: {message.document.file_size or 'неизвестно'} байт
📋 MIME тип: {message.document.mime_type or 'неизвестно'}
"""
        await message.answer(response_text, parse_mode="Markdown")


def register_photo_handlers(dp: Dispatcher):
    """Регистрация обработчиков фотографий"""
    # Регистрируем обработчик для фотографий и документов
    dp.message.register(handle_photo, F.photo)
    dp.message.register(handle_photo, F.document)

