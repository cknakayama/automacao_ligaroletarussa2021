<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">

		<link rel="stylesheet" type="text/css" href="reset.css">
		<link rel="stylesheet" type="text/css" href="estilos.css">
		<link rel="stylesheet"  href="bootstrap/css/bootstrap.css">
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
		<li><a href="#classe">Já é Membro?</a></li>
		<li><a href="#nosso_projeto">Ligas</a></li>
		<li><a href="#depoimento">Nossas ligas</a></li>
		<li><a href="#video">Video</a></li>
		<li><a href="#contatos_selecao">Contatos</a></li>
	</ul>
	</div>
	</nav>
</nav>

<section class="row centraliza " id="logo_header" >
<div class="col-xs-12" style="margin-top:20px;margin-bottom: 20px;">
	
<div class="row">
<div class="col-xs-4"></div>	
<div class="col-xs-4" style="text-align: left;text-shadow: 1px 1px 1px black;">
<h2 >Login:</h2>
<label>E-mail:</label>
<input type="text" name="nome" class="form-control">
<label>Senha</label>
<input type="text" name="nome" class="form-control">



<input type="button" name="" value="voltar" onclick="fcn_voltapagina()" class="btn btn-primary">
<input type="button" name="" value="enviar" onclick="fcn_redireciona()" class="btn btn-primary">
</div>
<div class="col-xs-4"></div>
</div>
</div>	
</section>
					
</header>
			


 	<footer >
  <section>
   <div class="row centraliza">
	 <div class="col-12">

				<h3 style="font-size: 36px;">A Liga mais competitiva do Brasil</h3>
	 </div>
	</div>
  </section>
 	</footer>

</body>
</html>
<script type="text/javascript">
	
	function fcn_voltapagina(){
		window.location.replace("index.php");

	}
	function fcn_redireciona(){
		window.location.replace("pagina_principal.php");

	}
</script>
