from sqlalchemy import create_engine


class DbUtils:
    db_string = "postgresql-psycopg2://postgres:final1215@localhost/asa"
    db_query = " "

    def create_tb_categorias(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE IF NOT EXISTS cadastro.tb_categorias (id_categoria int PRIMARY KEY, tituloCategoria varchar (30), descricaoCategoria varchar (100), fg_ativo int);"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problemas ao criar a tabela\n")
            res = False
        return res

    def create_tb_vendedores(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE IF NOT EXISTS cadastro.tb_vendedores (id_vendedor int PRIMARY KEY, cpf varchar (11), nome varchar (60), carteiraTrabalho varchar (20), telefone varchar (15), dataAdmissao date, fg_ativo int );"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problemas ao criar a tabela\n")
            res = False
        return res

    def create_tb_fornecedores(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE IF NOT EXISTS cadastro.tb_fornecedores (id_fornecedor int PRIMARY KEY, cnpj varchar (15), razaoSocial varchar (50), telefone varchar (15), endereco varchar (120), contato varchar (50), fg_ativo int);"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problemas ao criar a tabela\n")
            res = False
        return res

    def create_tb_produtos(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE IF NOT EXISTS cadastro.tb_produtos (id_produto int PRIMARY KEY, id_fornecedor int, id_categoria int, nomeProduto varchar(50), descricaoProduto varchar(120), valorUnitario numeric, quantidade int, quantidadeMinima int, fg_ativo int, foreign key(id_fornecedor) references cadastro.tb_fornecedores(id_fornecedor), foreign key(id_categoria) references cadastro.tb_categorias(id_categoria));"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problemas ao criar a tabela\n")
            res = False
        return res

    def create_tb_vendas(self):
        db = create_engine(self.db_string)
        self.db_query ="create table if not exists cadastro.tb_vendas (id_venda int primary key, id_vendedor int, id_categoria int, id_produto int, dataVenda date, valorTotal numeric, quantidade int, fg_ativo int, foreign key(id_vendedor) references cadastro.tb_vendedores(id_vendedor), foreign key(id_categoria) references cadastro.tb_categorias(id_categoria), foreign key(id_produto) references cadastro.tb_produtos(id_produto) );"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problemas ao criar a tabela")
            res = False
        return res

    def create_tb_compras(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE IF NOT EXISTS cadastro.tb_compras (id_compra int PRIMARY KEY, id_fornecedor int, id_produto int, id_categoria int, dataCompra date, valorTotal numeric, quantidade int, fg_ativo integer, foreign key(id_fornecedor) references cadastro.tb_fornecedores(id_fornecedor), foreign key(id_produto) references cadastro.tb_produtos(id_produto), foreign key(id_categoria) references cadastro.tb_categorias(id_categoria));"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problemas ao criar a tabela\n")
            res = False
        return res

    def add_categoria(self, id_categoria, tituloCategoria, descricaoCategoria, fg_ativo):
        db =create_engine(self.db_string)
        try:
            db.execute(
                "insert into cadastro.tb_categorias(id_categoria, tituloCategoria, descricaoCategoria, fg_ativo) values (%s, %s, %s, %s)", id_categoria, tituloCategoria, descricaoCategoria, fg_ativo
            )
            res = True
        except:
            print("Problemas ao inserir na tabela\n")
            res = False
        return res

    def get_categoria(self):
        db = create_engine(self.db_string)
        categoria = db.execute("SELECT * FROM cadastro.tb_categorias")
        return categoria