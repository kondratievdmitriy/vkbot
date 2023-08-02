import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from course_1 import get_course
from wiki_1 import get_wiki_article
from requests.exceptions import ReadTimeout, ProxyError

token = 'vk1.a.MF2Rt5gjsvgXkZCAVq-Ux957MZeMZnx0RYjhh2F7L_LBWA7DADUjAzHsBVUMtTE4-zCT9jI-h25K_O4awoE8a-qnwKrYmOViO4XfkbMQ3kvBpkSO41ogP6Gjj-IlQrLmTGsFA1MKPoA0N42Dhgsw2P2WMAkINL0vJ-mtNp2y_s9nlre5O9uQxs-5sjv3szGTxSl3KzeufH--XlJW64JIwA'

while True:
    try:
        vk_session = vk_api.VkApi(token = token)
        vk = vk_session.get_api()

        longpoll = VkLongPoll(vk_session)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                msg = event.text.lower()
                user_id = event.user_id
                random_id = random.randint(1, 10 ** 10)
                if msg == '-к':
                    responce = '{0} рублей за 1 доллар\n {1} рублей за 1 евро\n'\
                                '{2} рублей за 10 юаней\n {3} рублей за 1 фунт'.format(
                                    get_course('R01235'),
                                    get_course('R01239'),
                                    get_course('R01375'),
                                    get_course('R01035')
                                )
                    vk.messages.send(user_id = user_id, random_id = random_id, message = responce)

                elif msg.startswith('-в'):
                    article = msg[3:]
                    responce = get_wiki_article(article)[:500]

                else:
                    responce = 'Неизвестная команда'

                vk.messages.send(user_id=user_id, random_id=random_id, message=responce)
    except(ReadTimeout, ProxyError):
        pass