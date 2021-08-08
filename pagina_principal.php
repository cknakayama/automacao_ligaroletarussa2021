<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="reset.css">

	
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="estilos.css">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Roleta Russa </title>
</head>
<body>

<header>
	
				<nav class="navbar navbar-default align-text-top " >
					<div class="navbar-header">		
						<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#menuzinho" aria-expanded="false">
							<span class="sr-only"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>

						</button>
	
							<a class="navbar-brand " href="#" >Roleta Russa</a>					
					</div>

				<nav  id="menuzinho" class="collapse navbar-collapse">
					<div class="navbar">
						<ul  class="nav navbar-nav ">
							<li><a href="roleta_login.php">Já é Membro?</a></li>
							<li><a href="#nosso_projeto">Ligas</a></li>
							<li><a href="#depoimento">Nossas ligas</a></li>
							<li><a href="#video">Video</a></li>
							<li><a href="#contatos_selecao">Contatos</a></li>
						</ul>
					</div>
				</nav>
			</nav>

			<div id="logo_header" >
				<h1>Bem vindo</h1>  
				Bruno Santos Vieira 
				<ul >
					<a href="liga_principal.php"><li class="teste_li">Liga Principal</li><a>
					<a><li class="teste_li" >Liga Eliminatoria</li></a>
					<li class="teste_li">Mata Mata</li>
					<li class="teste_li">Teste</li>
				
				</ul>
			</div>
					
</header>

<input type="button" name="" value="voltar" onclick="fcn_voltapagina()" class="btn btn-primary">
<input type="button" name="" value="enviar" onclick="fcn_redireciona()" class="btn btn-primary">


</body>
<footer >
 <div class="row centraliza">
		<div class="col-xs-12">
			<h3 style="font-size: 36px;">A Liga mais competitiva do Brasil</h3>
	 	</div>
	</div>
</footer>
</html>
<script type="text/javascript">
	
	function fcn_voltapagina(){
		window.location.replace("index.php");

	}
	function fcn_redireciona(){
		window.location.replace("roleta_login.php");

	}
</script>