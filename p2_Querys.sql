-- OBSERVAÇÃO: COMO OCORRIDO DURANTE UMA DAS AULAS, O BANCO DE DADOS APRESENTOU A MENSAGEM
-- DE INCOMPATIBILIDADE COM O ONLY FULL GROUP BY MODE. DEVIDO A ISSO, PRECISEI UTILIZAR O COMANDO
-- ABAIXO PARA QUE A QUERY UTILIZANDO O HAVING STATEMENT FUNCIONASSE NORMALMENTE.

-- SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

-- inserindo os dados
use mecanica;

insert into Clientes (Nome, Sobrenome, RG, Telefone, Email, Endereço, Cidade, Estado)
values  ('Felipe', 'Rodrigues Fonseca', 12222222, '999887766','fel@email.com', 'Rua dos Nerds Nº2331 Bairro Hardicore', 'Uruguaiana', 'RS'),
		('Ricardo', 'Augusto Albertini', 33332222, '99888877', 'ricag@email.com', 'Rua Severina Nº11 Bairro Centro', 'São Paulo', 'SP'),
        ('Mariana', 'Larissa Alcantra', 222224444, '322233344', 'marialc@email.com', 'Rua Porto Seguro Nº36 Bairro De la Mancha', 'Niterói', 'RJ');


insert into Veiculos (Veiculo_idCliente, Placa, Modelo, Ano, Cor) 
values  (1, 'iii888', 'Fusca', 1990, 'Branco'),
		(2, 'JJk777', 'FordKA', 2012, 'Cinza'),
        (3, 'ss31112', 'Saveiro', 2018, 'Preto');


insert into Mecanicos (Nome, Sobrenome, RG, Endereço, Telefone, Estado)
values  ('Adalberto', 'Joazeiro Dionísio', 'RR1233355', 'R. Celenium Nº989 Bairro Centro', 3332224, 'MG'),
		('Edvanio', 'Carlos de Ambrósio', 'SS987756', 'R. Estiláquio N°4450 Bairro Zona Norte',3344565, 'MG'),
        ('Jeferson', 'Rodrigues Limeira', 'GG3333333', 'R. Pires da Cunha N°5660 Bairro Dal ponte', 33665555, 'MG');


insert into Serviços(idServiçoMecanico, Tipo_De_Serviço, Valor, Descrição)
values  (1, 'Reparo do Motor', 1100.0, 'Reparo Geral de motor fundido'),
		(2, 'Manutenção da Suspensão', 346.50, 'Troca geral de amortecedores'),
        (3, 'Troca de Óleo', 20.00, 'Troca de óleo do motor' );


insert into Ordem_de_Serviço(id_Ordem_de_Serviço_Serviço) 
values (2),
	   (3),
       (1);
       
insert into Atendimentos(idAtendimentoCliente, idAtendimentoVeículo, idAtendimentoOrdem_de_Serviço, valor_total)
values  (3, 3, 1, 346.50),
		(1, 1, 2, 20.0),
        (2, 2, 3, 1100.0);
        
        
insert into Notas_Fiscais(idNotaCliente, idNotaAtendimento, idNotaFiscal_OrdemServiço, Valor_Total, Data_de_Emissão)        
values  (1, 2, 2, 20.0, '2023-11-01'),
		(2, 3, 3, 1100.0, '2023-10-14'),
        (3, 1, 1, 346.50, '2023-11-04');
  
  
  
 -- Visualizando os dados e querys simples com select statment
 
select * from Clientes;
select * from Veiculos;
select * from Mecanicos;
select * from Serviços;
select * from Ordem_de_Serviço order by id_Ordem_de_Serviço asc;
select * from Atendimentos;              
select * from Notas_Fiscais;       


-- Realizando querys e elaborando Perguntas

-- Houve algum atendimento cujo o valor total foi maior do que R$1000,00? 

select concat (Nome,' ',Sobrenome) as Cliente, Telefone, valor_total as 'Valor total do Atendimento R$'
from Clientes c
inner join Atendimentos a
on c.idCliente = a.idAtendimentoCliente
where valor_total > 1000; 


-- Qual foi o Lucro Total obtido em Atendimento até o momento? (Retornando um atributo derivado)
select sum(valor_total) as 'Lucro Total em Atendimento' from Atendimentos;


-- Retorne a lista de Clientes ordenada em Ordem Alfabética
select * from Clientes order by Nome,Sobrenome;


-- Utilizando having statment para retornar o nome dos Clientes cujo o atendimento
-- resultou em um valor maior que R$200,00

select concat(Nome,' ', Sobrenome) as 'Nome do Cliente', Valor_Total, Data_de_Emissão as 'Data do Atendimento'
from Notas_Fiscais n
inner join Clientes c
on n.idNotaCliente = c.idCliente
group by c.Nome, c.Sobrenome
having Valor_Total > 200.0;
