import flet as ft

def main(page: ft.Page) -> tuple:

    page.title = "Chat"
    submitted_message = ft.TextField(label="Enter your message")

    def submit_message(e):
        page.add(ft.Text(submitted_message.value))
    
    page.add(submitted_message, ft.ElevatedButton(
        "Send", on_click=submit_message))

if __name__ == "__main__":
    ft.app(target=main)
