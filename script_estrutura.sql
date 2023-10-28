
create database ecommerce;
use ecommerce;


-- Criando tabela Clientes
create table Clientes(
idCliente int auto_increment,
    Pnome varchar(10),
    NmeioInicial char(3),
    Sobrenome varchar(20),
    cpf char(11) not null,
    Endereço varchar(100),
    Data_de_Nascimento date,
    constraint Chave_Primaria_Cliente primary key(IdCliente),
    constraint Cpf_Unico_Cliente unique(cpf)
);


alter table Clientes auto_increment = 1;

-- Criando tabela Produto
create table Produtos(
	idProduto int auto_increment,
    Nome_do_Produto varchar(30),
    Categoria enum('Eletrônico', 'Vestimenta', 'Brinquedos', 'Alimentos', 'Móveis'),
    Descrição varchar(45),
    Valor float,
    Avaliação float default 0,
    Tamanho varchar(10),
    constraint Chave_Primaria_Produtos primary key(idProduto)
);


-- Criando tabela Pagamentos

create table Pagamentos(
    idcliente int,
    idPagamento int,
    tipo_de_Pagamento enum('Boleto', 'Cartão de Débito', 'Cartão de Crédito'),
    limiteDisponível float,
    constraint Pk_Pagamento_Cliente primary key (idCliente, idPagamento)
);

-- Criando tabela Pedidos

create table Pedidos(
	idPedido int auto_increment,
    idClientePedido int,
    pedidoStatus enum('cancelado', 'confirmado', 'em processamento') default 'em processamento',
    pedidoDescrição varchar(255),
    valorFrete float default 10,
	pagamentoBoleto bool default false,
    constraint PrimaryKey_Pedidos primary key(idPedido),
    constraint FK_Pedidos_Clientes foreign key (idClientePedido) references Clientes(idCliente)
);

-- Criando tabela Estoque

create table Estoque(
	idEstoque int auto_increment,
    localidade varchar(45),
    quantidade int default 0,
    constraint PK_Estoque primary key(idEstoque)
);


-- Criando tabela fornecedor

create table Fornecedor(
	idFornecedor int auto_increment,
    RazãoSocial varchar(255) not null,
    CNPJ char(15) not null,
    Endereço varchar(50) not null,
    Cidade varchar(30) not null,
    Estado varchar(30) not null,
    Telefone varchar(20) not null,
    Email varchar(50) not null,
    constraint FK_Fornecedor primary key(idFornecedor),
    constraint CNPJ_Unico unique(CNPJ)
);

-- Criando tabela vendedor

create table Vendedor(
	idVendedor int auto_increment,
    RazãoSocial varchar(255) not null,
    CNPJ char(15) not null,
    CPF char(9),
    contato char(11) not null,
    localidade varchar(255),
    constraint PK_Vendedor primary key(idVendedor),
    constraint CNPJ_Unico unique(CNPJ),
    constraint CPF_Unico unique(CPF)
);

-- Criando tabela produtos/vendedor

create table Produtos_Vendedor(
	idPVendedor int,
    idPProduto int,
    PrdQuantidade int default 1,
    primary key(idPVendedor, idPProduto),
    constraint FK_Produtos_Vendedor foreign key (idPVendedor) references Vendedor(idVendedor),
    constraint FK_Produto_Produto foreign key (idPProduto) references Produtos(idProduto)
);

create table Produto_Pedido(
	idPOproduto int,
    idPOpedido int,
    poQuantidade int default 1,
    poStatus enum('Disponível', 'Sem Estoque') default 'Disponível',
    constraint Produto_Pedido_PK primary key(idPOproduto, idPOpedido),
    constraint fk_produtoPedido_vendedor foreign key (idPOproduto) references Produtos(idProduto),
    constraint fk_produtoPedido_produto foreign key (idPOpedido) references Pedidos(idPedido)
);


create table Estoque_Local(
	idLproduto int,
    idLestoque int,
    localização varchar(255) not null,
    constraint Estoque_Local_PK primary key(idLproduto, idLestoque),
    constraint fk_estoque_local_produto foreign key (idLproduto) references Produtos(idProduto),
    constraint fk_estoque_local_estoque foreign key (idLestoque) references Estoque(idEstoque)
);

create table Produto_Fornecedor(
	idPFFornecedor int,
    idPFProduto int, 
    quantidade int not null,
    constraint Produto_Fornecedor_PK primary key(idPFFornecedor, idPFProduto),
    constraint fk_produto_fornecedor_fornecedor foreign key (idPFFornecedor) references Fornecedor(idFornecedor),
    constraint fk_produto_fornecedor_produto foreign key (idPFproduto) references Produtos(idProduto)
);

