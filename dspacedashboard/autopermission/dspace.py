import os
import requests
import subprocess

from decouple import config

from django.conf import settings

#DEPRECATED: Uso da API do próprio DSpace. Remoção futura
def update_dspace_user_old(netid, extra_params=[]):
    dspace_cli = os.path.join(config('DSPACE_PATH'), 'bin/dspace')
    res = subprocess.check_output([dspace_cli, "user", "--modify", "-n", netid] + extra_params)
    return res

def update_dspace_user(netid, group_uuid):
    base_url = settings.DSPACE_EXTERNAL_API_URL

    session = requests.Session()

    # 1. Obter token CSRF
    status = session.get(f"{base_url}/authn/status")
    csrf_token = status.headers.get("DSPACE-XSRF-TOKEN")

    # 2. Login
    login = session.post(
        f"{base_url}/authn/login",
        data={"user": settings.DSPACE_IMPORT_USER_MAIL, "password": settings.DSPACE_IMPORT_USER_PASS},
        headers={"X-XSRF-TOKEN": csrf_token},
    )
    csrf_token = login.headers.get("DSPACE-XSRF-TOKEN", csrf_token)
    token = login.headers.get("Authorization", "").replace("Bearer ", "")

    # 3. Buscar EPerson pelo netid
    eperson = session.get(
        f"{base_url}/eperson/epersons/search/byEmail",
        params={"email": f"{netid}@ufrn.edu.br"},
        headers={"Authorization": f"Bearer {token}"},
    )
    eperson_uuid = eperson.json()["id"]

    # 4. Adicionar ao grupo
    session.post(
        f"{base_url}/eperson/groups/{group_uuid}/epersons",
        data=f"{base_url}/eperson/epersons/{eperson_uuid}",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "text/uri-list",
            "X-XSRF-TOKEN": csrf_token,
        },
    )
    print(f"Usuário {netid} adicionado ao grupo {group_uuid}")
