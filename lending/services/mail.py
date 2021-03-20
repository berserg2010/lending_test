from django.core.mail import send_mail


def send_form_data(form_data) -> None:
    body = (
        f'{form_data.get("name")}\n'
        f'{form_data.get("phone")}\n'
        f'{form_data.get("email")}\n'
    )
    send_mail(
        'Гамбит',
        body,
        'admin@localhost',
        ['admin@localhost'],
    )
