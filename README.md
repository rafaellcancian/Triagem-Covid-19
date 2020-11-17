# Triagem-Covid-19
Tarefa avaliativa: modelagem e implementação de sistema Python-Django

A partir dos sistemas construídos e discutidos em sala (sistema de empréstimo e sistema de gestão de atas), projetar e implementar um sistema online para funcionar em postos de saúde e auxiliar na triagem de pacientes com ou sem COVID19. A ideia da triagem é melhor a prioridade de atendimento do paciente.

O sistema deve permitir o login (logo o cadastro) de dois tipos de usuários: ADMINISTRADOR (com todas as permissões do sistema) e o ENFERMEIRO (com permissões de consultar usuários e gestão de triagem).

O sistema deve possuir, além dos apps obrigatórios de um sistema python-django, dois apps adicionais: usuario (para gestão de usuários) e triagem (para gestão dos atendimentos de triagem do COVID19).

O app usuário deve conter email (chave de controle), nome, fone celular, endereço residencial, tipo (ADMINISTRADOR ou ENFERMEIRO) e atributo de ativo.

O app triagem deve conter data, hora, nome completo do paciente, idade, altura, peso, IMC (índice de massa corpórea que deverá ser calculado e armazenado automaticamente), resultado da triagem. Na app, o usuário deverá poder cadastrar atendimento, listar atendimentos realizados em pacientes e pesquisar por atendimento.

O resultado da triagem é baseado no esquema da figura.
