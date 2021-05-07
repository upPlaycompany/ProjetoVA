from django.db import models


# Create your models here.

# RELAÇÃO DOS ÍNDICES APURADOS

class Acypr535(models.Model):
    municipio = models.CharField(max_length=255, null=True)
    iva_ant = models.FloatField(null=True)
    iva_atual = models.FloatField(null=True)
    iva_med = models.FloatField(null=True)
    iva_75 = models.FloatField(null=True)
    ucti = models.FloatField(null=True)
    trib_propr = models.FloatField(null=True)
    populacao = models.FloatField(null=True)
    area = models.FloatField(null=True)
    coef_soc = models.FloatField(null=True)
    ind_final = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# RELAÇÃO DAS VARIAÇÕES DOS INDICES
class Acypr540(models.Model):
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    ipm_ano_base = models.FloatField(null=True)
    ipm_ano_exercicio = models.FloatField(null=True)
    porcentagem = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# VALORES ADICIONADOS POR CONTRIBUINTE POSITIVO
class Acypr555(models.Model):
    tipo_contrib = models.CharField(max_length=255, null=True)
    cod = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    cnae = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    vr_adicionado = models.FloatField(null=True)
    entradas = models.FloatField(null=True)
    saidas = models.FloatField(null=True)
    st_entradas = models.FloatField(null=True)
    st_saidas = models.FloatField(null=True)
    ipi_entradas = models.FloatField(null=True)
    ipi_saidas = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# VALORES  UTILIZADOS PARA CÁLCULOS DE INDICE
class Acypr556(models.Model):
    codigo = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    vr_adic_ano_base = models.FloatField(null=True)
    vr_adic_ano_exercicio = models.FloatField(null=True)
    receita_propria = models.FloatField(null=True)
    populacao = models.FloatField(null=True)
    area = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# VALORES ADICIONADOS POR CONTRIBUINTE NEGATIVOS E NULOS
class Acypr557(models.Model):
    tipo_contrib = models.CharField(max_length=255, null=True)
    cod = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    cnae = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    vr_adicionado = models.FloatField(null=True)
    entradas = models.FloatField(null=True)
    saidas = models.FloatField(null=True)
    st_entradas = models.FloatField(null=True)
    st_saidas = models.FloatField(null=True)
    ipi_entradas = models.FloatField(null=True)
    ipi_saidas = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# RELATORIO DE VALORES ADICIONADOS
class Acypr600(models.Model):
    municipio = models.CharField(max_length=255, null=True)
    com_ind = models.FloatField(null=True)
    prod_rural = models.FloatField(null=True)
    prest_serv = models.FloatField(null=True)
    dar_1_aut = models.FloatField(null=True)
    nai = models.FloatField(null=True)
    credito_ex_off = models.FloatField(null=True)
    debito_ex_off = models.FloatField(null=True)
    total = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# Catálogo alfábetico de contribuintes(CAP)
class Cap(models.Model):
    numr_inscricao_estadual = models.CharField(max_length=255, null=True)
    nome_pessoa = models.CharField(max_length=255, null=True)
    nome_inscrito = models.CharField(max_length=255, null=True)
    numr_documento = models.CharField(max_length=255, null=True)
    desc_documento = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    tipo_inscrito = models.CharField(max_length=255, null=True)
    tipo_produtor = models.CharField(max_length=255, null=True)
    codg_cnae = models.CharField(max_length=255, null=True)
    desc_cnae = models.CharField(max_length=255, null=True)
    desc_segmento = models.CharField(max_length=255, null=True)
    codg_municipio = models.CharField(max_length=255, null=True)
    nome_municipio = models.CharField(max_length=255, null=True)
    tipo_logradouro_contribuinte = models.CharField(max_length=255, null=True)
    nome_logradouro_contribuinte = models.CharField(max_length=255, null=True)
    numr_logradouro_contribuinte = models.CharField(max_length=255, null=True)
    complemento_contribuinte = models.CharField(max_length=255, null=True)
    bairro_contribuinte = models.CharField(max_length=255, null=True)
    ddd_telefone_contribuinte = models.CharField(max_length=255, null=True)
    telefone_contribuinte = models.CharField(max_length=255, null=True)
    ddd_celular_contribuinte = models.CharField(max_length=255, null=True)
    celular_contribuinte = models.CharField(max_length=255, null=True)
    email_contribuinte = models.CharField(max_length=255, null=True)
    codg_crc = models.CharField(max_length=255, null=True)
    nome_contabilista = models.CharField(max_length=255, null=True)
    municipio_contabilista = models.CharField(max_length=255, null=True)
    tipo_logradouro_contabilista = models.CharField(max_length=255, null=True)
    nome_logradouro_contabilista = models.CharField(max_length=255, null=True)
    numr_logradouro_contabilista = models.CharField(max_length=255, null=True)
    complemento_contabilista = models.CharField(max_length=255, null=True)
    bairro_contabilista = models.CharField(max_length=255, null=True)
    ddd_telefone_contabilista = models.CharField(max_length=255, null=True)
    telefone_contabilista = models.CharField(max_length=255, null=True)
    ddd_celular_contabilista = models.CharField(max_length=255, null=True)
    celular_contabilista = models.CharField(max_length=255, null=True)
    email_contabilista = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# Catálogo alfabético de contribuintes(CCI)
class Cci(models.Model):
    numr_inscricao_estadual = models.CharField(max_length=255, null=True)
    nome_pessoa = models.CharField(max_length=255, null=True)
    nome_inscrito = models.CharField(max_length=255, null=True)
    numr_documento = models.CharField(max_length=255, null=True)
    desc_documento = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    tipo_inscrito = models.CharField(max_length=255, null=True)
    simples_nacional = models.CharField(max_length=255, null=True)
    flag_mei = models.CharField(max_length=255, null=True)
    data_inicio_atividade_sefaz = models.CharField(max_length=255, null=True)
    codg_cnae = models.CharField(max_length=255, null=True)
    desc_cnae = models.CharField(max_length=255, null=True)
    desc_segmento = models.CharField(max_length=255, null=True)
    codg_municipio = models.CharField(max_length=255, null=True)
    nome_municipio = models.CharField(max_length=255, null=True)
    tipo_logradouro_contribuinte = models.CharField(max_length=255, null=True)
    nome_logradouro_contribuinte = models.CharField(max_length=255, null=True)
    numr_logradouro_contribuinte = models.CharField(max_length=255, null=True)
    complemento_contribuinte = models.CharField(max_length=255, null=True)
    bairro_contribuinte = models.CharField(max_length=255, null=True)
    ddd_telefone_contribuinte = models.CharField(max_length=255, null=True)
    telefone_contribuinte = models.CharField(max_length=255, null=True)
    ddd_celular_contribuinte = models.CharField(max_length=255, null=True)
    celular_contribuinte = models.CharField(max_length=255, null=True)
    email_contribuinte = models.CharField(max_length=255, null=True)
    codg_crc = models.CharField(max_length=255, null=True)
    nome_contabilista = models.CharField(max_length=255, null=True)
    municipio_contabilista = models.CharField(max_length=255, null=True)
    tipo_logradouro_contabilista = models.CharField(max_length=255, null=True)
    nome_logradouro_contabilista = models.CharField(max_length=255, null=True)
    numr_logradouro_contabilista = models.CharField(max_length=255, null=True)
    complemento_contabilista = models.CharField(max_length=255, null=True)
    bairro_contabilista = models.CharField(max_length=255, null=True)
    ddd_telefone_contabilista = models.CharField(max_length=255, null=True)
    telefone_contabilista = models.CharField(max_length=255, null=True)
    ddd_celular_contabilista = models.CharField(max_length=255, null=True)
    celular_contabilista = models.CharField(max_length=255, null=True)
    email_contabilista = models.CharField(max_length=255, null=True)
    porte_empresa = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# Relatório de notas ficais de estradas eletrônicas EXPORTAÇÃO #ARQUIVO INPOSSIVEL DE IMPORTAR
class Acgpr051(models.Model):
    inscricao = models.CharField(max_length=255, null=True)
    razao_social = models.CharField(max_length=255, null=True)
    numero_nf = models.CharField(max_length=255, null=True)
    data = models.CharField(max_length=255, null=True)
    cfop = models.CharField(max_length=255, null=True)
    valor = models.CharField(max_length=255, null=True)
    cod_mun = models.CharField(max_length=255, null=True)


# CREDITO
class Cred(models.Model):
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    a_creditar = models.CharField(max_length=255, null=True)
    especificacao = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# CÓDIGO FISCAL DE OPERAÇÕES
class Cfop(models.Model):
    codigo = models.CharField(max_length=255, null=True)
    descricao = models.CharField(max_length=255, null=True)
    aplicacao = models.CharField(max_length=255, null=True)
    inicio_vigencia = models.CharField(max_length=255, null=True)
    fim_vigencia = models.CharField(max_length=255, null=True)
    tipo = models.CharField(max_length=10, null=True)
    valido = models.CharField(max_length=3, null=True)
    portaria = models.CharField(max_length=255, null=True)


# CODIGO NACIONAL DE ATIVIDADES ECONÔMICAS
class Cnae(models.Model):
    secao = models.CharField(max_length=255, null=True)
    divisao = models.CharField(max_length=100, null=True)
    grupo = models.CharField(max_length=100, null=True)
    classe = models.CharField(max_length=100, null=True)
    subclasse = models.CharField(max_length=100, null=True)
    denominacao = models.CharField(max_length=255, null=True)
    arbitramento = models.CharField(max_length=255, null=True)


# DEBITO
class Deb(models.Model):
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    a_debitar = models.CharField(max_length=255, null=True)
    especificacao = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# REG 14000 EFD REGISTROS VALROES PRESTADOS POR MUNICIPIO
class Reg_1400_efd(models.Model):
    inscricao = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    dt_inicial = models.CharField(max_length=255, null=True)
    dt_final = models.CharField(max_length=255, null=True)
    codg = models.CharField(max_length=255, null=True)
    municipio_reg_1400 = models.CharField(max_length=255, null=True)
    vr_reg_1400 = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# ESCRITURACAO FISCAL DIGITAL
class Efd(models.Model):
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    cad = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    cnae = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    dt_inicial = models.CharField(max_length=255, null=True)
    dt_final = models.CharField(max_length=255, null=True)
    cfop = models.CharField(max_length=255, null=True)
    vr_contabil = models.FloatField(null=True)
    ipi = models.FloatField(null=True)
    icms_st = models.FloatField(null=True)
    crc = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# SEM MOVIMENTO
class Efd_sem_mov(models.Model):
    num_efd = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    cpf_cnpj = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    mes = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)

# OMISSO
class Efd_omisso(models.Model):
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    mes = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# FUNDO DE PARTICIPAÇÃO DOS MUNICÍPIOS
# FAZER CLASSE FPM
class Fpm(models.Model):
    ano = models.CharField(max_length=255, null=True)
    janeiro = models.FloatField(null=True)
    fevereiro = models.FloatField(null=True)
    marco = models.FloatField(null=True)
    abril = models.FloatField(null=True)
    maio = models.FloatField(null=True)
    junho = models.FloatField(null=True)
    julho = models.FloatField(null=True)
    agosto = models.FloatField(null=True)
    setembro = models.FloatField(null=True)
    outubro = models.FloatField(null=True)
    novembro = models.FloatField(null=True)
    dezembro = models.FloatField(null=True)
    total = models.FloatField(null=True)
    variacao = models.FloatField(null=True)

# COP3 MENSAL: GIA-ICMS
class Gia_cop3(models.Model):
    inscricao = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    ano_base = models.CharField(max_length=255, null=True)
    cop = models.CharField(max_length=255, null=True)
    sit = models.CharField(max_length=255, null=True)
    mes = models.CharField(max_length=255, null=True)
    tipo = models.CharField(max_length=255, null=True)
    codg = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    vr_cop3 = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)


# DHRPR296 REGISTROS GIA POR CFOP
class Gia_entradas_saidas(models.Model):
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    cad = models.CharField(max_length=255, null=True)
    cnae = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    dt_inicial = models.CharField(max_length=255, null=True)
    dt_final = models.CharField(max_length=255, null=True)
    tipo = models.CharField(max_length=255, null=True)
    dt_process = models.CharField(max_length=255, null=True)
    cfop = models.CharField(max_length=255, null=True)
    vr_contabil = models.FloatField(null=True)
    crc = models.CharField(max_length=255, null=True)
    ie_anterior = models.CharField(max_length=255, null=True)
    base_calculo = models.CharField(max_length=255, null=True)
    icms = models.CharField(max_length=255, null=True)
    isentas = models.CharField(max_length=255, null=True)
    outras = models.CharField(max_length=255, null=True)
    ipi = models.FloatField(null=True)
    icms_st = models.FloatField(null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)




# DHRPR278: GIA-ICMS RELATORIO DE OMISSOS NA GIA-ICMS POR MUNICIPIOS E CONTABILISTAS
class Gia_omisso(models.Model):
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    cnae = models.CharField(max_length=255, null=True)
    cad = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    mes = models.CharField(max_length=255, null=True)
    periodicidade = models.CharField(max_length=255, null=True)
    crc = models.CharField(max_length=255, null=True)
    contabilista = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# DHRPR098 GIA-ICMS DECLARADAS SEM MOVIMENTO(ENTRADAS E SAIDAS ZERADAS)
class Gia_sem_mov(models.Model):
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    ano_base = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    cad = models.CharField(max_length=255, null=True)
    sit_gia = models.CharField(max_length=255, null=True)
    inf_mov = models.CharField(max_length=255, null=True)
    mes_inicial = models.CharField(max_length=255, null=True)
    mes_final = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)



# IE SIMPLES NACIONAL
class Ie(models.Model):
    numr_inscricao_estadual = models.CharField(max_length=255)
    nome_pessoa = models.CharField(max_length=255, null=True)
    flag_mei = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# NOTAS FISCAIS DE PRODUTOR E AVULSA NFPA
class Acgpt812(models.Model):
    ie_remetente = models.CharField(max_length=255, null=True)
    ie_simplificada = models.CharField(max_length=255, null=True)
    nome_remetente = models.CharField(max_length=255, null=True)
    cod = models.CharField(max_length=255, null=True)
    mun_remetente = models.CharField(max_length=255, null=True)
    ie_destinatario = models.CharField(max_length=255, null=True)
    nome_destinatario = models.CharField(max_length=255, null=True)
    codg = models.CharField(max_length=255, null=True)
    mun_destinatario = models.CharField(max_length=255, null=True)
    nro_nfpa = models.CharField(max_length=255, null=True)
    emissao = models.CharField(max_length=255, null=True)
    cfop = models.CharField(max_length=255, null=True)
    vr_nfpa = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)



# Relatorio de notas fiscais de entradas eletronicas
class Nfe_e(models.Model):
    ie_remetente = models.CharField(max_length=255, null=True)
    nome_do_produtor = models.CharField(max_length=255, null=True)
    cod = models.CharField(max_length=255, null=True)
    municipio_do_produtor = models.CharField(max_length=255, null=True)
    ie_adquirente = models.CharField(max_length=255, null=True)
    nome_adquirente = models.CharField(max_length=255, null=True)
    mun_adquirente = models.CharField(max_length=255, null=True)
    n_nf_e = models.CharField(max_length=255, null=True)
    emissao_nf_e = models.CharField(max_length=255, null=True)
    cfop = models.CharField(max_length=255, null=True)
    vr_nf_e = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)



# RELATORIO DE NOTAS FISCAIS DE ENTRADA ELETRONICAS EFD
class Nfe_efd(models.Model):
    ie_remetente = models.CharField(max_length=255, null=True)
    nome_remetente = models.CharField(max_length=255, null=True)
    cod = models.CharField(max_length=255, null=True)
    municipio_remetente = models.CharField(max_length=255, null=True)
    ie_adquirente = models.CharField(max_length=255, null=True)
    nome_adquirente = models.CharField(max_length=255, null=True)
    codg = models.CharField(max_length=255, null=True)
    municipio_adquirente = models.CharField(max_length=255, null=True)
    nro_nf = models.CharField(max_length=255, null=True)
    tipo_doc = models.CharField(max_length=255, null=True)
    mod = models.CharField(max_length=255, null=True)
    emissao = models.CharField(max_length=255, null=True)
    cfop = models.CharField(max_length=255, null=True)
    valor_nf = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)


# RECEITA DOS CONTRIBUINTES SIMPLES NACIONAL
class Pgdas_d(models.Model):
    tipo = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(max_length=255, null=True)
    contribuinte = models.CharField(max_length=255, null=True)
    cnae = models.CharField(max_length=255, null=True)
    cod = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    mes = models.CharField(max_length=255, null=True)
    rb_total = models.FloatField(null=True)
    rb_outros = models.CharField(max_length=255, null=True)
    rb_icms = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    ano_exercicio = models.CharField(max_length=100, null=True)
    ano_base = models.CharField(max_length=100, null=True)

class PTS(models.Model):
    exercicio = models.CharField(max_length=255, null=True)
    inscricao = models.CharField(max_length=255, null=True)
    dtinicio = models.CharField(max_length=255, null=True)
    dtfinal = models.CharField(max_length=255, null=True)
    tipo = models.CharField(max_length=255, null=True)
    dtprocessam = models.CharField(max_length=255, null=True)
    cfop = models.CharField(max_length=255, null=True)
    vlcontabil = models.FloatField(null=True)
    basecalculo = models.FloatField(null=True)
    icms = models.FloatField(null=True)
    isentas = models.FloatField(null=True)
    outras = models.FloatField(null=True)
    ipi = models.FloatField(null=True)
    retido = models.FloatField(null=True)
    situacao = models.CharField(max_length=255, null=True)
    idatualizacao = models.CharField(max_length=255, null=True)
    codmunicipio = models.CharField(max_length=255, null=True)
    efd = models.CharField(max_length=255, null=True)
    remessa = models.CharField(max_length=255, null=True)
    descricao = models.CharField(max_length=255, null=True)
    ano_exercicio = models.CharField(max_length=255, null=True)
    ano_base = models.CharField(max_length=255, null=True)



class REMESSAS(models.Model):
    arquivo = models.FileField(upload_to='.')
    descricao_arquivo = models.CharField(max_length=255)
    tabela = models.CharField(max_length=255)
    ano_base = models.IntegerField(null=True)
    ano_exercicio = models.IntegerField(null=True)
    data_hora_importacao = models.DateTimeField(null=True)
