import discord 
import random 
import asyncio
import json 
from random import choice
#discord-ui
from discord.ext import commands, tasks
from discord import ui
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True



client = commands.Bot(command_prefix=("!"), intents=intents)

#--- Cose per Hosting (Non toccare fiocco)

h_id = [1181630796759564358, 814224911005646888]
statuschannel = 1210908476868395058




is_me = commands.check(lambda ctx: ctx.author.id in h_id)

import json 

with open("config.json") as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print("Errore in config.json")
        print(e)
        exit(1)


@client.event
async def on_ready():
	print(f"Bot logged into {client.user}.")
	channel = client.get_channel(statuschannel)
	embed = discord.Embed(title=f"**Bot - Online 🟢 - Start Event**", color=discord.Color.green())
	await channel.send(embed=embed)



@client.command()
@is_me
async def update(ctx):
	embed = discord.Embed(title="Reloading system...", color=0x2c2f33)
	embed.set_image(url="https://support.discord.com/hc/en-us/article_attachments/206303208/eJwVyksOwiAQANC7sJfp8Ke7Lt15A0MoUpJWGmZcGe-ubl_eW7zGLmaxMZ80A6yNch-rJO4j1SJr73Uv6Wwkcz8gMae8HeXJBOjC5NEap42dokUX_4SotI8GVfBaYYDldr3n3y_jomRtD_H5ArCeI9g.zGz1JSL-9DXgpkX_SkmMDM8NWGg.gif")
	embed.add_field(name = ':globe_with_meridians: **Ping**', value = f'{round(client.latency * 1000)}ms')
	await ctx.send(embed=embed, delete_after=4)
	await asyncio.sleep(5)
	channel = client.get_channel(statuschannel)
	embed = discord.Embed(title=f"**Bot - Riavvio 🟡 - Update**", color=discord.Color.gold())
	await channel.send(embed=embed)
	exit(1)


#---




    

@client.tree.command(name="comandi", description = "Comando aiuto")
async def comandi(interaction: discord.Interaction):
    nome_embed7 = discord.Embed(title="**Lista comandi**", description="/comandi  mostra questa lista\n!bestemmia  farà dire al bot una bestemmia\n/bestemmione seleziona una bestemmia dal database\n/bestemmia del giorno seleziona la bestemmia più adatta a ogni giornata\n/modo-di-dire seleziona un modo di dire\n/urbex-equipaggiamento elenca gli oggetti da portare in esplorazione\n/abbigliamento-urbex ti disce gli abiti da indossare per andare in esplorazione\nurbex ti spiegha cosa sono gli urbex/ban banna un membro\n/sban sbanna un membro\n/espelli espelli un membro", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed7)
    #in lista comandi
    #funzionante



@client.tree.command(name="bestemmione", description="con questo comando sparero un bestemmione")
async def bestemmione(interaction: discord.Interaction):
    nome_embed3 = discord.Embed(title="**una bestemmia al giorno toglie il medico di torno**", description="**stò selezionando la bestemmia...**",color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed3)
    await asyncio.sleep(8)
    lista = ['Dio spacciatore','Dio affettato','Dio salume','Dio salumiere','Dio venditore di pentole','Dio sbadilato','Dio touch','Dio pistacchio','Dio ectoplasma','Dio pittura fresca','Dio lucchetto','Dio cinescopio','Dio intonaco','Dio armadietto','Dio memoria volatile','Dio intestino','Dio intestinale','Dio pastorizzato','Dio pressurizzato','Dio congelato','Dio gelataio','Dio estradato','Dio mandorla','Dio mandorlato','Dio mandorloso','Dio merdoso','Dio segaiolo','Dio colorato','Dio strafanto','Dio inghigliottinato','Dio cromosoma','Dio interrogato','Dio sgranocchioso','Dio croccante','Dio leggero','Dio impastato','Dio telecinesi','Dio telecinetico','Dio plasticoso','Dio plasticaccia','Dio murato','Dio esonerato','Dio tastiera','Dio intralciatore','Dio giocatore accanito di Call of Duty','Dio nerd','Dio plantigrado','Dio orso','Dio peluche','Dio Viggiani','Dio vetraio','Dio vietato','Dio retrattile','Dio ammuffito','Dio palla di neve','Dio fungo','Dio scolapasta','Dio mineralizzato','Dio stratificato','Dio appesantito','Dio sequoia','Dio narcotico','Dio narcotrafficante','Dio assortito','Dio assortimento di colori a pastello','Dio matita colorata','Dio pastello','Dio digitale','Dio digitalizzato','Dio digitalizzatore','Dio analogico','Dio spettrometro','Dio mefisto','Dio Minecraft','Dio esploso','Dio tavolino','Dio vittima di bullismo','Dio spaghetto','Dio spaghettoso','Dio prodigioso','Dio prodigioso spaghetto volante','Dio volante','Dio svolazzante','Dio fachiro','Dio poetico','Dio pepe','Dio ethernet','Dio LCD','Dio a cristalli liquidi','Dio lettore CD','Dio DJ','Dio produttore di musica elettronica','Dio gelsomino','Dio magnetico inciampato nella valle dei chiodi arrugginiti','Dio vaccinato','Dio radioattivo','Dio reattore nucleare','Dio comodo','Dio soffice','Dio cremoso','Dio roccia','Dio salmone','Dio caffeina','Dio ananas','Dio audiofilo','Dio box','Dio industrializzato','Dio episcopato','Dio episcopale','Dio cinescopio','Dio portatile','Dio veleno','Dio serpente','Dio sdentato','Dio luccicoso','Dio freddo','Dio caldo ','Dio tiepido','Dio frullatore','Dio frullato','Dio riflesso','Dio riflettore','Dio scomodo','Dio lampadina','Dio spaiato','Dio polare','Dio apolare','Dio ionizzato','Dio ionizzante','Dio ionizzatore','Dio ionico','Dio catione','Dio anione','Dio catodo ','Dio anodo','Dio volante','Dio pilota','Dio terrorista','Dio incelofanato','Dio kamikaze','Dio luminoso','Dio meteora','Dio meteorite','Dio giochicchioso','Dio amperometro','Dio ciabatta','Dio scarpa','Dio cellophane','Dio retromarcia','Dio retrovisore','Dio otaria','Dio spettrometro','Dio oscillatore','Dio oscillato','Dio nebbia','Dio nebbioso','Dio svaligiato','Dio iperbato','Dio pubblicitario','Dio bicchiere','Dio squamoso','Dio monouso','Dio platano ','Dio rospo','Dio tenebroso','Dio cactus','Dio topo','Dio pantera','Dio pantegana','Dio vaporetto','Dio marciapiede','Dio pettinatore di pelati','Dio davoroso','Dio sanatore di debiti','Dio silicone','Dio siliconato','Dio stella marina','Dio psichedeligo','Dio anisotopico','Dio lastra','Dio segnalibro','Dio microfono','Dio microfonico','Dio scaricato','Dio sputacchiera','Dio pachiderma','Dio magnete','Dio magnetico','Dio scalzo nella valle dei chiodi arrugginiti','Dio scarico','Dio aspirapolvere','Dio bastone','Dio robotico','Dio alternatore','Dio evidenziato','Dio verde','Dio appendiabiti','Dio temperato','Dio spazzacamino','Dio insipido','Dio millepiedi','Dio idrante','Dio kraphen','Dio ninfea','Dio cicala','Dio stilizzato','Dio ventilato','Dio ventilatore','Dio ripartitore','Dio ingarbui ','Dio alieno','Dio ripieno','Dio alogeno','Dio canguro nella valle dei tetti bassi','Dio setola','Dio frittella','Dio raviolo','Dio granchio','Dio castoro','Dio Parmalat','Dio Squarepants','Dio sbatushe','Dio nudo nella valle dei raggi gamma','Dio petaloso','Dio spargisale','Dio paravento','Dio sandalo','Dio assaggiatore di vini scaduti','Dio alfiere','Dio fantino','Dio cornflakes','Dio alcalino','Dio tubolare','Dio tuboliforme','Dio elicoeidale','Dio aeriforme','Dio spasmodico','Dio epilettico','Dio dissipato','Dio trasduttore','Dio centrino','Dio transatlantico','Dio a reazione','Dio stocafisso a reazione','Dio piezoelettrico','Dio carciofo','Dio amalfitano','Dio ibis','Dio dromedario','Dio tavoletta','Dio flauto','Dio pecorella smarrita','Dio frattabbacchio','Dio crostatina','Dio effervescente ','Dio frizzante ','Dio rinoceronte ','Dio pony','Dio unicorno','Dio baguette ','Dio giuggiola','Dio tarassaco','Dio scataron','Dio pomata','Dio menarca','Dio cardine','Dio sommozzatore','Dio cantastorie ','Dio meccanico ','Dio saponetta ','Dio solubile','Dio istamina','Dio carib ','Dio transenna','Dio criceto alcolista','Dio aborigeno','Dio libellula','Dio terapeuta','Dio koala','Dio narcisista','Dio tabasco','Dio igloo','Dio supercar','Dio rapa','Dio dentifricio','Dio cactus ','Dio frullatore ','Dio assorbito','Dio cordless ','Dio calindropo','Dio tassista ','Dio scatenato ','Dio lampone','Dio lucertola ','Dio inscotchettato','Dio carota','Dio rinsecchito','Dio termorestringente','Dio fenoftaleina','Dio anglosassone ','Dio in agrodolce','Dio focaccella','Dio abbrustolito ','Dio coriaceo','Dio pero','Dio asparago','Dio lacrimogeno','Dio anoressico','Dio mestolo ','Dio levriero ','Dio lamantino','Dio furetto','Dio merovingio','Dio proctologo','Dio pellicano ','Dio slovacco','Dio analfabeta nella valle degli scrittori','Dio aeroplano nel triangolo delle bermuda','Dio calamita nella valle dei rifiuti plastici','Dio scalatore nella valle delle pianure','Dio surfista nel deserto del Sahara      ','Dio ciambella senza buco','Dio ciclista nella valle degli orsi sciatori ','Dio puledro','Dio saliva','Dio saliscendi ','Dio aracnide','Dio lampreda','Dio platano','Dio jeep','Dio poliglotta','Dio piallatrice','Dio svittol','Dio lampadina','Dio fantabosco','Dio lavello','Dio intarsiatore','Dio intarsiato','Dio tibetano','Dio cavalca via','','Dio barbagianni','Dio collaudatore di carote','Dio carotatore di collaudi','Dio stupratore di feti abortiti','Dio cancaro','Dio cancro','Dio accesoriato','Dio stanatore di topi','Dio inalatore di gas tossici','Dio str del','Dio tornio CNC','Dio riparatore di iPhone','Dio suricato ','Dio accrocchio','Dio digitale terrestre','Dio sintonizzato','Dio sintonizzatore','Dio sintetizzatore','Dio telecomandato','Dio aratro','Dio lavoratore cinese sottopagato','Dio minatore','Dio interpretato male in un film','Dio Android','Dio tablet','Dio stampante 3D','Dio kebab','Dio kebabbaro','Dio in monociclo','Dio marsupio','Dio marsupiale','Dio newyorkese','Dio velocipede','Dio sulla sedia elettrica','Dio condannato a morte','Dio caminetto','Dio lampadina','Dio palla','Dio scoreggiatore','Dio spalatore di merda','Dio luce','Dio morto','Dio cancello','Dio pupilla','Dio sperma','Dio assicuratore di vasi da notte','Dio fungo','Dio stupido','Dio fotografia','Dio presa elettrica','Dio folgorato','Dio impest ','Dio vite spanata','Dio dal culo spanato','Dio spanato','Dio panna','Dio zuccheroso','Dio abbraccia alberi','Dio lebbroso','Dio esattore','Dio formica','Dio microfono','Dio pavimento sporco','Dio legnoso','Dio Xbox','Dio barista','Dio stupro','Dio cartaceo','Dio alluminio anodizzato']
    choice = random.choice(lista)
    nome_embed4 = discord.Embed(title=f"la bestemmia è: {choice}!",color=discord.Color.green())
    await interaction.edit_original_response(embed=nome_embed4)
    #mettere il database 
    #in lista comandi
    #funzionante



@client.tree.command(name="bestemmia-del-giorno", description="con questo comando selezionero la bestemmia del giorno")
async def bestemmiadelgiorno(interaction: discord.Interaction):
    nome_embed = discord.Embed(title="**bestemmia del giorno**", description="stò selezionando la bestemmia del giorno...", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed)
    await asyncio.sleep(8)
    lista = ['Dio spacciatore','Dio affettato','Dio salume','Dio salumiere','Dio venditore di pentole','Dio sbadilato','Dio touch','Dio pistacchio','Dio ectoplasma','Dio pittura fresca','Dio lucchetto','Dio cinescopio','Dio intonaco','Dio armadietto','Dio memoria volatile','Dio intestino','Dio intestinale','Dio pastorizzato','Dio pressurizzato','Dio congelato','Dio gelataio','Dio estradato','Dio mandorla','Dio mandorlato','Dio mandorloso','Dio merdoso','Dio segaiolo','Dio colorato','Dio strafanto','Dio inghigliottinato','Dio cromosoma','Dio interrogato','Dio sgranocchioso','Dio croccante','Dio leggero','Dio impastato','Dio telecinesi','Dio telecinetico','Dio plasticoso','Dio plasticaccia','Dio murato','Dio esonerato','Dio tastiera','Dio intralciatore','Dio giocatore accanito di Call of Duty','Dio nerd','Dio plantigrado','Dio orso','Dio peluche','Dio Viggiani','Dio vetraio','Dio vietato','Dio retrattile','Dio ammuffito','Dio palla di neve','Dio fungo','Dio scolapasta','Dio mineralizzato','Dio stratificato','Dio appesantito','Dio sequoia','Dio narcotico','Dio narcotrafficante','Dio assortito','Dio assortimento di colori a pastello','Dio matita colorata','Dio pastello','Dio digitale','Dio digitalizzato','Dio digitalizzatore','Dio analogico','Dio spettrometro','Dio mefisto','Dio Minecraft','Dio esploso','Dio tavolino','Dio vittima di bullismo','Dio spaghetto','Dio spaghettoso','Dio prodigioso','Dio prodigioso spaghetto volante','Dio volante','Dio svolazzante','Dio fachiro','Dio poetico','Dio pepe','Dio ethernet','Dio LCD','Dio a cristalli liquidi','Dio lettore CD','Dio DJ','Dio produttore di musica elettronica','Dio gelsomino','Dio magnetico inciampato nella valle dei chiodi arrugginiti','Dio vaccinato','Dio radioattivo','Dio reattore nucleare','Dio comodo','Dio soffice','Dio cremoso','Dio roccia','Dio salmone','Dio caffeina','Dio ananas','Dio audiofilo','Dio box','Dio industrializzato','Dio episcopato','Dio episcopale','Dio cinescopio','Dio portatile','Dio veleno','Dio serpente','Dio sdentato','Dio luccicoso','Dio freddo','Dio caldo ','Dio tiepido','Dio frullatore','Dio frullato','Dio riflesso','Dio riflettore','Dio scomodo','Dio lampadina','Dio spaiato','Dio polare','Dio apolare','Dio ionizzato','Dio ionizzante','Dio ionizzatore','Dio ionico','Dio catione','Dio anione','Dio catodo ','Dio anodo','Dio volante','Dio pilota','Dio terrorista','Dio incelofanato','Dio kamikaze','Dio luminoso','Dio meteora','Dio meteorite','Dio giochicchioso','Dio amperometro','Dio ciabatta','Dio scarpa','Dio cellophane','Dio retromarcia','Dio retrovisore','Dio otaria','Dio spettrometro','Dio oscillatore','Dio oscillato','Dio nebbia','Dio nebbioso','Dio svaligiato','Dio iperbato','Dio pubblicitario','Dio bicchiere','Dio squamoso','Dio monouso','Dio platano ','Dio rospo','Dio tenebroso','Dio cactus','Dio topo','Dio pantera','Dio pantegana','Dio vaporetto','Dio marciapiede','Dio pettinatore di pelati','Dio davoroso','Dio sanatore di debiti','Dio silicone','Dio siliconato','Dio stella marina','Dio psichedeligo','Dio anisotopico','Dio lastra','Dio segnalibro','Dio microfono','Dio microfonico','Dio scaricato','Dio sputacchiera','Dio pachiderma','Dio magnete','Dio magnetico','Dio scalzo nella valle dei chiodi arrugginiti','Dio scarico','Dio aspirapolvere','Dio bastone','Dio robotico','Dio alternatore','Dio evidenziato','Dio verde','Dio appendiabiti','Dio temperato','Dio spazzacamino','Dio insipido','Dio millepiedi','Dio idrante','Dio kraphen','Dio ninfea','Dio cicala','Dio stilizzato','Dio ventilato','Dio ventilatore','Dio ripartitore','Dio ingarbui ','Dio alieno','Dio ripieno','Dio alogeno','Dio canguro nella valle dei tetti bassi','Dio setola','Dio frittella','Dio raviolo','Dio granchio','Dio castoro','Dio Parmalat','Dio Squarepants','Dio sbatushe','Dio nudo nella valle dei raggi gamma','Dio petaloso','Dio spargisale','Dio paravento','Dio sandalo','Dio assaggiatore di vini scaduti','Dio alfiere','Dio fantino','Dio cornflakes','Dio alcalino','Dio tubolare','Dio tuboliforme','Dio elicoeidale','Dio aeriforme','Dio spasmodico','Dio epilettico','Dio dissipato','Dio trasduttore','Dio centrino','Dio transatlantico','Dio a reazione','Dio stocafisso a reazione','Dio piezoelettrico','Dio carciofo','Dio amalfitano','Dio ibis','Dio dromedario','Dio tavoletta','Dio flauto','Dio pecorella smarrita','Dio frattabbacchio','Dio crostatina','Dio effervescente ','Dio frizzante ','Dio rinoceronte ','Dio pony','Dio unicorno','Dio baguette ','Dio giuggiola','Dio tarassaco','Dio scataron','Dio pomata','Dio menarca','Dio cardine','Dio sommozzatore','Dio cantastorie ','Dio meccanico ','Dio saponetta ','Dio solubile','Dio istamina','Dio carib ','Dio transenna','Dio criceto alcolista','Dio aborigeno','Dio libellula','Dio terapeuta','Dio koala','Dio narcisista','Dio tabasco','Dio igloo','Dio supercar','Dio rapa','Dio dentifricio','Dio cactus ','Dio frullatore ','Dio assorbito','Dio cordless ','Dio calindropo','Dio tassista ','Dio scatenato ','Dio lampone','Dio lucertola ','Dio inscotchettato','Dio carota','Dio rinsecchito','Dio termorestringente','Dio fenoftaleina','Dio anglosassone ','Dio in agrodolce','Dio focaccella','Dio abbrustolito ','Dio coriaceo','Dio pero','Dio asparago','Dio lacrimogeno','Dio anoressico','Dio mestolo ','Dio levriero ','Dio lamantino','Dio furetto','Dio merovingio','Dio proctologo','Dio pellicano ','Dio slovacco','Dio analfabeta nella valle degli scrittori','Dio aeroplano nel triangolo delle bermuda','Dio calamita nella valle dei rifiuti plastici','Dio scalatore nella valle delle pianure','Dio surfista nel deserto del Sahara      ','Dio ciambella senza buco','Dio ciclista nella valle degli orsi sciatori ','Dio puledro','Dio saliva','Dio saliscendi ','Dio aracnide','Dio lampreda','Dio platano','Dio jeep','Dio poliglotta','Dio piallatrice','Dio svittol','Dio lampadina','Dio fantabosco','Dio lavello','Dio intarsiatore','Dio intarsiato','Dio tibetano','Dio cavalca via','','Dio barbagianni','Dio collaudatore di carote','Dio carotatore di collaudi','Dio stupratore di feti abortiti','Dio cancaro','Dio cancro','Dio accesoriato','Dio stanatore di topi','Dio inalatore di gas tossici','Dio str del','Dio tornio CNC','Dio riparatore di iPhone','Dio suricato ','Dio accrocchio','Dio digitale terrestre','Dio sintonizzato','Dio sintonizzatore','Dio sintetizzatore','Dio telecomandato','Dio aratro','Dio lavoratore cinese sottopagato','Dio minatore','Dio interpretato male in un film','Dio Android','Dio tablet','Dio stampante 3D','Dio kebab','Dio kebabbaro','Dio in monociclo','Dio marsupio','Dio marsupiale','Dio newyorkese','Dio velocipede','Dio sulla sedia elettrica','Dio condannato a morte','Dio caminetto','Dio lampadina','Dio palla','Dio scoreggiatore','Dio spalatore di merda','Dio luce','Dio morto','Dio cancello','Dio pupilla','Dio sperma','Dio assicuratore di vasi da notte','Dio fungo','Dio stupido','Dio fotografia','Dio presa elettrica','Dio folgorato','Dio impest ','Dio vite spanata','Dio dal culo spanato','Dio spanato','Dio panna','Dio zuccheroso','Dio abbraccia alberi','Dio lebbroso','Dio esattore','Dio formica','Dio microfono','Dio pavimento sporco','Dio legnoso','Dio Xbox','Dio barista','Dio stupro','Dio cartaceo','Dio alluminio anodizzato']
    choice = random.choice(lista)
    nome_embed2 = discord.Embed(title=f"la bestemmia del giorno è: {choice}!",color=discord.Color.green())
    await interaction.edit_original_response(embed=nome_embed2)
    #mettere il database 
    #in lista comandi
    #funzionante



@client.tree.command(name="urbex", description="con questo comando ti spieghero chi sono gli urbex")
async def equipaggiamento(interaction: discord.Interaction):
    nome_embed5 = discord.Embed(title="**Chi sono gli urbex?**", description="Gli 'urbex', abbreviazione di 'Urban Exploration', sono un gruppo di appassionati di esplorazione urbana che si dedicano all'esplorazione di luoghi abbandonati, dismessi o inaccessibili al pubblico. Questo movimento è nato negli anni '80 ed è diventato sempre più popolare nel corso degli anni grazie alla diffusione dei social media e alla crescente curiosità nei confronti dell'architettura e della storia urbana. Gli Urbex esplorano una vasta gamma di luoghi, tra cui fabbriche abbandonate, ospedali, scuole, chiese, stazioni ferroviarie, discariche, bunker, tunnel e altro ancora. La loro motivazione principale è quella di scoprire e documentare luoghi dimenticati, preservando la memoria storica e l'architettura dietro di essi. Tuttavia, l'Urbex non riguarda solo l'esplorazione fisica dei luoghi, ma anche la fotografia e la documentazione delle loro scoperte. Molti Urbex sono appassionati fotografi e condividono le loro immagini e storie attraverso blog, forum online e social media. È importante notare che l'Urbex può comportare rischi significativi, poiché gli esploratori possono incontrare pericoli come strutture instabili, infiltrazioni d'acqua, presenza di sostanze pericolose, animali selvatici, nonché il rischio di incappare in proprietari privati o autorità che vietano l'accesso ai luoghi abbandonati. Pertanto, la sicurezza e il rispetto per l'ambiente circostante sono considerazioni fondamentali per gli Urbex. Nonostante i rischi, l'Urbex continua a crescere come movimento globale, con numerosi gruppi e comunità di appassionati che si incontrano, condividono esperienze e pianificano nuove avventure di esplorazione urbana.", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed5)
    #in lista comandi
    #funzionante


@client.tree.command(name="equipaggiamento-urbex", description="con questo comando ti elenchero gli oggetti da portare in esplorazione")
async def equipaggiamento(interaction: discord.Interaction):
    nome_embed5 = discord.Embed(title="**oggetti da portare in esplorazione**", description="Gli oggetti da portare con se in esplorazione\n\nElementi fondamentali:\ntorcia\nbatterie\ntelefono\nguanti\nacqua\nsnack energetici\nOggetti facoltativi\npassamontagna\ncoltello\ncontatore geiger\naccendino", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed5)
    #in lista comandi
    #funzionante



@client.tree.command(name="abbigliamento-urbex", description="con questo comando ti elenchero i vestiti da indossare per andare in esplorazione")
async def abbigliamento_urbex(interaction: discord.Interaction):
    nome_embed6 = discord.Embed(title="**abbigliamento**", description="Inverno\n\npantaloni lunghi\nmaglietta a maniche lunghe\nfelpa (termica o non)\ncalzini pesanti\nscarponi da montagna\n\nEstate\n\npantaloni Lunghi\nmaglietta (a maniche corte o non)\ncalzini leggeri\nscarponi da montagna\nfelpa (per la sera in caso fa freddo)", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed6)
    #in lista comandi
    #funzionante



@client.tree.command(name="proverbio", description="con questo comando ti suggerirò un proverbio")
async def proverbio(interaction: discord.Interaction):
    nome_embed10 = discord.Embed(title="**ecco un proverbio**", description="stò selezionando il proverbio...", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed10)
    await asyncio.sleep(8)
    lista = ["Chi più sa, meno crede.","Chi troppo in alto sale, al culmine cade.","Chi ha il pane non ha i denti, chi ha i denti non ha il pane.","Chi è causa del suo mal, pianga sé stesso.","Chi ben comincia è a metà dell'opera.","Chi fa da sé, fa per tre.","Chi di spada ferisce, di spada perisce.","Chi ha il pane non ha i denti.","Chi ha il capo caldo, ha i piedi freddi.","Chi ha il vino, non ha il pane.","Chi ha tempo, non aspetti tempo.","Chi ha fame, ha la rabbia.","Chi ha i denti, ha il pane.","Chi ha il diavolo addosso, la vecchiaia lo spaventa.","Chi ha la testa, non ha il pane.","Chi ha il pane, ha la bocca.","Chi ha il malanno, ha il rimedio.","Chi ha la schiena tozza, non ha la gobba.","Chi ha la casa di vetro, non tiri le pietre altrui.","Chi ha l'amante, non ha il buon giorno.","Chi ha il gatto, non ha il sorcio.","Chi ha il malanno, ha la metà della medicina.","Chi ha il cuore di pietra, non sente dolore.","Chi ha il cuore a destra, non è un mostro.","Chi ha il cuore in mano, non ha l'udito.","Chi ha il cuore grande, non ha la forza.","Chi ha il cuore tenero, non ha la forza.","Chi ha il cuore leggero, non sente dolore.","Chi ha il cuore buono, non sente dolore.","Chi ha il cuore caldo, non ha la febbre.","Chi ha il cuore in fiamme, non sente dolore.","Chi ha il cuore duro, non sente dolore.","Chi ha il cuore leggero, non ha il dolore.","Chi ha il cuore di latta, non sente dolore."]
    choice = random.choice(lista)
    nome_embed11 = discord.Embed(title=f"il proverbio è: {choice}", color=discord.Color.green())
    await interaction.edit_original_response(embed=nome_embed11)
    #in lista comandi
    #funzionante



@client.tree.command(name="ban", description="banna un membro")
async def ban(interaction: discord.Interaction, membro: discord.Member, *,motivo:str=None): 
    await membro.ban(reason=motivo)
    nome_embed = discord.Embed(title="**Ban**", description=f"{membro} **è stato bannato**", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed)
    #in lista comandi
    #funzionante



@client.tree.command(name="sban", description="sbanna un membro")
async def sban(interaction: discord.Interaction, membro:discord.User):  
    interaction.guild.unban(membro)
    nome_embed = discord.Embed(title="**Sban**", description=f"{membro} **è stato sbannato**", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed)
    #in lista comandi
    #funzionante



@client.tree.command(name="espelli", description="espelli un membro")
async def sban(interaction: discord.Interaction, membro: discord.Member, *,motivo:str=None):  
    await interaction.guild.kick(membro)
    nome_embed = discord.Embed(title="**Espulso**", description=f"{membro} **è stato espulso per {motivo}**", color=discord.Color.green())
    await interaction.response.send_message(embed=nome_embed)
    #in lista comandi
    #funzionante



@client.command()
async def autodistruzione(ctx):
    await ctx.send("processo di auto distruzione 0%")
    await ctx.send("processo di auto distruzione 10%")
    await ctx.send("processo di auto distruzione 17%")
    await asyncio.sleep(1)
    await ctx.send("processo di auto distruzione 23%")
    await ctx.send("processo di auto distruzione 29%")
    await ctx.send("processo di auto distruzione 36%")
    await asyncio.sleep(2)
    await ctx.send("processo di auto distruzione 42%")
    await ctx.send("processo di auto distruzione 54%")
    await ctx.send("processo di auto distruzione 65%")
    await asyncio.sleep(1)
    await ctx.send("processo di auto distruzione 72%")
    await ctx.send("processo di auto distruzione 78%")
    await ctx.send("processo di auto distruzione 84%")
    await asyncio.sleep(2)
    await ctx.send("processo di auto distruzione 95%")
    await ctx.send("processo di auto distruzione 100%")
    list=['Dio spacciatore','Dio affettato','Dio salume','Dio salumiere','Dio venditore di pentole','Dio sbadilato','Dio touch','Dio pistacchio','Dio ectoplasma','Dio pittura fresca','Dio lucchetto','Dio cinescopio','Dio intonaco','Dio armadietto','Dio memoria volatile','Dio intestino','Dio intestinale','Dio pastorizzato','Dio pressurizzato','Dio congelato','Dio gelataio','Dio estradato','Dio mandorla','Dio mandorlato','Dio mandorloso','Dio merdoso','Dio segaiolo','Dio colorato','Dio strafanto','Dio inghigliottinato','Dio cromosoma','Dio interrogato','Dio sgranocchioso','Dio croccante','Dio leggero','Dio impastato','Dio telecinesi','Dio telecinetico','Dio plasticoso','Dio plasticaccia','Dio murato','Dio esonerato','Dio tastiera','Dio intralciatore','Dio giocatore accanito di Call of Duty','Dio nerd','Dio plantigrado','Dio orso','Dio peluche','Dio Viggiani','Dio vetraio','Dio vietato','Dio retrattile','Dio ammuffito','Dio palla di neve','Dio fungo','Dio scolapasta','Dio mineralizzato','Dio stratificato','Dio appesantito','Dio sequoia','Dio narcotico','Dio narcotrafficante','Dio assortito','Dio assortimento di colori a pastello','Dio matita colorata','Dio pastello','Dio digitale','Dio digitalizzato','Dio digitalizzatore','Dio analogico','Dio spettrometro','Dio mefisto','Dio Minecraft','Dio esploso','Dio tavolino','Dio vittima di bullismo','Dio spaghetto','Dio spaghettoso','Dio prodigioso','Dio prodigioso spaghetto volante','Dio volante','Dio svolazzante','Dio fachiro','Dio poetico','Dio pepe','Dio ethernet','Dio LCD','Dio a cristalli liquidi','Dio lettore CD','Dio DJ','Dio produttore di musica elettronica','Dio gelsomino','Dio magnetico inciampato nella valle dei chiodi arrugginiti','Dio vaccinato','Dio radioattivo','Dio reattore nucleare','Dio comodo','Dio soffice','Dio cremoso','Dio roccia','Dio salmone','Dio caffeina','Dio ananas','Dio audiofilo','Dio box','Dio industrializzato','Dio episcopato','Dio episcopale','Dio cinescopio','Dio portatile','Dio veleno','Dio serpente','Dio sdentato','Dio luccicoso','Dio freddo','Dio caldo ','Dio tiepido','Dio frullatore','Dio frullato','Dio riflesso','Dio riflettore','Dio scomodo','Dio lampadina','Dio spaiato','Dio polare','Dio apolare','Dio ionizzato','Dio ionizzante','Dio ionizzatore','Dio ionico','Dio catione','Dio anione','Dio catodo ','Dio anodo','Dio volante','Dio pilota','Dio terrorista','Dio incelofanato','Dio kamikaze','Dio luminoso','Dio meteora','Dio meteorite','Dio giochicchioso','Dio amperometro','Dio ciabatta','Dio scarpa','Dio cellophane','Dio retromarcia','Dio retrovisore','Dio otaria','Dio spettrometro','Dio oscillatore','Dio oscillato','Dio nebbia','Dio nebbioso','Dio svaligiato','Dio iperbato','Dio pubblicitario','Dio bicchiere','Dio squamoso','Dio monouso','Dio platano ','Dio rospo','Dio tenebroso','Dio cactus','Dio topo','Dio pantera','Dio pantegana','Dio vaporetto','Dio marciapiede','Dio pettinatore di pelati','Dio davoroso','Dio sanatore di debiti','Dio silicone','Dio siliconato','Dio stella marina','Dio psichedeligo','Dio anisotopico','Dio lastra','Dio segnalibro','Dio microfono','Dio microfonico','Dio scaricato','Dio sputacchiera','Dio pachiderma','Dio magnete','Dio magnetico','Dio scalzo nella valle dei chiodi arrugginiti','Dio scarico','Dio aspirapolvere','Dio bastone','Dio robotico','Dio alternatore','Dio evidenziato','Dio verde','Dio appendiabiti','Dio temperato','Dio spazzacamino','Dio insipido','Dio millepiedi','Dio idrante','Dio kraphen','Dio ninfea','Dio cicala','Dio stilizzato','Dio ventilato','Dio ventilatore','Dio ripartitore','Dio ingarbui ','Dio alieno','Dio ripieno','Dio alogeno','Dio canguro nella valle dei tetti bassi','Dio setola','Dio frittella','Dio raviolo','Dio granchio','Dio castoro','Dio Parmalat','Dio Squarepants','Dio sbatushe','Dio nudo nella valle dei raggi gamma','Dio petaloso','Dio spargisale','Dio paravento','Dio sandalo','Dio assaggiatore di vini scaduti','Dio alfiere','Dio fantino','Dio cornflakes','Dio alcalino','Dio tubolare','Dio tuboliforme','Dio elicoeidale','Dio aeriforme','Dio spasmodico','Dio epilettico','Dio dissipato','Dio trasduttore','Dio centrino','Dio transatlantico','Dio a reazione','Dio stocafisso a reazione','Dio piezoelettrico','Dio carciofo','Dio amalfitano','Dio ibis','Dio dromedario','Dio tavoletta','Dio flauto','Dio pecorella smarrita','Dio frattabbacchio','Dio crostatina','Dio effervescente ','Dio frizzante ','Dio rinoceronte ','Dio pony','Dio unicorno','Dio baguette ','Dio giuggiola','Dio tarassaco','Dio scataron','Dio pomata','Dio menarca','Dio cardine','Dio sommozzatore','Dio cantastorie ','Dio meccanico ','Dio saponetta ','Dio solubile','Dio istamina','Dio carib ','Dio transenna','Dio criceto alcolista','Dio aborigeno','Dio libellula','Dio terapeuta','Dio koala','Dio narcisista','Dio tabasco','Dio igloo','Dio supercar','Dio rapa','Dio dentifricio','Dio cactus ','Dio frullatore ','Dio assorbito','Dio cordless ','Dio calindropo','Dio tassista ','Dio scatenato ','Dio lampone','Dio lucertola ','Dio inscotchettato','Dio carota','Dio rinsecchito','Dio termorestringente','Dio fenoftaleina','Dio anglosassone ','Dio in agrodolce','Dio focaccella','Dio abbrustolito ','Dio coriaceo','Dio pero','Dio asparago','Dio lacrimogeno','Dio anoressico','Dio mestolo ','Dio levriero ','Dio lamantino','Dio furetto','Dio merovingio','Dio proctologo','Dio pellicano ','Dio slovacco','Dio analfabeta nella valle degli scrittori','Dio aeroplano nel triangolo delle bermuda','Dio calamita nella valle dei rifiuti plastici','Dio scalatore nella valle delle pianure','Dio surfista nel deserto del Sahara      ','Dio ciambella senza buco','Dio ciclista nella valle degli orsi sciatori ','Dio puledro','Dio saliva','Dio saliscendi ','Dio aracnide','Dio lampreda','Dio platano','Dio jeep','Dio poliglotta','Dio piallatrice','Dio svittol','Dio lampadina','Dio fantabosco','Dio lavello','Dio intarsiatore','Dio intarsiato','Dio tibetano','Dio cavalca via','','Dio barbagianni','Dio collaudatore di carote','Dio carotatore di collaudi','Dio stupratore di feti abortiti','Dio cancaro','Dio cancro','Dio accesoriato','Dio stanatore di topi','Dio inalatore di gas tossici','Dio str del','Dio tornio CNC','Dio riparatore di iPhone','Dio suricato ','Dio accrocchio','Dio digitale terrestre','Dio sintonizzato','Dio sintonizzatore','Dio sintetizzatore','Dio telecomandato','Dio aratro','Dio lavoratore cinese sottopagato','Dio minatore','Dio interpretato male in un film','Dio Android','Dio tablet','Dio stampante 3D','Dio kebab','Dio kebabbaro','Dio in monociclo','Dio marsupio','Dio marsupiale','Dio newyorkese','Dio velocipede','Dio sulla sedia elettrica','Dio condannato a morte','Dio caminetto','Dio lampadina','Dio palla','Dio scoreggiatore','Dio spalatore di merda','Dio luce','Dio morto','Dio cancello','Dio pupilla','Dio sperma','Dio assicuratore di vasi da notte','Dio fungo','Dio stupido','Dio fotografia','Dio presa elettrica','Dio folgorato','Dio impest ','Dio vite spanata','Dio dal culo spanato','Dio spanato','Dio panna','Dio zuccheroso','Dio abbraccia alberi','Dio lebbroso','Dio esattore','Dio formica','Dio microfono','Dio pavimento sporco','Dio legnoso','Dio Xbox','Dio barista','Dio stupro','Dio cartaceo','Dio alluminio anodizzato']
    choice=random.choice(list)
    nome_embed2 = discord.Embed(title="**auto distruzione**", description=f"coglione ci sei cascato {choice}", color=discord.Color.green())
    await ctx.send(embed=nome_embed2,content=f"messaggio senza embed")
    #mettere il database  
    #comando easter egg
    #funzionante



@client.command()
async def coso_man(ctx, variabile=None):
    if variabile == None: 
        nome_embed = discord.Embed(title="**pex**", description="date il pex a coso_man!!!!", color=discord.Color.green())
        await ctx.send(embed=nome_embed,content=f"messaggio senza embed {variabile}")
    if variabile == "depex":
        nome_embed2 = discord.Embed(title="**depex**", description="depexate coso_man!!!!", color=discord.Color.green())
        await ctx.send(embed=nome_embed2,content=f"messaggio senza embed")
    #comando easter egg
    #funzionante



@client.command()
async def developer(ctx):
    await ctx.send("!developer  mostra questa lista")
    await ctx.send("!slash_reset  ricarica tutti i comandi slash")
    await ctx.send("!data_delete  elimina gli id dal database")
    await ctx.send("!data_add  mette gli id nel database")
    await ctx.send("!data_get  estrapola dati dal database")
    #comando developer
    #in lista comandi developer
    #funzionante
    #aggiungere messaggio di errore 



@client.command()
async def slash_reset(ctx):
    slash_n = await client.tree.sync()
    await ctx.send(f"ho aggiornato {slash_n} slash")
    #comando developer
    #in lista comandi developer
    #funzionante
    #aggiungere messaggio di errore 



@client.command()
async def data_get(ctx):
        choice = random.randint(1, 4224)
        bestemmia = "bestemmia" + choice
        file = "database.json" 
        with open(file, 'r') as f: 
            dati_database = json.load(f) 
        if str(bestemmia) in dati_database: 
            canale_info = dati_database[str(bestemmia)] 
            await ctx.send(canale_info) 
        else:
            await ctx.send("nessun dato trovato") 
    #comando developer
    #in lista comandi developer
    #funzionante 
    #aggiungere messaggio di errore 



@client.command()
async def data_add(ctx, dato): 
        user_id = ctx.author.id 
        file = "id.json" 
        with open(file, 'r') as f: 
            dati_database = json.load(f) 
        if not str(user_id) in dati_database: 
            dati_database[str(user_id)] = dato 
            with open(file, 'w') as f: 
                json.dump(dati_database, f)
        else:
            await ctx.send("Sei già registrato nel database") 
    #comando developer
    #in lista comandi developer
    #funzionante
    #aggiungere messaggio di errore 



@client.command()
async def data_delete(ctx): 
        user_id = ctx.author.id 
        file = "di.json" 
        with open(file, 'r') as f: 
            dati_database = json.load(f) 
        if str(user_id) in dati_database: 
            await ctx.send("Ho eliminato i tuoi dati") 
            del dati_database[str(user_id)] 
            with open(file, 'w') as f: 
                json.dump(dati_database, f)
        else:
            await ctx.send("non trovato") 
    #comando developer
    #in lista comandi developer
    #funzionante 
    #aggiungere messaggio di errore






token_json = data["discord_token"]
client.run(token_json)
