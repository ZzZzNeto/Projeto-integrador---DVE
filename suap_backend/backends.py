# coding: utf-8

from social_core.backends.oauth import BaseOAuth2
from Login.models import CustomUser, UserInternal
from django.contrib.auth.models import Group

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

        if UserInternal.objects.filter(registration=response[self.ID_KEY]).count() == 0:
            group = Group.objects.get(name="EstudanteIFRN")
            user = CustomUser.objects.create_user(name=response['nome_usual'],email=response['email'])
            user.set_unusable_password()
            user.username = user.email
            user.photo = response['url_foto_150x200']
            user.save()
            user.groups.add(group)
            print("skadajsbhdfd" , response['url_foto_150x200'])
            internal = UserInternal.objects.create(user=user)
            internal.registration = response[ self.ID_KEY]
            internal.course = response['vinculo']['curso']
            internal.birth_date = response['data_nascimento']
            internal.save()
        else: 
            pass

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
