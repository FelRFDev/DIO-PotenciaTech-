-- Criando as Tabelas
drop database mecanica;
create database Mecanica;
use Mecanica;

create table Clientes(
	idCliente int auto_increment,
    Nome varchar(30) not null,
    Sobrenome varchar(30) not null,
    RG varchar(45) unique not null,
    Telefone varchar(12) not null,
    Email varchar(80) not null,
    Endereço varchar(45) not null,
    Cidade varchar(45) not null,
    Estado varchar(4) not null,
    constraint Clientes_PK primary key(idCliente)
);

create table Veiculos(
	idVeiculo int auto_increment,
    Veiculo_idCliente int,
    Placa varchar(8) not null,
    Modelo varchar(45) not null,
    Ano int not null,
    Cor varchar(20),
    constraint Veiculo_PK primary key(idVeiculo),
    constraint Clientes_Veiculos_FK foreign key Veiculos(Veiculo_idCliente) references Clientes(idCliente) 
);


create table Mecanicos(
	idMecanico int auto_increment,
    Nome varchar(30) not null,
    Sobrenome varchar(45) not null,
    RG varchar(45) unique not null,
    Endereço varchar(45) not null,
    Telefone int not null,
    Estado varchar(4),
    constraint Mecanicos_PK primary key(idMecanico)
);


create table Serviços(
	idServiço int auto_increment,
    idServiçoMecanico int not null,
    Tipo_De_Serviço varchar(40) not null,
    Valor float not null,
    Descrição varchar(45) not null,
    constraint Serviços_PK primary key(idServiço),
    constraint Servico_Mecanico_FK foreign key Serviços(idServiçoMecanico) references Mecanicos(idMecanico)
);

create table Ordem_de_Serviço(
	id_Ordem_de_Serviço int auto_increment,
    id_Ordem_de_Serviço_Serviço int not null,
    constraint Ordem_de_Serviço_PK primary key(id_Ordem_de_Serviço),
    constraint Ordem_de_Serviço_FK foreign key(id_Ordem_de_Serviço_Serviço) references Serviços(idServiço)
);
 

create table Atendimentos(
	idAtendimento int auto_increment,
	idAtendimentoCliente int not null,
    idAtendimentoVeículo int not null,
    idAtendimentoOrdem_de_Serviço int not null,
    valor_total float not null,
    constraint Atendimentos_PK primary key(idAtendimento),
    constraint Atendimento_Cliente_FK foreign key Atendimentos(idAtendimentoCliente) references Clientes(idCliente),
    constraint Atendimento_Veículo_FK foreign key Atendimentos(idAtendimentoVeículo) references Veiculos(idVeiculo),
    constraint Atendimento_Ordem_deServiço_FK foreign key Atendimentos(idAtendimentoOrdem_de_Serviço) references Ordem_de_Serviço (id_Ordem_de_Serviço)
);

create table Notas_Fiscais(
	idNotaFiscal int auto_increment,
    idNotaCliente int,
    idNotaAtendimento int,
    idNotaFiscal_OrdemServiço int, 
    Valor_Total float not null,
    Data_de_Emissão date not null,
    constraint Notas_Fiscais_PK primary key(idNotaFiscal),
    constraint Nota_Fiscal_Cliente_FK foreign key Notas_Fiscais(idNotaCliente) references Clientes(idCliente),
    constraint Nota_Fiscal_OrdemServiço_FK foreign key Notas_Fiscais(idNotaFiscal_OrdemServiço) references Ordem_de_Serviço(id_Ordem_de_Serviço)
    );


