from socket import send_fds


def enviar_email_confirmacao(adocao):

    assunto = "Adoção realizada com suceso"
    conteudo = f"Parabéns por realizar a adoção do pet {adocao.pet.nome} com o valor mensal de {adocao.valor}"
    remetente = "pythonlonan@gmail.com"
    destinatario = [adocao.email]
    send_mail = (assunto, conteudo, remetente, destinatario)
