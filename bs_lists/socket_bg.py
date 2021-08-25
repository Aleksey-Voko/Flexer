"""База гнёзд БГ"""

import pandas as pd


# Многокорневые слова БГ.csv
def save_multi_root_words(_, socket_group_list):
    """
    Найти в БГ строки с многокорневыми словами, т.е. словами, у которых есть
    корневой индекс (кроме невидимок).

    Создать документ Многокорневые слова БГ.csv и заполнить его строками
    с найденными многокорневыми словами с соблюдением следующих правил:
        1. строки приводятся полностью;
        2. строки вставляются в тот или иной столбец в зависимости
            от корневого индекса;
        3. уже вставленная строка не должна вставляться второй (и более!) раз!
            Другими словами, в документе Многокорневые слова БГ.csv не должно
            быть повторов одинаковых строк (напр. строка:
                автобус 3* .СеИ неод мI1 мнII1 * auto(mobile) (omni)bus
            вставляется 1 раз несмотря на то, что в базе она
            встречается 2 раза, или напр. строка:
                ЮНЕСКО 6
            вставляется 1 раз несмотря на то, что в базе
            она встречается 6 раз).

    По завершении заполнения документа Многокорневые слова БГ.csv
    вставленные строки в столбцах расположить в соответствии
    с алфавитным порядком слов,
    а сами столбцы - в следующем порядке:
    2 2! 2* 3 3! 3* 3** 4 4! 4* 4** 5 5! 5* 5** 6 6! 6* 6** 7 7! 7* 7**
    """
    root_index_ds = {
        '2': [],
        '2!': [],
        '2*': [],
        '3': [],
        '3!': [],
        '3*': [],
        '3**': [],
        '4': [],
        '4!': [],
        '4*': [],
        '4**': [],
        '5': [],
        '5!': [],
        '5*': [],
        '5**': [],
        '6': [],
        '6!': [],
        '6*': [],
        '6**': [],
        '7': [],
        '7!': [],
        '7*': [],
        '7**': [],
    }

    for socket_group in socket_group_list:
        for socket_word_form in socket_group.socket_word_forms:
            root_index = socket_word_form.root_index
            if root_index and not socket_word_form.invisible:
                root_index_ds[root_index].append(str(socket_word_form))

    for k in root_index_ds:
        root_index_ds[k] = sorted(list(
            set(root_index_ds[k])),
            key=lambda x: x.replace('*', '').lower().strip()
        )

    ds = []
    for k in root_index_ds:
        for word_form in root_index_ds[k]:
            ds.append({
                'root_index': k,
                'word_form': word_form,
            })

    df = pd.DataFrame(ds)
    res_df = (df
              .assign(idx=df.groupby("root_index").cumcount())
              .pivot_table(index="idx", columns="root_index",
                           values="word_form", aggfunc="first"))
    res_df.to_csv('Многокорневые слова БГ.csv', sep=';', encoding='cp1251')
