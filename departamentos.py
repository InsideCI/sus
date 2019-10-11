import requests
from bs4 import BeautifulSoup as soup


def departamentos():
    """
    departamentos retorna todos os departamentos de ensino da ufpb e seus 
    respectivos id's.
    """

    params = (
        ('aba', 'p-academico'),
    )

    response = requests.get(
        'https://sigaa.ufpb.br/sigaa/public/centro/lista.jsf', params=params)

    page_soup = soup(response.content, "lxml")

    centros = page_soup.find_all("table", {"class": "listagem"})

    departamentos = []

    for centro in centros:
        try:
            # capturando o id do centro
            ctr = centro.find("a", {"class", "iconeCentro"})
            ctr = ctr['href'][-4:]
            # print(ctr)
        except:
            ctr = ''

        dpts = centro.find_all("a", {"class": "nomeDepartamento"})
        for dpt in dpts:
            dpt_id = dpt['href'][-4:]  # id do departamento
            if dpt.text.strip() != '':  # ignorando o código mal feito do sigaa
                if ctr != '':
                    # departamentos.append([dpt_id, dpt.text.strip(), ctr])
                    dp = {
                        "id": int(dpt_id),
                        "nome": dpt.text.strip(),
                        "id_centro": int(ctr)
                    }
                    departamentos.append(dp)
                    print(dp)
                else:
                    dp = {
                        "id": int(dpt_id),
                        "nome": dpt.text.strip(),
                        "id_centro": ""
                    }
                    departamentos.append(dp)

    return departamentos


# departamentos()
