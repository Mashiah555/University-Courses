# researcher(Name, FieldsList).
researcher = {
    'prof_levi': ['ai', 'nlp', 'data_science'],
    'dr_cohen': ['cyber_security', 'networks'],
    'prof_alon': ['algorithms', 'ai', 'graph_theory'],
    'dr_shapiro': ['databases', 'data_science'],
    'dr_maron': ['nlp', 'bioinformatics']
}

articles = [
    ('paper_01', ['prof_levi', 'dr_cohen'], 'ai'),
    ('paper_02', ['dr_cohen', 'prof_alon'], 'cyber_security'),
    ('paper_03', ['prof_levi', 'dr_maron'], 'nlp'),
    ('paper_04', ['dr_maron', 'prof_gordon'], 'nlp'),
    ('paper_05', ['prof_gordon', 'dr_shapiro'], 'cryptography'),
    ('paper_06', ['dr_shapiro', 'prof_alon'], 'databases'),
    ('paper_07', ['prof_alon', 'dr_maron'], 'graph_theory')
]

def get_articles_by_researcher(name):
    return list(map(lambda paper: paper[0], filter(lambda paper: name in paper[1], articles)))

def unqualified_articles(name, article_list, acc = 0):
    if not article_list or name not in researcher:
        return acc
    if article_list[0][0] in get_articles_by_researcher(name) and article_list[0][2] not in researcher[name]:
        return unqualified_articles(name, article_list[1:], acc + 1)
    return unqualified_articles(name, article_list[1:], acc)

def print_unqualified():
    print([r for r in researcher if unqualified_articles(r, articles) > 0])

# Run Examples:
print(get_articles_by_researcher('dr_cohen'))

print(unqualified_articles('dr_cohen', articles))
print(unqualified_articles('prof_levi', articles))

print_unqualified()