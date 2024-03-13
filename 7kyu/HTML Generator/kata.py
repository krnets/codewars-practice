# class HTMLGen:
#     def a(self, text):
#         return f"<a>{text}</a>"

#     def b(self, text):
#         return f"<b>{text}</b>"

#     def p(self, text):
#         return f"<p>{text}</p>"

#     def body(self, text):
#         return f"<body>{text}</body>"

#     def div(self, text):
#         return f"<div>{text}</div>"

#     def span(self, text):
#         return f"<span>{text}</span>"

#     def title(self, text):
#         return f"<title>{text}</title>"

#     def comment(self, text):
#         return f"<!--{text}-->"


class HTMLGen:
    a = lambda self, text: f"<a>{text}</a>"
    b = lambda self, text: f"<b>{text}</b>"
    p = lambda self, text: f"<p>{text}</p>"
    div = lambda self, text: f"<div>{text}</div>"
    body = lambda self, text: f"<body>{text}</body>"
    span = lambda self, text: f"<span>{text}</span>"
    title = lambda self, text: f"<title>{text}</title>"
    comment = lambda self, text: f"<!--{text}-->"
