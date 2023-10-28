use ecommerce;
show tables;

-- Persistindo Dados

insert into clientes (Pnome, NmeioInicial, Sobrenome, cpf, Endereço, Data_de_Nascimento)
values	('Rodrigo','C.', 'Daciole', 233331, 'Rua Rodrigues de Prata Nº 31, Cidade das Diamantinas', '1988-05-31'),
		('Alexia','L.', 'Martinez', 435422, 'Rua Alameda 1 Nº 101, Cidade das Diamantinas', '1988-07-11'),
        ('Carla','D.', 'Barbosa', 23423432, 'Rua Portugalia Nº 39, Cidade das Diamantinas', '1988-02-10'),
        ('Bjor','R.', 'Lothbrok', 3333333, 'Rua Doze de Dezembro Nº 210, Cidade das Diamantinas', '1988-09-07'),
        ('Ziguer','W.', 'Alfenor', 44424444, 'Rua dos Almondes Nº 111, Cidade das Diamantinas', '1988-12-14'),
        ('Alen','Z.', 'Turius', 126778981, 'Rua Lírios de Ouro Nº 331, Cidade das Diamantinas', '1988-06-22');
select * from clientes;



insert into produtos(Nome_Do_produto, Categoria, Descrição, Valor, Avaliação, Tamanho)
values ('Headphone JBL', 'Eletrônico','Headphone 7.1 Sem Mic.', 270.00, 9, null),
		('Sofá Retrátil Relax Plus', 'Móveis', 'Sofá retrátil Super Confortável',890.00, 8,'3x57x80'),
        ('Boneco de Ação MaxIron', 'Brinquedos', 'Boneco de Ação com Veículo', 55.6, 7, null),
        ('Polo Masculina MaxMen', 'Vestimenta', 'Polo Masculina, sem estampa', 56.0, 8, null);
select * from produtos;



insert into Pedidos(idClientePedido, pedidoStatus, pedidoDescrição, valorFrete, pagamentoBoleto)
values(1, 'confirmado', 'Compra feito no site',45, False),
		(2, default, 'Compra feita no APP', 30, True),
		(3, 'cancelado', 'Cancelada por falta de saldo', default, False),
		(4, 'confirmado', 'Compra feita no site', 60.50, True);
select * from pedidos;


insert into Produto_Pedido(idPOproduto, idPOpedido, poQuantidade, poStatus)
	values(1 ,1, 2, null),
    (2, 2, 1, null),
    (3, 3, 1, null);
select * from Produto_Pedido;


insert into Estoque(localidade, quantidade)
values('Rio de Janeiro', 1000),
('Minas Gerais', 500),
('São Paulo', 300),
('Rio Grande do Sul', 260);
select * from estoque;


insert into Estoque_Local(idLproduto, idLestoque, localização)
values (1, 2, 'MG'),
		(2, 4, 'RS');
select * from Estoque_Local;


insert into Fornecedor(RazãoSocial, CNPJ, Endereço, Cidade, Estado, Telefone, Email)
values('F&L Distribuidora', 13333333333333, 'Rua das Alagoas, Centro 222', 'São Paulo', 'SP', '22 2398131', 'f&lcontato@email'),
		('ValD Eletrônicos', 2444444444444, 'Rua Esperança, Bairro Atibaia 333', 'Rio de Janeiro', 'RJ', '21 2222222', 'vald@email'),
		('GMultimídia', 355555555555, 'Rua das Castanhas Bairro Esperança 444', 'Itauna', 'MG', '33 3333312','gm@email' );
select * from Fornecedor;


insert into Produto_Fornecedor(idPFFornecedor, idPFProduto, quantidade) 
values(1, 1, 500),
		(1, 2, 400),
        (2, 4, 633);
        
select * from Produto_Fornecedor;


insert into Vendedor(RazãoSocial, CNPJ, CPF, contato, localidade)
values('Tech&Eletro', 444433333, 1222135, 3332400, 'Minas Gerrais'),
	('Botique Durgas', 11112222333, 3333434, 2288888, 'São Paulo'),
    ('Happy World', 66666688888, 09988567, 25341212, 'Rio de Janeiro');
select * from Vendedor;


insert into Produtos_Vendedor(idPVendedor, idPProduto, PrdQuantidade)
values (10, 2, 80),
		(12, 3, 10);
select * from Produtos_Vendedor;


-- Gerando Querys

-- Quantidade total de clientes.
select count(*) as Qtd_Clientes from Clientes;

-- Informações sobre pedidos de cada cliente.
select * from Clientes c, Pedidos p where c.idCliente = idClientePedido;

-- Informações sobre pedidos de cada cliente informando os atributos.
select Pnome, Sobrenome, idPedido, pedidoStatus from Clientes c, Pedidos p where c.idCliente = idClientePedido;
select concat(Pnome,' ', Sobrenome) as Cliente, idPedido as Solicitação, pedidoStatus as Status from Clientes c, pedidos p where c.idCliente = idClientePedido;
select * from Clientes c, Pedidos p where c.idCliente = idClientePedido
group by idPedido;

-- Retorna os clientes que fizeram algum pedido
select * from Clientes c inner join Pedidos p on c.idCliente = p.idClientePedido
					inner join Produto_Pedido pr on pr.idPOpedido = p.idPedido;
