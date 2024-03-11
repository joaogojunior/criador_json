from json import loads, dumps
from os import path


def escreve_json_padrao(arquivo, json_padrao):
    with (open(arquivo, "w") as config):
        # salva json
        config.write(json_padrao)


# carrega valores padroes, cria arquivo de configuração caso nao exista
def carrega_ou_cria_config(arquivo, valores_padroes):
    if isinstance(valores_padroes, dict):
        # trata como dicionario e format json
        retorno = valores_padroes
        json_padrao = dumps(valores_padroes, indent=3)
    else:
        # trata como json e formata json
        retorno = loads(valores_padroes)
        json_padrao = dumps(retorno, indent=3)
    # obtem versao do json padrao (se existir)
    try:
        json_ver_padrao = retorno['json_ver']
    except KeyError:
        json_ver_padrao = -1
    # testa se o arquivo de configuração existe
    if not path.isfile(arquivo):
        # se nao existir cria um com os defaults
        print("Arquivo de configuração %s não encontrado, criando um com padrões..." % arquivo)
        escreve_json_padrao(arquivo, json_padrao)
        return retorno
    else:
        # carrega config do arquivo
        dict_arquivo = carrega_config(arquivo)
        # checa se o arquivo tem precedência
        try:
            # se o arquivo tiver uma versão mais nova ou igual
            if dict_arquivo['json_ver'] >= json_ver_padrao:
                # retorna ele
                return dict_arquivo
            else:
                # se tiver versão mais baixa entao atualiza com padroes novos
                backup_json(arquivo, json_padrao)
                # e retorna o json padrao
                return retorno
        except KeyError:
            if json_ver_padrao > -1:
                # como o json padrao tem uma versao e o arquivo nao tem retorna ele
                # e faz backup do arquivo
                backup_json(arquivo, json_padrao)
                return retorno
            else:
                # o json padrao e o json do arquivo nao tem versao mostra mensagem avisando e retorna
                # o json do arquivo
                print("Como ambos arquivos não tem versão (chave 'json_ver' ausente) retornando o json do arquivo...")
                return dict_arquivo


def backup_json(arquivo, json_padrao):
    # faz backup
    with open(arquivo, "r") as entrada:
        # rescreve backup antigo se existir
        with open(arquivo + "_backup", "w") as saida:
            saida.write(entrada.read())
    print("Configuração está sendo atualizada, a configuração antiga foi salva como %s." % arquivo + "_backup")
    escreve_json_padrao(arquivo, json_padrao)


def carrega_config(arquivo):
    # carrega o arquivo de configuracao
    print("Carregando configurações de", arquivo + "...")
    with open(arquivo, "r") as config:
        return loads(config.read().strip())
