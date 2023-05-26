import wikipediaapi

def get_wiki_page(text:str):
    wiki = wikipediaapi.Wikipedia('ru')
    result = wiki.page(text)
    return result.summary