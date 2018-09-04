def normaliza(vetor):
    ###Implementação
    return vetor_normal

def projeta_vetor(vetor_base, vetor):
    ###Implementação
    #(<v^t,vb>)*vb
    return vetor_projetado

def perpendicular(vetor_base, vetor_qualquer):
    vetor_projetado=projeta_vetor(vetor_base, vetor_qualquer)
    vetor_perpendicular=vetor_qualquer-vetor_projetado
    return vetor_perpendicular

def gramschimidt(vetor_base, vetor_qualquer):
    vetor_base_normal=normaliza(vetor_base)
    vetor_perpendicular=perpendicular(vetor_base_normal, vetor_qualquer)
    #seria interessante guardar todas essas bases?
    #continue seu raciocínio a partir daqui
    return vetor_perpendicular

if __name__ == '__main__':
    #inicie seu código aqui !!!!
    #use o quebra cabeça, pense depois na implementação de cada função
