# coding: utf-8

from social_core.backends.oauth import BaseOAuth2


class SuapOAuth2(BaseOAuth2):
    name = 'suap'
    AUTHORIZATION_URL = 'https://suap.ifrn.edu.br/o/authorize/'
    ACCESS_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_URL = 'https://suap.ifrn.edu.br/o/token/'
    ID_KEY = 'matricula'
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    EXTRA_DATA = [
        ('cpf','cpf'),
        ('data_nascimento','data_nascimento'),
        ('vinculo', 'vinculo'),
        ('url_foto_75x100','url_foto_75x100'),
        ('url_foto_150x200', 'url_foto_150x200'),
    ]
    USER_DATA_URL = 'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/'
    

    def user_data(self, access_token, *args, **kwargs):
        return self.request(
            url=self.USER_DATA_URL,
            data={'scope': kwargs['response']['scope']},
            method='GET',
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        ).json()

    def get_user_details(self, response):
        """
        Retorna um dicionário mapeando os fields do settings.AUTH_USER_MODEL.
        você pode fazer aqui outras coisas, como salvar os dados do usuário
        (`response`) em algum outro model.
        """
        splitted_name = response['nome_usual'].split()
        first_name, last_name = splitted_name[0], ''
        if len(splitted_name) > 1:
            last_name = splitted_name[-1]

        return {
            'username': response[ self.ID_KEY],
            'first_name': response['cpf'],
            'last_name': last_name.strip(),
            'email': response['email'],
        }
