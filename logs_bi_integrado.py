# coding: utf-8
import os
from datetime import datetime, timedelta
from humanize import naturaltime, i18n
from config_log import logger


i18n.activate("pt_BR")

DIR = '/mnt/t/SEPOC/ProjetoQlikView/0-Origem/BASES_GCT/'
ARQUIVOS = [
    'Valores Gerais.qvd',
    'Valores x Empenhos.qvd',
    'BD_DH_NF.qvd',
    'PF_MES.qvd',
    'GCT_Pago_SRestos.qvd',
    'GCT_Liquidado_CompDH.qvd',
    'GCT_Liquidado_CompDHNE.qvd',
    'GCT_Cota_Programada_em_Sol.qvd',
    'GCT_Cota_Programada.qvd',
    'PLF_SolicProgFin_PT.qvd',
    'GCT_Prog_Financeira_em_Sol.qvd',
    'GCT_Prog_Financeira.qvd',
    'GCT_ProvCrédito.qvd',
    'GCT_MovAltOrçamentoEmSol.qvd',
    'GCT_Despesa_Regularizar.qvd',
    'GCT_DisponibilidadeFnt.qvd',
    'GCT_Bloqueio_Dotação.qvd',
    'GCT_Dotação_Inicial.qvd',
    'GCT_Cota_a_Programar.qvd',
    'GCT_Empenhado_com_Cronograma.qvd',
    'GCT_Empenhado.qvd',
    'GCT_RPP_Insc_Saldo.qvd',
    'GCT_ReceitaOrçada_a_partir_2019.qvd',
    'GCT_DotaçãoAutorizada.qvd',
    'GCT_ReceitaRealizada_a_partir_2019.qvd',
    'GCT_Liquidado.qvd',
    'GCT_RPP_Canc.qvd',
    'GCT_Pago_CRestos.qvd',
    'Liquidacao_2024.csv',
    'Liquidacao_2023.rar',
    'Liquidacao_2022.rar',
    'Liquidacao_2021.rar',
    'Liquidacao_2020.rar',
    'Liquidacao_2019.rar',
    'GCT_Receita_Realizada_Mapeada.qvd',
    'GCT_Liquidado_Mapeamento.qvd',
    'GCT_DotaçãoAutorizadaIndicadorExercicio.qvd',
    'GCT_CredObjDetFonte.qvd',
    'SEPLAG - empenhos.xls',
    'SEPLAG - geral.xls',
    'Cenarios Fiscais Resumido2.qvw',
    'PD.qvw'
 ]


data_referencia = datetime.now() - timedelta(days=1)

for arquivo in ARQUIVOS:
    isodt = os.path.getmtime(DIR + '/' + arquivo)
    data_modificacao_arquivo = datetime.fromtimestamp(isodt)
    tempo_modificacao = naturaltime(data_modificacao_arquivo)

    texto_log = f'{arquivo} foi gerado a {tempo_modificacao}'
    if data_referencia > data_modificacao_arquivo:
        logger.warning(texto_log)
    else:
        logger.info(texto_log)
        
    
