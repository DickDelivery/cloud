"""
templates is list of Template
Template structure:
- name: name of template
- greetings: list of strings, first message to send to delivery subject
- text: text to send after message has been read/replied by delivery subject
- review: review message to send to delivery subject
- picture: can be [PATH, any, math or "exact_type"], NOTE: this will be replaced with "обычный" if delivery type is "ДВОЙНОЕ"
    PATH: location to picture relative to pictures folder (e.g. "picture.png", "picture.png" must exist in pictures folder)
    any: any image from location
    match: match image to delivery type
    exact_type: string that represents exact type (обычный, конский etc.)
"""

templates = [
    {
        "name": "Вежливая доставка",
        "greetings": [
            "Здравствуйте, я по поводу посылки.",
            "Пишу вам по поводу посылки"
        ],
        "text": "На ваше имя оформлен заказ: член, половой, {product_name}. Доставка осуществляется непосредственно в личные сообщения.Примите и распишитесь. С уважением, почтовая интернет-служба",
        "review": "Оцените, пожалуйста, качество доставки по 10-бальной шкале.",
        "picture": "any"
    }
]