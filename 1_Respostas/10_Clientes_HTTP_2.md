1. Utilize o programa criado pelo professor para baixar as páginas principais dos seguintes sites:

(a) www.google.com

```
Deu erro
Abrindo o socket para o cliente... Feito!
Obtendo o IP do servidor... Can't resolve host: No space left on device

```

(b) www.google.com.br

```HTML
Deu erro
Abrindo o socket para o cliente... Feito!
Obtendo o IP do servidor... Can't resolve host: No space left on device

```

(c) www.unb.br

```HTML
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 21 Apr 2019 16:18:11 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Vary: Accept-Encoding
Referrer-Policy: origin
Upgrade-Insecure-Requests: 0
Set-Cookie: 3ec986f4f850e1d0bdcd00fd24b0c473=ni9p5i67soh7gts3aemq4rncj6; path=/; HttpOnly
Expires: Wed, 17 Aug 2005 00:00:00 GMT
Last-Modified: Sat, 21 Apr 2019 16:18:11 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Vary: Accept-Encoding
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff

1dbe
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-br" lang="pt-br" dir="ltr">
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
  	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
	<script>
		function openMenu(){
			var x = document.getElementById("responsiveMenu");
			if (x.className === "nav menu menuPrincipal") {
				x.className += " responsive";
			} else {
				x.className = "nav menu menuPrincipal";
			}
		}
		/*Ocultar/exibir menu dropdown ao clicar em dispositivos móveis*/
		jQuery(function($) {
			$(document).ready(function(){
					$('.nav-header').click(function(){
							$('.nav-header').not(this).nextUntil('.nav-header').hide();
							$('.nav-header').not(this).attr("style", "background: url(/images/icones/icon_mais.png) no-repeat right;");
								$(this).nextUntil('.nav-header').toggle();
							if ($(this).closest('li').find('ul').is(':hidden')){
									$(this).attr("style", "background: url(/images/icones/icon_mais.png) no-repeat right;");
							}
							else {
								$(this).attr("style", "background: url(/images/icones/icon_menos.png) no-repeat right;");
							}
							return false;
					});
					$(document).click(function(){
							var largura = $(document).width();
                                                        if (largura < 641){
								$('.nav-header').nextUntil('.nav-header').hide();
								$('.nav-header').attr("style", "background: url(/images/icones/icon_mais.png) no-repeat right;");
							}
					});
					
					$(window).resize(function(){
							var largura = $(document).width();
							if (largura > 641){
								$('#responsiveMenu').removeClass('responsive');
							}
					});
			});
		});
	</script>
   	<base href="http://www.unb.br/" />
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="generator" content="Joomla! - Open Source Content Management" />
	<title>UnB - Universidade de Brasília - Início</title>
	<link href="/?format=feed&amp;type=rss" rel="alternate" type="application/rss+xml" title="RSS 2.0" />
	<link href="/?format=feed&amp;type=atom" rel="alternate" type="application/atom+xml" title="Atom 1.0" />
	<link href="/templates/unb/favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
	<link href="/templates/unb/css/template.css" rel="stylesheet" type="text/css" />
	<link href="/templates/unb/css/custom.css" rel="stylesheet" type="text/css" />
	<link href="/templates/unb/css/menu.css" rel="stylesheet" type="text/css" />
	<link href="/plugins/system/vembed/vembed.css" rel="stylesheet" type="text/css" />
	<link href="/media/jfontsize/css/jfontsize.css" rel="stylesheet" type="text/css" />
	<script type="application/json" class="joomla-script-options new">{"csrf.token":"9273f7d177e338ebc85dd24783397964","system.paths":{"root":"","base":""}}</script>
	<script src="/media/jui/js/jquery.min.js?df485351eda0a833786ce440b4a4a85c" type="text/javascript"></script>
	<script src="/media/jui/js/jquery-noconflict.js?df485351eda0a833786ce440b4a4a85c" type="text/javascript"></script>
	<script src="/media/jui/js/jquery-migrate.min.js?df485351eda0a833786ce440b4a4a85c" type="text/javascript"></script>
	<script src="/media/system/js/caption.js?df485351eda0a833786ce440b4a4a85c" type="text/javascript"></script>
	<script src="/media/jui/js/bootstrap.min.js?df485351eda0a833786ce440b4a4a85c" type="text/javascript"></script>
	<script src="/media/system/js/core.js?df485351eda0a833786ce440b4a4a85c" type="text/javascript"></script>
	<script src="/templates/unb/js/template.js" type="text/javascript"></script>
	<script src="/components/com_extrawatch/js/jdownloadurl.js" type="text/javascript"></script>
	<script src="/components/com_extrawatch/js/extrawatch.js" type="text/javascript"></script>
	<script src="/media/jfontsize/js/jquery.jfontsize-1.0.min.js" type="text/javascript"></script>
	<script type="text/javascript">
jQuery(window).on('load',  function() {
				new JCaption('img.caption');
			});
	</script>
	<script type="text/javascript">
	(function ($) {
		$().ready(function () {
			 $('body').jfontsize({
			     btnMinusClasseId: '#jfontsize-minus',
			     btnDefaultClasseId: '#jfontsize-default',
			     btnPlusClasseId: '#jfontsize-plus',
			     btnMinusMaxHits: 10,
			     btnPlusMaxHits: 10,
			     sizeChange: 1
			 });
		});
	})(jQuery)
</script>

				<link href='//fonts.googleapis.com/css?family=liberation_sansregular' rel='stylesheet' type='text/css' /> 
		<style type="text/css">
			h1,h2,h3,h4,h5,h6,.site-title{
				font-family: 'liberation_sansregular', sans-serif;
			}
		</style>
				<style type="text/css">
		body.site
		{
			border-top: 3px solid #1b4a81;
			background-color: #ffffff		}
		a
		{
			color: #1b4a81;
		}
		.navbar-inner, .nav-list > .active > a, .nav-list > .active > a:hover, .dropdown-menu li > a:hover, .dropdown-menu .active > a, .dropdown-menu .active > a:hover, .nav-pills > .active > a, .nav-pills > .active > a:hover,
		.btn-primary
		{
			background: #1b4a81;
		}
		.navbar-inner
		{
			-moz-box-shadow: 0 1px 3px rgba(0, 0, 0, .25), inset 0 -1px 0 rgba(0, 0, 0, .1), inset 0 30px 10px rgba(0, 0, 0, .2);
			-webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, .25), inset 0 -1px 0 rgba(0, 0, 0, .1), inset 0 30px 10px rgba(0, 0, 0, .2);
			box-shadow: 0 1px 3px rgba(0, 0, 0, .25), inset 0 -1px 0 rgba(0, 0, 0, .1), inset 0 30px 10px rgba(0, 0, 0, .2);
		}

	</style>
		  	<!--[if lt IE 9]>
		<script src="/media/jui/js/html5.js"></script>
	<![endif]-->
	<script defer="defer" src="//barra.brasil.gov.br/barra.js" type="text/javascript"></script>
</head>

<body class="site com_content view-featured no-layout no-task itemid-101">

	<!-- Body -->
	<div class="body">
	<div id="barra-brasil" style="background:#7F7F7F; height: 20px; padding:0 0 0 10px;display:block;"> 
		<ul id="menu-barra-temp" style="list-style:none;">
			<li style="display:inline; float:left;padding-right:10px; margin-right:10px; border-right:1px solid #EDEDED"><a href="http://brasil.gov.br" style="font-family:sans,sans-serif; text-decoration:none; color:white;">Portal do Governo Brasileiro</a></li> 
			<li><a style="font-family:sans,sans-serif; text-decoration:none; color:white;" href="http://epwg.governoeletronico.gov.br/barra/atualize.html">Atualize sua Barra de Governo</a></li>
		</ul>
	</div>
		<!--<div class="barra-topo">
			<div class="barra-inner container">
				<div class="row-fluid">
					<div class="logo-unb span3">
						

<div class="custom"  >
	<p><a title="Ir para o Portal da UnB" href="http://www.unb.br"><img src="/images/logo-unb.png" alt="" /></a></p></div>

					</div>
					<div class="menu-unb span7">
						<div class="menu-toggle-list">
							<a class="btn-menu" data-toggle="collapse" data-target="#menu-collapse">
								<img src="/images/icon-menu.png" alt="Ícone do menu"> <span>Menu</span>
							</a>
							<div id="menu-collapse" class="sp-mobile-menu collapse">
								    
							</div>
						</div>	
					</div>
					<div class="links-unb span2 pull-right">
						
					</div>
					<div class="clearfix"></div>
				</div>
			</div>-->
       <link type="text/css" href="https://web.unb.br/templates/compartilhado/css/template.css" rel="stylesheet">
  
<div class="barra-topo">
    <div class="barra-inner container">
      <div class="row-fluid">
          <div class="logo-unb span3">
             <div class="custom">
				<p>
                  </p>
			 </div>
          </div>
          <div class="menu-unb span7">
                    
  
          </div>
          <div class="links-unb span2 pull-right">

2000
                 <div class="modulo-icones-barratopo" style="float:right">
                     <ul>
                         <!-- 111 <li><a target="_blank" href="https://webmail.unb.br/" class="icones-barratopo" id="default">&nbsp;</a>
                         </li> -->
<!-- JONA-->                         <li><a target="_blank" href="https://webmail.unb.br/" class="icones-barratopo" id="webmail" title="Webmail">&nbsp;</a>
                         </li>
			          	 			<li><a href="/../mapa-site" class="icones-barratopo" class="icones-barratopo" style="padding-right:35px" id="mapa" title="Mapa do Site">&nbsp;</a>
                                        </li>
                   	                          <li><a target="_blank" href="https://www.unb.br/images/mprazer.pdf" id="telefones" title="Telefones da UnB">&nbsp;</a>
                         </li>
                         <li><a target="_blank" href="http://www.unb.br/documentos?menu=475" id="transparencia" title="Transparência UnB">&nbsp;</a>
                         </li>
                       
                       <li><a target="_blank" href="http://www.sistemas.unb.br" class="icones-barratopo" id="sistemas" title="Sistemas">&nbsp;</a>
                         </li> 
                       
                       
                     </ul>
                 </div>
          </div>
          <div class="clearfix"></div>
        </div>
    </div>
  </div>



  

		</div>
		<div class="container">
			<!-- Header -->
			<header class="header" role="banner">
				<div class="header-inner clearfix">
					<a class="brand pull-left" href="/">
						<img src="http://www.unb.br/images/Imagens/logo_unb.png" alt="UnB - Universidade de Brasília" />											</a>
					<div class="header-search pull-right">
						<form action="/component/pesquisagoogle/" id="form_pesquisa" method="post" style="display:none">
    <div class="btn-toolbar">
        <div class="btn-group pull-left"> 
            <!-- <input type="text" name="busca" placeholder="Pesquisar..." maxlength="" value="" class="inputbox search-query" /> -->
            <input name="busca" id="mod-search-searchword" class="inputbox search-query" type="search" size="20" placeholder="Pesquisar...">
        </div>
    </div>
</form>

<script>
    
     jQuery(function($a) {
    	$a("#pesquisa").click(function() {
        		$a("#form_pesquisa").css("display", "inline-table");
        		$a("#pesquisa").css("display", "none");
                        $a(".search-query").attr("style" ,"margin-right: 5px;");
                        var largura = $a(document).width();
                        if (largura <= 767){
                             $a(".jfontsize").attr("style", "width: 40% !important");
			}
			else{
                           $a(".jfontsize").attr("style", "width: 103px !important;");
			}
	});	
    });
</script>
<div class="jfontsize">
	<a class="jfontsize-button" id="pesquisa">
        <!-- <img src="/images/icones/icon_pesquisar.png" class="icone_pesquisa"> --> </a>
        <a class="jfontsize-button" id="contraste"></a>
	<a class="jfontsize-button" id="jfontsize-minus">A-</a>
	<a class="jfontsize-button" id="jfontsize-default">A</a>
	<a class="jfontsize-button" id="jfontsize-plus">A+</a>
</div>

<script>
(function ($) {
		$().ready(function () {
		$( "a#contraste" ).click(function() {
  		$("html").toggleClass( "contraste" );
  		});
		});
	})(jQuery)

</script>

					</div>
				</div>
			</header>
			<div class="iconMenuResp">
				<a href="javascript:void(0);" class="linkMenu" onclick="openMenu()"><h4>MENU</h4>
					<img src="/images/icones/icon_menu.png">
				</a>
			</div><span class="espacos"><br><br></span>
    							<div class="row-fluid">
					<div class="menu-site span12">
						<nav class="navigation navbar" role="navigation">
							<ul class="nav menu menuPrincipal"style="position:relative;z-index:3" id="responsiveMenu">
<li class="item-101 current active"><a class=" hidden" href="/" >Início</a></li><li class="item-722 deeper parent"><span class="nav-header " >Notícias</span>
<ul class="dropdown-menu-principal"><li class="item-723"><a href="https://noticias.unb.br/publicacoes" target="_blank" >Últimas</a></li><li class="item-724"><a href="https://www.unbciencia.unb.br/" target="_blank" >UnBCiência</a></li><li class="item-725"><a href="https://www.noticias.unb.br/component/agenda/agendas" target="_blank" >UnBAgenda</a></li><li class="item-726"><a href="https://www.noticias.unb.br/unb-hoje" target="_blank" >UnBHoje</a></li><li class="item-727"><a href="http://www.revistadarcy.unb.br/" target="_blank" >Darcy</a></li></ul></li><li class="item-422 deeper parent"><span class="nav-header " >Institucional</span>
<ul class="dropdown-menu-principal"><li class="item-592"><a href="http://www.unb.br/a-unb?menu=423" >A UnB</a></li><li class="item-593"><a href="http://www.unb.br/campi?menu=424" >Campi</a></li><li class="item-594"><a href="http://www.unb.br/estrutura-administrativa?menu=425" >Estrutura administrativa</a></li><li class="item-595"><a href="http://www.prefeitura.unb.br" target="_blank" >Prefeitura</a></li><li class="item-597"><a href="http://www.unb.br/documentos?menu=475" >Transparência e documentos</a></li></ul></li><li class="item-373 deeper parent"><span class="nav-header " >Estude na UnB</span>
<ul class="dropdown-menu-principal"><li class="item-598"><a href="http://www.unb.br/graduacao2?menu=434" >Graduação</a></li><li class="item-599"><a href="http://www.unb.br/pos-graduacao2?menu=435" >Pós-graduação</a></li></ul></li><li class="item-374 deeper parent"><span class="nav-header " >Aluno</span>
<ul class="dropdown-menu-principal"><li class="item-601"><a href="http://www.unb.br/graduacao?menu=439" >Graduação</a></li><li class="item-602"><a href="http://www.unb.br/pos-graduacao?menu=440" >Pós-graduação</a></li><li class="item-701"><a href="http://dex.unb.br/" >Extensão</a></li><li class="item-606"><a href="/aluno/ex-aluno" >Ex-aluno</a></li><li class="item-607"><a href="http://www.unbidiomas.unb.br/" target="_blank" >Idiomas</a></li><li class="item-608"><a href="http://www.unb.br/atendimento?menu=471" >Atendimento</a></li><li class="item-609"><a href="https://www.facebook.com/dce.unb/" target="_blank" >Diretório Central dos Estudantes</a></li><li class="item-603"><a href="http://www.unb.br/educacao-a-distancia?menu=441" >Educação a distância</a></li><li class="item-103"><a href="http://aprender.unb.br/" target="_blank" >Aprender UnB</a></li><li class="item-604"><a href="http://www.dds.dac.unb.br" target="_blank" >Assistência estudantil</a></li><li class="item-642"><a href="https://aluno.unb.br/" target="_blank" >Portal Aluno</a></li><li class="item-327"><a href="https://servicos.unb.br/dadosdados/login/index.html?response_type=code&amp;client_id=95&amp;redirect_uri=/sae/index.html" target="_blank" >SaeWeb</a></li><li class="item-605"><a href="https://matriculaweb.unb.br/" onclick="window.open(this.href,'targetWindow','toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,');return false;" >Matrícula Web</a></li></ul></li><li class="item-375 deeper parent"><span class="nav-header " >Unidades acadêmicas</span>
<ul class="dropdown-menu-principal"><li class="item-610"><a href="/unidades-academicas/institutos" >Institutos</a></li><li class="item-611"><a href="/unidades-academicas/faculdades" >Faculdades</a></li><li class="item-612"><a href="/unidades-academicas/centros" >Centros</a></li><li class="item-613"><a href="/unidades-academicas/nucleos" >Núcleos</a></li><li class="item-614"><a href="/unidades-academicas/laboratorios" >Laboratórios</a></li><li class="item-542"><a href="http://www.fal.unb.br/" target="_blank" >Fazenda Água Limpa</a></li></ul></li><li class="item-376 deeper parent"><span class="nav-header " >Serviços</span>
<ul class="dropdown-menu-principal"><li class="item-615"><a href="http://www.saa.unb.br/calendarios" target="_blank" >Calendários</a></li><li class="item-616"><a href="http://www.unb.br/images/Noticias/2016/Documentos/Carta_Cidadao.pdf" target="_blank" >Carta de Serviços</a></li><li class="item-617"><a href="http://www.bc
2000
e.unb.br/" target="_blank" >Biblioteca Central</a></li><li class="item-251"><a href="http://www.museuvirtual.unb.br/index.htm" target="_blank" >Museu Virtual</a></li><li class="item-618"><a href="http://www.arquivocentral.unb.br/" target="_blank" >Arquivo Central</a></li><li class="item-619"><a href="http://www.ebserh.gov.br/web/hub-unb" target="_blank" >Hospital Universitário</a></li><li class="item-620"><a href="/servicos/hospitais-veterinarios" >Hospitais Veterinários</a></li><li class="item-621"><a href="http://www.ouvidoria.unb.br/" target="_blank" >Ouvidoria</a></li><li class="item-622"><a href="http://www.ppne.unb.br/" target="_blank" >Necessidades especiais</a></li><li class="item-623"><a href="http://www.editora.unb.br/" target="_blank" >Editora</a></li><li class="item-729"><a href="/servicos/menu-campi" >Conheça os campi</a></li><li class="item-631"><a href="/servicos/transporte" >Transporte</a></li><li class="item-632"><a href="/servicos/alimentacao" >Alimentação</a></li><li class="item-308"><a href="/servicos/fale-conosco" >Fale Conosco</a></li></ul></li><li class="item-377 deeper parent"><span class="nav-header " >Comunidade</span>
<ul class="dropdown-menu-principal"><li class="item-580"><a href="https://www.sistemas.unb.br/siex/publico/oferta_extensao_listagem.xhtml" target="_blank" >Projetos de extensão</a></li><li class="item-624"><a href="http://www.dea.unb.br/" target="_blank" >Esporte, Arte e Cultura</a></li><li class="item-625"><a href="/comunidade/nossos-pesquisadores" >Nossos Pesquisadores</a></li><li class="item-626"><a href="http://www.unb.br/oportunidades?menu=456" >Oportunidades</a></li><li class="item-627"><a href="http://www.cds.unb.br/" target="_blank" >Sustentabilidade</a></li><li class="item-628"><a href="https://www.facebook.com/divunb" target="_blank" >Diversidade</a></li><li class="item-629"><a href="http://www.cal.unb.br/" target="_blank" >Casa da Cultura da América Latina</a></li><li class="item-600"><a href="http://www.unbidiomas.unb.br/" target="_blank" >UnB Idiomas</a></li></ul></li><li class="item-378 deeper parent"><span class="nav-header " >Servidor</span>
<ul class="dropdown-menu-principal"><li class="item-633"><a href="http://dgp.unb.br" target="_blank" >Docente</a></li><li class="item-634"><a href="http://dgp.unb.br" target="_blank" >Técnico administrativo</a></li><li class="item-635"><a href="http://dgp.unb.br/servi" target="_blank" >Guia do Servidor</a></li><li class="item-372"><a href="http://www.capacitacao.unb.br/" target="_blank" >Capacitação</a></li><li class="item-591"><a href="/servidor/sindicatos-e-associacoes" >Sindicatos e Associações</a></li></ul></li></ul>


<div class="custom redes-sociais"  >
	<p><a href="https://www.facebook.com/oficialUnB/" target="_blank" rel="alternate noopener noreferrer"><img src="/images/icones/facebook_01.fw.png" alt="facebook 01.fw" /></a> <a href="https://www.instagram.com/unb_oficial/" target="_blank" rel="alternate noopener noreferrer"><img src="/images/icones/instagran_01.fw.png" alt="instagran 01.fw" /></a> <a href="https://twitter.com/unb_oficial" target="_blank" rel="noopener noreferrer"><img src="/images/icones/twitter_01.fw.png" alt="twitter 01.fw" /></a> <a href="http://www.noticias.unb.br" target="_blank" rel="alternate noopener noreferrer"><img src="/images/icones/rss_01.fw.png" alt="rss 01.fw" /></a>&nbsp;<a href="http://www.flickr.com/photos/unb_agencia" target="_blank" rel="noopener noreferrer"><img src="/images/icones/flick.png" alt="flick.fw" width="31" height="32" /></a></p></div>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  </head>
</html>
<div id="myCarousel1" data-interval="5000" class="newsflash carousel slide" data-ride="carousel" >

        <!-- Wrapper for slides -->
        <div class="carousel-inner fadeIn" >
                     
           <div class="item active fadeIn">
                        <a href="http://noticias.unb.br/publicacoes/76-institucional/2538-unb-e-a-9-melhor-do-pais-em-ranking-da-folha" target="_blank" title="UnB é nona melhor instituição de ensino superior do país">
                         <img src="/images/Noticias/2018/BannerTopDestaques/03102018_ICC_JulioMinasi.jpg"/>
                        </a>
                        <div class="carousel-caption fadeIn"> 
                <span class="chapeu">RANKING FOLHA</span>
                <h4>
                                    <a href="http://noticias.unb.br/publicacoes/76-institucional/2538-unb-e-a-9-melhor-do-pais-em-ranking-da-folha" target="_blank" title="UnB é nona melhor instituição de ensino superior do país">
                                    UnB é nona melhor instituição de ensino superior do país                                            </a>
                                    </h4>
                <p></p>
            </div>
            
            
        </div>
                 
           <div class="item  fadeIn">
                        <a href="http://noticias.unb.br/publicacoes/124-esporte-e-cultura/2530-mostra-une-criatividade-tecnologia-e-inovacao-para-apresentar-cursos-da-unb" target="_blank" title="Milhares de estudantes de ensino médio conhecem a UnB">
                         <img src="/images/Noticias/2018/BannerTopDestaques/25set18_cinedebate_chegadefiufiu_andregomes_destaque-3.JPG"/>
                        </a>
                        <div class="carousel-caption fadeIn"> 
                <span class="chapeu">MOSTRA DE CURSOS</span>
                <h4>
                                    <a href="http://noticias.unb.br/publicacoes/124-esporte-e-cultura/2530-mostra-une-criatividade-tecnologia-e-inovacao-para-apresentar-cursos-da-unb" target="_blank" title="Milhares de estudantes de ensino médio conhecem a UnB">
                                    Milhares de estudantes de ensino médio conhecem a UnB                                            </a>
                                    </h4>
                <p></p>
            </div>
            
            
        </div>
                 
           <div class="item  fadeIn">
                        <a href="http://noticias.unb.br/publicacoes/76-institucional/2476-caminhos-pensados-para-seu-bem-estar" target="_blank" title="Conheça os melhores caminhos para andar com tranquilidade">
                         <img src="/images/Noticias/2018/DestaquesSlide/BannerCorredorSegurança_940.jpg"/>
                        </a>
                        <div class="carousel-caption fadeIn"> 
                <span class="chapeu">CAMPUS DARCY RIBEIRO</span>
                <h4>
                                    <a href="http://noticias.unb.br/publicacoes/76-institucional/2476-caminhos-pensados-para-seu-bem-estar" target="_blank" title="Conheça os melhores caminhos para andar com tranquilidade">
                                    Conheça os melhores caminhos para andar com tranquilidade                                            </a>
                                    </h4>
                <p> </p>
            </div>
            
            
        </div>
        </div>
    <!-- Indicators -->
    <div class="navegar-item">
        <ol class="carousel-indicators">
                            <li data-target="#myCarousel1" data-slide-to="0" class="active"></li>
                            <li data-target="#myCarousel1" data-slide-to="1" class=""></li>
                            <li data-target="#myCarousel1" data-slide-to="2" class=""></li>
                    </ol>
    </div>
    
<!-- Controles -->
 <!--    <div class="controles-item">
            <a class="left carousel-control" href="#myCarousel1" role="button" data-slide="prev">
                <span class="icon-chevron-left"></span>
            </a>
            <a class="right carousel-control" href="#myCarousel1" role="button" data-slide="next">
                <sp
2000
an class="icon-chevron-right"></span>
            </a>
        </div>   -->
</div>
<div class="noticias-destaques">
	<br>
	<table id="noticias" border="0">
		<tr>
					<td>	
				<div class="item">
				  <div class="imgArtigo">
					<a href="http://noticias.unb.br/publicacoes/124-esporte-e-cultura/2535-programa-bolsa-atleta-oferece-110-vagas" itemprop="url" target="_blank" title="Programa Bolsa Atleta do Esporte Universitário oferece 110 vagas">
						<img class="imgartigo" src="/images/Noticias/2018/DestaquesSlide/20082018_Natacao_DEL.jpg"/>
					</a>
					<!-- <span class="nomeautor"></span> -->
				  </div>
				  <div class="titulo-autor">
					<span class="chapeu">
					 INSCRIÇÕES ATÉ DIA 14					</span>
					<h5>
					  <a href="http://noticias.unb.br/publicacoes/124-esporte-e-cultura/2535-programa-bolsa-atleta-oferece-110-vagas" itemprop="url" target="_blank" title="Programa Bolsa Atleta do Esporte Universitário oferece 110 vagas">
						<div class="tituloNoticia">
							<span itemprop="name">
								Programa Bolsa Atleta do Esporte Universitário oferece 110 vagas							</span>
						</div>
					  </a>
					</h5>
					<br>
				  </div>
				</div>
			</td>
					<td>	
				<div class="item">
				  <div class="imgArtigo">
					<a href="http://noticias.unb.br/publicacoes/67-ensino/2536-editais-do-programa-de-avaliacao-seriada-sao-divulgados" itemprop="url" target="_blank" title="Editais do Programa de Avaliação Seriada (PAS) são divulgados">
						<img class="imgartigo" src="http://noticias.unb.br/images/Noticias/Fotos_frequentes/23072018_PAS_BeatrizFerraz.jpg"/>
					</a>
					<!-- <span class="nomeautor"></span> -->
				  </div>
				  <div class="titulo-autor">
					<span class="chapeu">
					 ADMISSÃO					</span>
					<h5>
					  <a href="http://noticias.unb.br/publicacoes/67-ensino/2536-editais-do-programa-de-avaliacao-seriada-sao-divulgados" itemprop="url" target="_blank" title="Editais do Programa de Avaliação Seriada (PAS) são divulgados">
						<div class="tituloNoticia">
							<span itemprop="name">
								Editais do Programa de Avaliação Seriada (PAS) são divulgados							</span>
						</div>
					  </a>
					</h5>
					<br>
				  </div>
				</div>
			</td>
					<td>	
				<div class="item">
				  <div class="imgArtigo">
					<a href="http://noticias.unb.br/publicacoes/124-esporte-e-cultura/2539-roda-de-conversa-aborda-saude-e-sexualidade-indigena" itemprop="url" target="_blank" title="Encontro idealizado por estudantes discute sexualidade indígena">
						<img class="imgartigo" src="/images/Noticias/2018/DestaquesSlide/24jul18_maloca_lgprado_03.jpg"/>
					</a>
					<!-- <span class="nomeautor"></span> -->
				  </div>
				  <div class="titulo-autor">
					<span class="chapeu">
					 SEXTA-FEIRA, DIA 5					</span>
					<h5>
					  <a href="http://noticias.unb.br/publicacoes/124-esporte-e-cultura/2539-roda-de-conversa-aborda-saude-e-sexualidade-indigena" itemprop="url" target="_blank" title="Encontro idealizado por estudantes discute sexualidade indígena">
						<div class="tituloNoticia">
							<span itemprop="name">
								Encontro idealizado por estudantes discute sexualidade indígena							</span>
						</div>
					  </a>
					</h5>
					<br>
				  </div>
				</div>
			</td>
		</tr><tr>			<td>	
				<div class="item">
				  <div class="imgArtigo">
					<a href="https://noticias.unb.br/publicacoes/76-institucional/2509-cad-cria-comissao-para-rever-normativa-de-2013-sobre-a-flexibilizacao" itemprop="url" target="_blank" title="CAD aprova comissão para rever norma de flexibilização de jornada">
						<img class="imgartigo" src="http://noticias.unb.br/images/Noticias/2018/09-Set/20set18_cad_lgprado_06.jpg"/>
					</a>
					<!-- <span class="nomeautor"></span> -->
				  </div>
				  <div class="titulo-autor">
					<span class="chapeu">
					 ÓRGÃOS COLEGIADOS					</span>
					<h5>
					  <a href="https://noticias.unb.br/publicacoes/76-institucional/2509-cad-cria-comissao-para-rever-normativa-de-2013-sobre-a-flexibilizacao" itemprop="url" target="_blank" title="CAD aprova comissão para rever norma de flexibilização de jornada">
						<div class="tituloNoticia">
							<span itemprop="name">
								CAD aprova comissão para rever norma de flexibilização de jornada							</span>
						</div>
					  </a>
					</h5>
					<br>
				  </div>
				</div>
			</td>
					<td>	
				<div class="item">
				  <div class="imgArtigo">
					<a href="http://www.unbciencia.unb.br/artes-e-letras/100-artes-cenicas/589-laboratorio-impulsiona-experiencias-criativas-nos-palcos" itemprop="url" target="_blank" title="Laboratório de Dramaturgia completa vinte anos em atividade">
						<img class="imgartigo" src="http://www.unbciencia.unb.br/images/Noticias/2018/09-Set/23082018_LabDramaturgia_BetoMonteiro-98.jpg"/>
					</a>
					<!-- <span class="nomeautor"></span> -->
				  </div>
				  <div class="titulo-autor">
					<span class="chapeu">
					 ARTES CÊNICAS					</span>
					<h5>
					  <a href="http://www.unbciencia.unb.br/artes-e-letras/100-artes-cenicas/589-laboratorio-impulsiona-experiencias-criativas-nos-palcos" itemprop="url" target="_blank" title="Laboratório de Dramaturgia completa vinte anos em atividade">
						<div class="tituloNoticia">
							<span itemprop="name">
								Laboratório de Dramaturgia completa vinte anos em atividade							</span>
						</div>
					  </a>
					</h5>
					<br>
				  </div>
				</div>
			</td>
					<td>	
				<div class="item">
				  <div class="imgArtigo">
					<a href="http://noticias.unb.br/publicacoes/76-institucional/2534-pos-graduacao-tera-oficinas-por-areas-de-conhecimento" itemprop="url" target="_blank" title="Oficinas por áreas visam aperfeiçoar a pós-graduação">
						<img class="imgartigo" src="/images/Noticias/2018/DestaquesSlide/01out18_seminariodpg_lgprado_10.jpg"/>
					</a>
					<!-- <span class="nomeautor"></span> -->
				  </div>
				  <div class="titulo-autor">
					<span class="chapeu">
					 SEMINÁRIO DPG					</span>
					<h5>
					  <a href="http://noticias.unb.br/publicacoes/76-institucional/2534-pos-graduacao-tera-oficinas-por-areas-de-conhecimento" itemprop="url" target="_blank" title="Oficinas por áreas visam aperfeiçoar a pós-graduação">
						<div class="tituloNoticia">
							<span itemprop="name">
								Oficinas por áreas visam aperfeiçoar a pós-graduação							</span>
						</div>
					  </a>
					</h5>
					<br>
				  </div>
				</div>
			</td>
		</tr><tr>		
		</tr>
	</table>
</div>
<div>
	<p class="linkTodasNoticias">
		<a href="http://noticias.unb.br" target="_blank">ACESSE TODAS AS NOTÍCIAS
			<img src="/images/icones/icon_mais_noticias.png" class="todasNoticias">
		</a>
	</p>
	<br><br><br>
</div>
<div class="agenda">
    <div class="agenda-titulo-link">
	<h3> <a href="http://noticias.unb.br/component/agenda/agendas" target="_blank" class="link-agenda"> FIQUE POR DENTRO </a></h3>    
    </div>
    <div class="lista-agenda">
                                                                    <div class="item-content"> 
                                            <div class="data">
                            04 | Out                            
			    <small>.</small> <span>16:00 </span>                
                        </div>
                                        <div class="item-content-inner">
                        <h5 class="titulo">
                                                    <a href="http://noticias.unb.br/component/agenda/agenda/2075" target="_blank">
                        <!-- <a href="/component/agenda/agenda/2075"> -->
                                                        Credit Supply and House Prices: Exploring discontinuities in financing limits of a government program in Brazil                            </a>
                        </h5>  
                          
                    </div>
                    <div class="clr"></div>
                </div>
                                                                                        <div class="item-content"> 
                                            <div class="data">
                            05 | Out             
1000
               
			    <small>.</small> <span>10:00 </span>                
                        </div>
                                        <div class="item-content-inner">
                        <h5 class="titulo">
                                                    <a href="http://noticias.unb.br/component/agenda/agenda/2080" target="_blank">
                        <!-- <a href="/component/agenda/agenda/2080"> -->
                                                        TV, Pluralismo e Direito à Informação                           </a>
                        </h5>  
                          
                    </div>
                    <div class="clr"></div>
                </div>
                                                                                        <div class="item-content"> 
                                            <div class="data">
                            05 | Out                            
			    <small>.</small> <span>12:00 </span>                
                        </div>
                                        <div class="item-content-inner">
                        <h5 class="titulo">
                                                    <a href="http://noticias.unb.br/component/agenda/agenda/2085" target="_blank">
                        <!-- <a href="/component/agenda/agenda/2085"> -->
                                                        Roda de conversa sobre sexualidade indígena                           </a>
                        </h5>  
                          
                    </div>
                    <div class="clr"></div>
                </div>
                                                                                        <div class="item-content"> 
                                            <div class="data">
                            05 | Out                            
			    <small>.</small> <span>17:00 </span>                
                        </div>
                                        <div class="item-content-inner">
                        <h5 class="titulo">
                                                    <a href="http://noticias.unb.br/component/agenda/agenda/2088" target="_blank">
                        <!-- <a href="/component/agenda/agenda/2088"> -->
                                                        1º Happy Hour do Sintfub                            </a>
                        </h5>  
                          
                    </div>
                    <div class="clr"></div>
                </div>
                                </div>
</div>

						</nav>
					</div>			
				</div>
						
			<div class="row-fluid">
								<main id="content" role="main" class="span4">
					<!-- Begin Content -->
							<div class="moduletable noticias-clipping">
						<style>
input.tabs:checked + label {
  line-height:30px;
  color: #fff;
  background: #003a7a;
  border-bottom: 5px solid #fff;
  

  
}
input.tabs:checked + label + div {
  opacity: 1;
  z-index: 1000;
}

.cliping_item{
   margin: 0px 0 16px 0;
    font-weight: normal;
}
 </style>

<div class="tabs-container">
 
  <input type="radio" name="tabs" class="tabs" id="artigos" value="artigos" checked="checked">
  <label for="artigos">ARTIGOS</label>
  <div>
   
    
      <div class="carousel-inner">
        <div class="item active">
                          <div class="itemlastnews">
              <div class="itemlastnews-inner artigo-item">
                
                  <div class="boxautor">
                    <img class="imgautorartigo" src="https://noticias.unb.br//images/autores/22112017_ProfAndreReis_28_LGPrado.jpg"/>
                  </div>
                
                  <div class="titulo-autor">
                    <span class="chapeuartigo">
                      01/10/2018                    </span>
                    <h5 class="titulo_artigo">
                      <a target="_blanck" href="https://noticias.unb.br//artigos-main/2533-politica-de-acoes-do-dac-fomenta-participacao-da-comunidade-academica" itemprop="url">
  
2000
                      <span itemprop="name">
							Política de ações do DAC fomenta participação da comunidade acad?...                        </span>
                      
                      </a>
                      
                    </h5>
                    <span class="nomeautor">André Reis¹</span>
                  </div>
                
                <div class="clearfix"></div>
              </div>
            </div>               <div class="itemlastnews">
              <div class="itemlastnews-inner artigo-item">
                
                  <div class="boxautor">
                    <img class="imgautorartigo" src="https://noticias.unb.br//images/autores/pedro2018a.jpg"/>
                  </div>
                
                  <div class="titulo-autor">
                    <span class="chapeuartigo">
                      25/09/2018                    </span>
                    <h5 class="titulo_artigo">
                      <a target="_blanck" href="https://noticias.unb.br//artigos-main/2518-alerta-sobre-os-preparativos-para-a-eleicao-de-2018" itemprop="url">
                        <span itemprop="name">
							Alerta sobre os preparativos para a eleição de 2018                        </span>
                      
                      </a>
                      
                    </h5>
                    <span class="nomeautor">Pedro Antonio Dourado de Rezende¹</span>
                  </div>
                
                <div class="clearfix"></div>
              </div>
            </div>               <div class="itemlastnews">
              <div class="itemlastnews-inner artigo-item">
                
                  <div class="boxautor">
                    <img class="imgautorartigo" src="https://noticias.unb.br//images/autores/Prof_Marcia_Abrahao.jpg"/>
                  </div>
                
                  <div class="titulo-autor">
                    <span class="chapeuartigo">
                      24/09/2018                    </span>
                    <h5 class="titulo_artigo">
                      <a target="_blanck" href="https://noticias.unb.br//artigos-main/2512-o-direito-a-universidade" itemprop="url">
                        <span itemprop="name">
							O direito à universidade                        </span>
                      
                      </a>
                      
                    </h5>
                    <span class="nomeautor">Márcia Abrahão¹</span>
                  </div>
                
                <div class="clearfix"></div>
              </div>
            </div>               <div class="itemlastnews">
              <div class="itemlastnews-inner artigo-item">
                
                  <div class="boxautor">
                    <img class="imgautorartigo" src="https://noticias.unb.br//images/autores/Ileno-Izdio-GIPSI---10ago2012---Paulo-Castro-79.jpg"/>
                  </div>
                
                  <div class="titulo-autor">
                    <span class="chapeuartigo">
                      13/09/2018                    </span>
                    <h5 class="titulo_artigo">
                      <a target="_blanck" href="https://noticias.unb.br//artigos-main/2496-vamos-falar-sobre-suicidio-nas-universidades-e-na-vida-sem-mistificacoes-ou-manipulacoes-mas-com-cuidado-e-delicadeza" itemprop="url">
                        <span itemprop="name">
							Vamos falar sobre suicídio nas universidades (e na vida)...                        </span>
                      
                      </a>
                      
                    </h5>
                    <span class="nomeautor">Ileno Izídio da Costa¹</span>
                  </div>
                
                <div class="clearfix"></div>
              </div>
            </div>          </div> 
      </div>
          
    
          <style>
            .boxautor img{
              width: 70px; /*75*/
              float:left;
              margin-right: 5px;
            }
            .titulo_artigo{
              margin: 0px !important;
              height: 30px;
              overflow: hidden;
            }
            .artigo-item{
              margin-bottom: 8px; /*10 */
            }
          </style>

    
  </div>
  <input type="radio" name="tabs" class="tabs" id="clipping" value="clipping">
  <label for="clipping" style="margin-left:3px">UnB NA MÍDIA</label>
  <div>
     <div class="chapeu-data">04/10/2018 11:30 </div><h5 class="cliping_item"><a target="_blank" href="http://linearc.com.br/unb?n=53356888">Referência da história contemporânea, Constituição completa 30 an ...</a></h5><div class="chapeu-data">04/10/2018 11:24 </div><h5 class="cliping_item"><a target="_blank" href="http://linearc.com.br/unb?n=53355506">Referência da história contemporânea, Constituição completa 30 an ...</a></h5><div class="chapeu-data">04/10/2018 11:24 </div><h5 class="cliping_item"><a target="_blank" href="http://linearc.com.br/unb?n=53355507">Referência da história contemporânea, Constituição completa 30 an ...</a></h5><div class="chapeu-data">04/10/2018 11:20 </div><h5 class="cliping_item"><a target="_blank" href="http://linearc.com.br/unb?n=53355115">Referência da história contemporânea, Constituição completa 30 an ...</a></h5><div class="chapeu-data">04/10/2018 10:57 </div><h5 class="cliping_item"><a target="_blank" href="http://linearc.com.br/unb?n=53355471">UFBA é considerada uma das dez melhores universidades brasileiras pel ...</a></h5>          

    
  </div>
</div>
<div class="carousel-footer">

           <div class="controles-carousel pull-left">
               <a class="carousel-control-multi left" href="#carousel-178" data-slide="prev">&nbsp;</a>

              <a class="carousel-control-multi right" href="#carousel-178" data-slide="next">&nbsp;</a>
          </div>

                <a class="link-categoria pull-right" target="_blanck" id="mais_artigo_clipping" href="http://noticias.unb.br/artigos-main" >
                        <span>+</span>
                </a>

          <div class="clearfix"></div>
      </div>
<script>
        
  $("#ultimas").click(function() {
    jQuery("#mais_artigo_clipping").attr('href', 'http://noticias.unb.br/artigos-main');
  });
  $("#artigos").click(function() {
    jQuery("#mais_artigo_clipping").attr('href', 'http://www.noticias.unb.br/artigos-main');
  });
  $("#clipping").click(function() {
    jQuery("#mais_artigo_clipping").attr('href', 'http://noticias.unb.br/clipping');
  });

  
</script>

		</div>
	
					<div id="system-message-container">
	</div>

					<div class="blog-featured" itemscope itemtype="https://schema.org/Blog">




</div>
					
					<!-- End Content -->
				</main>
									<!-- Begin Sidebar -->
					<div id="sidebar" class="side span4">
						<div class="sidebar-nav">
									<div class="moduletable menu-acesso-rapido">
							<h4>ACESSO RÁPIDO</h4>
						<ul class="nav menu"style="position:relative;z-index:3">
<li class="item-742"><a href="https://matriculaweb.unb.br/" target="_blank" ><img src="/images/icones/acesso_rapido/icon_matriculaweb.png" alt="Matricula Web" /><span class="image-title">Matricula Web</span> </a></li><li class="item-743"><a href="https://aprender.unb.br/" target="_blank" ><img src="/images/icones/acesso_rapido/icon_aprenderunb.png" alt="Aprender UnB" /><span class="image-title">Aprender UnB</span> </a></li><li class="item-744"><a href="https://www.sigraweb.unb.br/SigraWeb/Fronteira/paginaajudalogin.htm" target="_blank" ><img src="/images/icones/acesso_rapido/icon_mencaoweb.png" alt="Menção Web" /><span class="image-title">Menção Web</span> </a></li><li class="item-745"><a href="http://www.saa.unb.br/calendarios" target="_blank" ><img src="/images/icones/acesso_rapido/icon_calendario.png" alt="Calendário Acadêmico" /><span class="image-title">Calendário Acadêmico</span> </a></li><li class="item-746"><a href="http://proic.unb.br" target="_blank" ><img src="/images/icones/acesso_rapido/icon_iniciacaocientifica.png" alt="Iniciação Científica" /><span class="image-title">Iniciação Científica</span> </a></li><li c
2000
lass="item-747"><a href="http://www.dds.dac.unb.br/" target="_blank" ><img src="/images/icones/acesso_rapido/icon_assitenciaestudantil.png" alt="Assistência Estudantil" /><span class="image-title">Assistência Estudantil</span> </a></li><li class="item-748"><a href="http://www.dex.unb.br/" target="_blank" ><img src="/images/icones/acesso_rapido/icon_extensao.png" alt="Extensão" /><span class="image-title">Extensão</span> </a></li><li class="item-759"><a href="https://servicos.unb.br/publico/#/validardiploma" target="_blank" ><img src="/images/icones/acesso_rapido/icon_diplomadigital.png" alt="Diploma Digital" /><span class="image-title">Diploma Digital</span> </a></li><li class="item-749"><a href="http://www.unb.br/graduacao?menu=439" target="_blank" ><img src="/images/icones/acesso_rapido/icon_graduacao.png" alt="Graduação" /><span class="image-title">Graduação</span> </a></li><li class="item-750"><a href="http://www.unb.br/pos-graduacao?menu=440" target="_blank" ><img src="/images/icones/acesso_rapido/icon_posgraduacao.png" alt="Pós-Graduação" /><span class="image-title">Pós-Graduação</span> </a></li><li class="item-751"><a href="http://unb.br/graduacao2/formas-de-ingresso?menu=434" target="_blank" ><img src="/images/icones/acesso_rapido/icon_ingresso.png" alt="Formas de Ingresso" /><span class="image-title">Formas de Ingresso</span> </a></li><li class="item-752"><a href="http://www.bce.unb.br" target="_blank" ><img src="/images/icones/acesso_rapido/icon_biblioteca.png" alt="Biblioteca Central" /><span class="image-title">Biblioteca Central</span> </a></li><li class="item-753"><a href="http://www.unb.br/documentos?menu=475" target="_blank" ><img src="/images/icones/acesso_rapido/icon_documentos.png" alt="Acesso à Informação" /><span class="image-title">Acesso à Informação</span> </a></li><li class="item-754"><a href="http://www.marca.unb.br" target="_blank" ><img src="/images/icones/acesso_rapido/icon_marcaunb.png" alt="Marca UnB" /><span class="image-title">Marca UnB</span> </a></li></ul>
		</div>
	
						</div>
					</div>
					<!-- End Sidebar -->
								
			</div>

      <div class="row-fluid destaques">
                 </div>
 	 </div>
								<div class="row-fluid">
				<div class="base2">
					<div class="base-inner container">
								<div class="moduletable  moduletable videos streming-unb">
							<h3>UnB TV</h3>
						<div class="bannergroup  moduletable videos streming-unb">

	<div class="banneritem">
										<object width='300' height='300' id='UnBTVPlayer' name='UnBTVPlayer' type='application/x-shockwave-flash'
        classid='clsid:d27cdb6e-ae6d-11cf-96b8-444553540000' >
                <param name='movie' value='http://164.41.20.15/swfs/swfs.swf' />
                <param name='quality' value='high' />
                <param name='bgcolor' value='#000000' />
                <param name='allowfullscreen' value='true' />
                <param name='flashvars' value= '&src=rtmp://164.41.20.15/live/unbtv&autoHideControlBar=true&streamType=live&autoPlay=true'/>
        <embed class="streaming" src='http://164.41.20.15/swfs/swfs.swf' width='560' height='300' height='199' id='UnBTVPlayer' quality='high' bgcolor='#000000' name='UnBTVPlayer' allowfullscreen='true'
                pluginspage='http://www.adobe.com/go/getflashplayer' flashvars='&src=rtmp://164.41.20.15/live/unbtv&autoHideControlBar=true&streamType=live&autoPlay=true'
                type='application/x-shockwave-flash'>
        </embed>
</object>				<div class="clr"></div>
	</div>

</div>
		</div>
			<div class="moduletable  menu-leia-mais span4">
							<h3>Saiba Mais</h3>
						<ul class="nav menu"style="position:relative;z-index:3">
<li class="item-680"><a href="/menu-agenda-reitora" >Agenda da Reitora</a></li><li class="item-682"><a href="http://www.editora.unb.br/" target="_blank" >Editora UnB</a></li><li class="item-755"><a href="http://www.ru.unb.br/index.php/cardapio" target="_blank" >Cardápio RU</a></li><li class="item-681"><a href="http://unb.br/servicos/fale-conosco" >Fale Conosco</a></li></ul>
		</div>
			<div class="moduletable  menu-links-uteis span4">
						<ul class="nav menu"style="position:relative;z-index:3">
<li class="item-678"><a href="http://www.portalsei.unb.br" target="_blank" ><img src="/images/sei/logoSei_new.jpg" alt="SEI - Processo Eletrônico" /></a></li><li class="item-679"><a href="https://unbalerta.unb.br/" target="_blank" ><img src="/images/Logotipos/logoUnBAlerta.jpg" alt="UnBAlerta" /></a></li></ul>
		</div>
	
					</div>
				</div>
			</div>
		    <!--<style>
  
       a:hover {
         color:#fff;
         
      }</style>-->
	<!-- Footer --> 
	<footer class="footer" role="contentinfo">
		<!--<div class="footer-inner">
							<div class="menu-footer container">
					
				</div>
						<div class="clearfix"></div>
			<hr />
			
			<div class="creditos text-center container">
				<p>
					<em>Campus</em> Universitário Darcy Ribeiro, Brasília-DF | CEP 70910-900 | telefone geral 55 61 3107 3300 <br />
					Copyright &copy; 2018 Universidade de Brasília. Todos os direitos reservados.
				</p>
			</div>
		</div>-->

       <link type="text/css" href="https://web.unb.br/templates/compartilhado/css/template.css" rel="stylesheet">
  	<footer class="footer" role="contentinfo">
	<div class="footer-inner">
		<div class="menu-footer container">
  
<!-- <footer class="footer" role="contentinfo">
	<div class="footer-inner">
		<div class="menu-footer container"> -->
			<ul class="nav menu">
			<li class="item-113 divider deeper parent"><span class="separator">
	Institucional</span>
<ul class="nav-child unstyled small"><li class="item-114"><a href="http://www.unb.br/institucional" >Sobre a UnB</a></li><li class="item-221"><a href="http://www.dpo.unb.br/dados_institucional.php" >Números</a></li><li class="item-222"><a href="http://www.unb.br/campi?menu=424" >Conheça os campi</a></li><li class="item-223"><a href="http://www.unb.br/servicos/transporte" >Como chegar</a></li><li class="item-224"><a href="http://www.unb.br/images/Noticias/2016/Documentos/regimento_estatuto_unb.pdf" >Estatuto e Regimento</a></li><li class="item-257"><a href="http://www.unb.br/images/Noticias/2016/Documentos/Carta_Cidadao.pdf?menu=475" >Carta de serviços</a></li></ul></li><li class="item-259 divider deeper parent"><span class="separator">
	Unidades acadêmicas</span>
<ul class="nav-child unstyled small"><li class="item-260"><a href="http://www.unb.br/estrutura-administrativa/centros?menu=425" >Centros</a></li><li class="item-261"><a href="http://www.unb.br/unidades-academicas/faculdades" >Faculdades</a></li><li class="item-262"><a href="http://www.unb.br/unidades-academicas/institutos" >Institutos</a></li><li class="item-263"><a href="http://www.unb.br/unidades-academicas/laboratorios" >Laboratórios</a></li><li class="item-264"><a href="http://www.unb.br/unidades-academicas/nucleos" >Núcleos</a></li><li class="item-277"><a href="http://www.fal.unb.br/" >Fazenda Água Limpa</a></li></ul></li><li class="item-265 divider deeper parent"><span class="separator">
	Graduação</span>
<ul class="nav-child unstyled small"><li class="item-266"><a href="http://www.unb.br/graduacao/cursos-presenciais?menu=439" >Cursos presenciais</a></li><li class="item-267"><a href="http://www.unb.br/graduacao/curso-a-distancia?menu=439" >Cursos a distância</a></li><li class="item-268"><a href="http://www.unb.br/graduacao2/formas-de-ingresso?menu=434" >Formas de admissão</a></li><li class="item-269"><a href="http://www.unb2.unb.br/administracao/diretorias/dds/assistenciaestudantil/" target="_blank" >Assistência estudantil</a></li><li class="item-270"><a href="http://www.unb.br/oportunidades/estagio?menu=456" >Estágio</a></li><li class="item-271"><a href="http://www.unb.br/aluno/ex-aluno" >Ex-aluno</a></li><li class="item-272"><a href="https://matriculaweb.unb.br/" target="_blank" >Matrícula Web</a></li></ul></li><li class="item-128 divider deeper parent"><span class="separator">
	Pós-graduação</span>
<ul class="nav-child unstyled small"><li class="item-130"><a href="https://matriculaweb.unb.br/posgraduacao/default.aspx" target="_blank" >Mestr
1000
ado e doutorado</a></li><li class="item-129"><a href="http://www.unb2.unb.br/posgraduacao/lato_sensu/cursos.php?menu=440" target="_blank" >Especialização</a></li><li class="item-131"><a href="http://www.unb.br/atendimento?menu=471" >Apoio ao aluno</a></li><li class="item-132"><a href="http://dpp.unb.br/index.php?option=com_phocadownload&amp;view=category&amp;id=101&amp;Itemid=419" target="_blank" >Legislação</a></li><li class="item-133"><a href="http://www.saa.unb.br/revalidacao-diploma" target="_blank" >Revalidação de diploma</a></li><li class="item-134"><a href="http://dpp.unb.br/index.php?option=com_content&amp;view=article&amp;id=451&amp;Itemid=327" target="_blank" >Pesquisa</a></li><li class="item-135"><a href="http://dpp.unb.br/index.php?option=com_content&amp;view=article&amp;id=511&amp;Itemid=420" target="_blank" >Coordenadores</a></li></ul></li><li class="item-122 divider deeper parent"><span class="separator">
	Outras unidades</span>
<ul class="nav-child unstyled small"><li class="item-273"><a href="http://www.bce.unb.br/" >Biblioteca Central</a></li><li class="item-123"><a href="http://www.cpd.unb.br" >Centro de Informática</a></li><li class="item-124"><a href="http://www.editora.unb.br/" >Editora UnB</a></li><li class="item-138"><a href="http://www.ebserh.gov.br/web/hub-unb" >Hospital Universitário</a></li><li class="item-142"><a href="http://www.arquivocentral.unb.br/" >Arquivo Central</a></li><li class="item-274"><a href="http://www.int.unb.br/" >Assuntos Internacionais</a></li><li class="item-275"><a href="http://www.cdt.unb.br/" >Desenvolvimento Tecnológico</a></li><li class="item-278"><a href="http://www.saa.unb.br/" >Administração Acadêmica</a></li><li class="item-279"><a href="http://www.cespe.unb.br/" target="_blank" >Cespe/Cebraspe</a></li></ul></li><li class="item-280 divider deeper parent"><span class="separator">
	Administração</span>
<ul class="nav-child unstyled small"><li class="item-284"><a href="http://www.unb.br/estrutura-administrativa/conselhos?menu=425" >Conselhos e câmaras</a></li><li class="item-281"><a href="http://www.unb.br/estrutura-administrativa/reitoria?menu=425" >Reitoria</a></li><li class="item-282"><a href="http://www.unb.br/estrutura-administrativa/vice-reitoria?menu=425" >Vice-Reitoria</a></li><li class="item-283"><a href="http://www.unb.br/estrutura-administrativa/decanatos?menu=425" >Decanatos</a></li><li class="item-285"><a href="http://www.prc.unb.br/Novo/index.php" >Prefeitura do Campus</a></li><li class="item-286"><a href="http://www.unb2.unb.br/administracao/procuradoria_juridica/index.php" target="_blank" >Procuradoria Jurídica</a></li><li class="item-287"><a href="http://www.unb2.unb.br/administracao/auditoria_interna" target="_blank" >Auditoria</a></li><li class="item-146"><a href="http://www.comissaodeetica.unb.br" target="_blank" >Comissão de Ética</a></li></ul></li><li class="item-173 divider deeper parent"><span class="separator">
	Comunicação</span>
<ul class="nav-child unstyled small"><li class="item-174"><a href="http://www.noticias.unb.br/" >Notícias</a></li><li class="item-175"><a href="http://www.noticias.unb.br/atender" >Secom</a></li><li class="item-225"><a href="http://www.noticias.unb.br/component/agenda/agendas" >UnB Agenda</a></li><li class="item-289"><a href="http://www.unbtv.unb.br/" >UnBTV</a></li><li class="item-290"><a href="http://www.noticias.unb.br/unb-hoje" >UnB Hoje</a></li><li class="item-291"><a href="http://www.unb.br/comunidade/nossos-pesquisadores" target="_blank" >Nossos pesquisadores</a></li><li class="item-292"><a href="http://cerimonial.unb.br/" target="_blank" >Cerimonial</a></li><li class="item-293"><a href="http://www.marca.unb.br" >Marca UnB</a></li></ul></li><li class="item-143 divider deeper parent"><span class="separator">
	Transparência</span>
<ul class="nav-child unstyled small"><li class="item-144"><a href="http://www.unb.br/documentos/transparencia-unb?menu=475" >Acesso à Informação</a></li><li class="item-295"><a href="http://www.portaldatransparencia.gov.br/" target="_blank" >Transparência p?
e0a
?blica</a></li><li class="item-145"><a href="http://www.ouvidoria.unb.br/" >Ouvidoria UnB</a></li></ul></li><li class="item-226 divider deeper parent"><span class="separator">
	Servidor</span>
<ul class="nav-child unstyled small"><li class="item-231"><a href="http://www.dgp.unb.br/docente" target="_blank" >Docente</a></li><li class="item-230"><a href="https://www.sigraweb.unb.br/SigraWeb/Fronteira/paginaajudalogin.htm" target="_blank" >Menção Web</a></li><li class="item-137"><a href="http://dgp.unb.br/concursos/tecnico-administrativo" target="_blank" >Técnico</a></li><li class="item-227"><a href="http://www.dgp.unb.br/guia-do-servidor" target="_blank" >Guia</a></li><li class="item-140"><a href="http://www.unb.br/servidor/sindicatos-e-associacoes" >Sindicatos e associações</a></li></ul></li><li class="item-296 divider deeper parent"><span class="separator">
	Links rápidos</span>
<ul class="nav-child unstyled small"><li class="item-141"><a href="http://www-periodicos-capes-gov-br.ez54.periodicos.capes.gov.br/index.php?option=com_phome" target="_blank" >Periódicos Capes</a></li><li class="item-139"><a href="http://www.sgp.unb.br/locacao-de-imoveis-residenciais" target="_blank" >Imóveis UnB</a></li><li class="item-298"><a href="http://www.unbfuturo.unb.br/" target="_blank" >UnB Futuro</a></li><li class="item-299"><a href="http://www.unbidiomas.unb.br/" target="_blank" >UnB Idiomas</a></li><li class="item-220"><a href="http://www.sistemas.unb.br/" target="_blank" >Sistemas</a></li><li class="item-300"><a href="http://www.unb2.unb.br/" target="_blank" >Acesse o portal antigo</a></li></ul></li></ul>
<!-- 		</div>
<div class="clearfix"></div>
<hr>
<div class="creditos text-center container">
	<p>
		<em>Campus</em>
		Universitário Darcy Ribeiro, Brasília-DF | CEP 70910-900 | telefone geral 55 61 3107 3300
		<br>
		Copyright © 2015 Universidade de Brasília. Todos os direitos reservados.
	</p>
</div>
	</div>
</footer> -->

  		</div>
		<div class="clearfix"></div>
		<hr>
		<div class="creditos text-center container">
			<p>
				<em>Campus</em>
				Universitário Darcy Ribeiro, Brasília-DF | CEP 70910-900 |
 <a href="https://www.unb.br/images/mprazer.pdf">Telefones UnB </a>
				<br>
				Copyright © 2016 Universidade de Brasília. Todos os direitos reservados.
			</p>
		</div>
	</div>
	</footer>

  

	
    </footer>
	

<div class="custom"  >
	<script>// <![CDATA[
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-85991647-1', 'auto');
  ga('send', 'pageview');
// ]]></script></div>
<a href='http://www.extrawatch.com'>&nbsp;</a><script type="text/javascript" id="extraWatchAgent">

		var extraWatchAjaxLink = "%2F%3Foption%3Dcom_ajax%26module%3Dextrawatch_agent%26format%3Draw%26origin%3Dfrontend%26ewToken%3D7000ad69a073a5a97a973831091908294ba45279%26task%3Dajax%26action%3D";

		var extraWatchLiveSite = "%2F";

		var extraWatchEnv = "ExtraWatchJoomlaEnv";

        (function() {

        var ew = document.createElement('script');
        ew.type = 'text/javascript'; ew.async = true;

        ew.src = "/components/com_extrawatch/js/agent.js?env=ExtraWatchJoomlaEnv&rand="+ Math.random();
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ew, s);

        })();

        </script>
        
</body>
</html>

0


```

(d) [fga.unb.br](fga.unb.br)

```HTML
HTTP/1.1 301 Moved Permanently
Server: nginx/1.6.2
Date: Sat, 21 Apr 2019 16:18:11 GMT
Content-Type: text/html
Content-Length: 184
Connection: keep-alive
Location: https://fga.unb.br/
Strict-Transport-Security: max-age=15768000

<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.6.2</center>
</body>
</html>

```

Comente os resultados obtidos para cada página, em termos das respostas HTTP e HTML obtidas.