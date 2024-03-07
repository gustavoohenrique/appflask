from flask import Flask, render_template

app = Flask(__name__)

#Criar a primeira página do site
#route -> Qual o link da página
# Função -> O que você quer exibir naquela página
#template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

#Escrito dentro da boca de jacaré será dinâmico
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


#Colocar o site no ar

#Debug ativado todas edições feitas no código já serão exibidas na página web.
if __name__ == "__main__":
    app.run(debug=True)