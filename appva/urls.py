from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('index/', views.index, name='index'),

    path('', views.logar, name='login'),
    path('/deslogar', views.deslogar, name='deslogar'),

    path('usuario_novo/', views.usuario_novo, name="usuario_novo"),
    path('usuario_listar/', views.usuario_listar, name='usuario_listar'),
    path('usuario_novo/', views.usuario_novo, name='usuario_novo'),
    path('usuario_editar/<int:pk>', views.usuario_editar, name='usuario_editar'),
    path('usuario_remover/<int:pk>', views.usuario_remover, name='usuario_remover'),

    path('remessas_novo/', views.remessas_novo, name='remessas_novo'),
    path('tabela_listagem/', views.tabela_listagem, name='tabela_listagem'),
    path('remessas_remover/<int:pk>', views.remessas_remover, name='remessas_remover'),
    path('REMESSAS_APAGAR_EFD_418/', views.REMESSAS_APAGAR_EFD_418, name='REMESSAS_APAGAR_EFD_418'),
    path('REMESSAS_APAGAR_GIA_296/', views.REMESSAS_APAGAR_GIA_296, name='REMESSAS_APAGAR_GIA_296'),


    path('GIA_OMISSO/', views.GIA_OMISSO, name='GIA_OMISSO'),
    path('import_gia_omisso/<int:pk>', views.import_gia_omisso, name='import_gia_omisso'),

    path('CCI/', views.CCI, name='CCI'),
    path('import_cci/<int:pk>', views.import_cci, name='import_cci'),

    path('IE/', views.IE, name='IE'),
    path('import_ie/<int:pk>', views.import_ie, name='import_ie'),

    path('NFE_EFD/', views.NFE_EFD, name='NFE_EFD'),
    path('import_nfe_efd/<int:pk>', views.import_nfe_efd, name='import_nfe_efd'),

    path('REG_1400_EFD/', views.REG_1400_EFD, name='REG_1400_EFD'),
    path('import_reg_1400_efd/<int:pk>', views.import_reg_1400_efd, name='import_reg_1400_efd'),

    path('CAP/', views.CAP, name='CAP'),
    path('import_cap/<int:pk>', views.import_cap, name='import_cap'),

    path('GIA_COP3/', views.GIA_COP3, name='GIA_COP3'),
    path('import_gia_cop3/<int:pk>', views.import_gia_cop3, name='import_gia_cop3'),

    path('GIA_ENTRADAS_SAIDAS/', views.GIA_ENTRADAS_SAIDAS, name='GIA_ENTRADAS_SAIDAS'),
    path('import_gia_entradas_saidas/<int:pk>', views.import_gia_entradas_saidas, name='import_gia_entradas_saidas'),
    path('GIA_ENTRADAS_SAIDAS_lista_valor_adicionado/', views.GIA_ENTRADAS_SAIDAS_lista_valor_adicionado, name='GIA_ENTRADAS_SAIDAS_lista_valor_adicionado'),
    path('VALOR_ADICIONADO_gia_296/<str:inscricao>', views.VALOR_ADICIONADO_gia_296, name='VALOR_ADICIONADO_gia_296'),
    path('VALOR_ADICIONADO_gia_296_POR_MUNICIPIO/<str:municipio>', views.VALOR_ADICIONADO_gia_296_POR_MUNICIPIO, name='VALOR_ADICIONADO_gia_296_POR_MUNICIPIO'),

    path('NFE_e/', views.NFE_e, name='NFE_e'),
    path('import_nfe_e/<int:pk>', views.import_nfe_e, name='import_nfe_e'),

    path('ACYPR535/', views.ACYPR535, name='ACYPR535'),
    path('import_acypr535/<int:pk>', views.import_acypr535, name='import_acypr535'),

    path('ACYPR540/', views.ACYPR540, name='ACYPR540'),
    path('import_acypr540/<int:pk>', views.import_acypr540, name='import_acypr540'),

    path('ACYPR555/', views.ACYPR555, name='ACYPR555'),
    path('import_acypr555/<int:pk>', views.import_acypr555, name='import_acypr555'),

    path('ACYPR556/', views.ACYPR556, name='ACYPR556'),
    path('import_acypr556/<int:pk>', views.import_acypr556, name='import_acypr556'),

    path('ACYPR557/', views.ACYPR557, name='ACYPR557'),
    path('import_acypr557/<int:pk>', views.import_acypr557, name='import_acypr557'),

    path('ACYPR600/', views.ACYPR600, name='ACYPR600'),
    path('import_acypr600/<int:pk>', views.import_acypr600, name='import_acypr600'),

    path('CRED/', views.CRED, name='CRED'),
    path('import_cred/<int:pk>', views.import_cred, name='import_cred'),

    path('CNAE/', views.CNAE, name='CNAE'),
    path('import_cnae/<int:pk>', views.import_cnae, name='import_cnae'),

    path('DEB/', views.DEB, name='DEB'),
    path('import_deb/<int:pk>', views.import_deb, name='import_deb'),

    path('FPM/', views.FPM, name='FPM'),
    path('import_fpm/<int:pk>', views.import_fpm, name='import_fpm'),

    path('GIA_SEM_MOV/', views.GIA_SEM_MOV, name='GIA_SEM_MOV'),
    path('import_gia_sem_mov/<int:pk>', views.import_gia_sem_mov, name='import_gia_sem_mov'),

    path('EFD/', views.EFD, name='EFD'),
    path('import_efd/<int:pk>', views.import_efd, name='import_efd'),
    path('EFD_lista_valor_adicionado/', views.EFD_lista_valor_adicionado, name='EFD_lista_valor_adicionado'),
    path('VALOR_ADICIONADO_efd_418/<str:inscricao>', views.VALOR_ADICIONADO_efd_418, name='VALOR_ADICIONADO_efd_418'),
    path('VALOR_ADICIONADO_efd_418_POR_MUNICIPIO/<str:municipio>', views.VALOR_ADICIONADO_efd_418_POR_MUNICIPIO, name='VALOR_ADICIONADO_efd_418_POR_MUNICIPIO'),

    path('EFD_OMISSO/', views.EFD_OMISSO, name='EFD_OMISSO'),
    path('import_efd_omisso/<int:pk>', views.import_efd_omisso, name='import_efd_omisso'),

    path('EFD_SEM_MOV/', views.EFD_SEM_MOV, name='EFD_SEM_MOV'),
    path('import_efd_sem_mov/<int:pk>', views.import_efd_sem_mov, name='import_efd_sem_mov'),

    path('ACGPT812/', views.ACGPT812, name='ACGPT812'),
    path('import_acgpt812/<int:pk>', views.import_acgpt812, name='import_acgpt812'),

    path('PGDAS_D/', views.PGDAS_D, name='PGDAS_D'),
    path('import_pgdas_d/<int:pk>', views.import_pgdas_d, name='import_pgdas_d'),

    path('ACGPR051/', views.ACGPR051, name='ACGPR051'),
    path('import_acgpr051/<int:pk>', views.import_acgpr051, name='import_acgpr051'),

    path('CFOP/', views.CFOP, name='CFOP'),
    path('import_cfop/<int:pk>', views.import_cfop, name='import_cfop'),

]
