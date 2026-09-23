from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_view), # deixar vazio significa que será reconhecido como a página inicial!
]











# MVT (MVC)

# www.vollmed.online
# www.vollmed.online/Login
# www.vollmed.online/

# medico
# www.vollmed.online/medico/id/ -> id do médico (1,2,3..)
# www.vollmed.online/medico/id/alterar -> alterar cadastro do médico
# www.vollmed.online/medico/id/consultas

# paciente
# www.vollmed.online/paciente/id -> perfil do paciente
# www.vollmed.online/paciente/id/alterar -> alterar cadastro do paciente

# www.vollmed.online/paciente/id/consultas/cadastrar/
# www.vollmed.online/paciente/id/consultas/id/ -> ver,alterar,deletar

# secretario 
# www.vollmed.online/secretario/id -> perfil do secretario
# www.vollmed.online/secretario/id/alterar -> alterar cadastro do secretario

# www.vollmed.online/secretario/id/consultas/cadastrar/
# www.vollmed.online/secretario/id/consultas/id/ -> ver,alterar,deletar


# consulta
# www.vollmed.online/consulta/