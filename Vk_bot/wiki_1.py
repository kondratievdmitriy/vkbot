import  wikipedia

def get_wiki_article(article):
    wikipedia.set_lang('ru')

    try:
        return f'{wikipedia.summary(article)} {wikipedia.page(article).links}'

    except wikipedia.WikipediaException:
        return 'Не удалось найти информацию по данному вопросу'