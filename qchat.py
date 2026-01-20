from uuid import uuid4
from nicegui import ui

chat_history = []

@ui.refreshable
def display_messages(user_id):
    for uid, avatar_url, message in chat_history:
        ui.chat_message(avatar=avatar_url, text=message, sent=uid == user_id)

@ui.page('/')
def home():
    def send_message():
        chat_history.append((current_user, user_avatar, message_input.value))
        display_messages.refresh()
        message_input.value = ''

    current_user = str(uuid4())
    user_avatar = f'https://robohash.org/{current_user}?bgset=bg2'

    with ui.column().classes('w-full items-stretch'):
        display_messages(current_user)

    with ui.footer().classes('bg-white'):
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(user_avatar)
            message_input = ui.input(placeholder='Type your message...') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', send_message)


ui.run()
