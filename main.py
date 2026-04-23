import sys
import urllib.parse
import xbmcgui
import xbmcplugin

def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def main():
    try:
        handle = int(sys.argv[1])
        arg_string = sys.argv[2][1:] if len(sys.argv[2]) > 1 else ""
        params = dict(urllib.parse.parse_qsl(arg_string))
    except:
        return

    # --- KOMPLETNÁ DATABÁZA SLOVENSKÝCH RÁDIÍ ---
    radia_sk = [
        {"nazov": "Rádio Tlis", "url": "https://stream.tlis.sk/tlis.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/tlis.png"},
        {"nazov": "Rádio Topoľčany", "url": "http://80.242.44.249:8000/;", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/topolcany.png"},
        {"nazov": "Radio Slovakia International", "url": "https://icecast.stv.livebox.sk/rsi_128.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/slovakia-international.png"},
        {"nazov": "Rádio Šírava", "url": "http://stream.sepia.sk:8000/radiosirava.mp3", "logo": "https://cdn.radia.sk/_radia/loga/app/sirava.webp?v=2"},
        {"nazov": "Rádio Rock SV", "url": "https://s2.myradiostream.com/:4870/listen.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/rock-sv.png"},
        {"nazov": "Rádio Sity", "url": "https://radiosity.online:8000/aac", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/sity.png"},
        {"nazov": "Rádio Pyramída", "url": "https://icecast.stv.livebox.sk/pyramida_128.mp3", "logo": "https://www.radiomix.sk/wp-content/uploads/2024/01/radio-pyramida-560x560.png"},
        {"nazov": "Rádio Rebeca", "url": "https://mpc2.mediacp.eu:8200/rebecaweb", "logo": "https://cdn.radia.sk/_radia/loga/app/rebeca.webp?v=2"},
        {"nazov": "Rádio Pohoda 2", "url": "http://mpc1.mediacp.eu:18111/stream", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/pohoda2.png"},
        {"nazov": "Rádio Pokoj", "url": "http://radioserver.online:8822/;", "logo": "https://cdn.radia.sk/_radia/loga/app/pokoj.webp?v=2"},
        {"nazov": "Rádio Piešťany", "url": "https://solid33.streamupsolutions.com/proxy/gktiemqb/stream", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-piestany/play_250_250.webp"},
        {"nazov": "Rádio Pohoda", "url": "https://audio.radiopohoda.com:8000/stream", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-pohoda/fb_cover.jpg"},
        {"nazov": "Rádio Paráda", "url": "https://extra.mediacp.eu/stream/RadioParada,o.z.", "logo": "https://www.radioparada.sk/wp-content/uploads/2021/12/LOGO-PARADA-NEW-1024x1024.png"},
        {"nazov": "Rádio Patria", "url": "https://icecast.stv.livebox.sk/patria_128.mp3", "logo": "https://upload.wikimedia.org/wikipedia/commons/8/85/R%C3%A1dio_PATRIA_LOGO.jpg"},
        {"nazov": "Rádio Modra", "url": "http://185.98.208.12:8000/;", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/modra.png"},
        {"nazov": "Rádio PaF", "url": "https://node-23.zeno.fm/92cv04cggfhvv", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/paf.png"},
        {"nazov": "Rádio Logos", "url": "http://radioserver.online:8824/;", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/logos.png"},
        {"nazov": "Rádio Metropolitan", "url": "https://mpc2.mediacp.eu:8214/stream", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-metropolitan/play_250_250.webp"},
        {"nazov": "Rádio Klub", "url": "https://listen.radioking.com/radio/860681/stream/930496", "logo": "https://d3t3ozftmdmh3i.cloudfront.net/staging/podcast_uploaded_nologo/44153165/44153165-1756027969361-fe65b85dada35.jpg"},
        {"nazov": "Rádio Litera", "url": "https://icecast.stv.livebox.sk/litera_128.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/litera.png"},
        {"nazov": "Rádio KIKS - Big 90s", "url": "https://online.radiokiks.sk:8000/kiks_big90s.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/kiks-big-90s.png"},
        {"nazov": "Rádio KIKS - Rock Music", "url": "https://online.radiokiks.sk:8000/kiks_rock.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/kiks-rock-music.png"},
        {"nazov": "Rádio KIKS", "url": "https://online.radiokiks.sk:8000/kiks_hq.mp3", "logo": "https://cdn.radia.sk/_radia/loga/app/kiks.webp?v=1"},
        {"nazov": "Rádio KIKS - Big 80s", "url": "https://online.radiokiks.sk:8000/kiks_big80s.mp3", "logo": "https://radiokiks.net/wp-content/uploads/2024/08/Logo_BIG_80.png"},
        {"nazov": "Rádio Jemné Chillout", "url": "https://stream.bauermedia.sk/chillout-hi.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/jemne-chillout.png"},
        {"nazov": "Rádio Junior", "url": "https://icecast.stv.livebox.sk/junior_128.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-junior/fb_cover.jpg"},
        {"nazov": "Rádio Janko Hraško", "url": "http://78.24.9.110:31088/;", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-janko-hrasko/play_250_250.webp"},
        {"nazov": "Rádio Jazz", "url": "http://stream.sepia.sk:8000/jazz192.mp3", "logo": "http://radiojazz.sk/image/logo.png"},
        {"nazov": "Rádio FanWaves", "url": "https://stream.zeno.fm/gtkbdehhekftv", "logo": "https://images.zeno.fm/ZtUvkDMtkuf8ykYmi9VmIi3zRsaaaKixAoEEe6F5Tzk/rs:fill:288:288/g:ce:0:0/aHR0cHM6Ly9wcm94eS56ZW5vLmZtL2NvbnRlbnQvc3RhdGlvbnMvYzFkZDQwMDYtMjJkNC00NjYyLWIyZGMtZjNjNTVlYmY2YWVlL2ltYWdlLz91PTE3NTUzNjM0NjEwMDA.webp"},
        {"nazov": "Rádio Folk", "url": "https://mpc1.mediacp.eu/stream/demo2", "logo": "https://www.radiofolk.sk/wp-content/uploads/2021/08/cropped-cropped-cropped-Logo-pre-web.png"},
        {"nazov": "Rádio Biblia", "url": "http://radiobiblia.online:8000/stream.ogg", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-biblia/play_250_250.webp"},
        {"nazov": "Rádio Extra", "url": "http://live.topradio.cz:8000/extra192", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-extra/fb_cover.jpg"},
        {"nazov": "Rádio Beta Česko a Slovenské Hity", "url": "http://109.71.67.102:8000/beta_cspop.mp3", "logo": "https://cdn.radia.sk/_radia/loga/app/beta-cz-sk-hity.webp?v=1"},
        {"nazov": "Rádio Beta 80'S a 90'S", "url": "http://109.71.67.102:8000/beta_80a90.mp3", "logo": "https://cdn.radia.sk/_radia/loga/app/beta-hity-80s-90s.webp?v=1"},
        {"nazov": "Rádio Beta Hráme jubilantom", "url": "http://109.71.67.102:8000/beta_jubilanti.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/beta-hrame-jubilantom.png"},
        {"nazov": "Rádio Bela", "url": "http://65.109.81.84:8855/live", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/bela.png"},
        {"nazov": "Rádio Best FM", "url": "https://stream3.bestfm.sk:8000/160.aac", "logo": "https://bestfm.sk/wp-content/uploads/2021/09/logo_transparent.png"},
        {"nazov": "Rádio Basavel", "url": "https://stream.zeno.fm/6gd9c6yn4nhvv", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/basavel.png"},
        {"nazov": "Rádio Aetter", "url": "http://stream.aetter.sk:8000/aetter", "logo": "https://cdn.radia.sk/_radia/loga/app/aetter.webp?v=1"},
        {"nazov": "Rádio 7", "url": "https://play.radio7.sk/128", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/7.png"},
        {"nazov": "Rádio 9", "url": "http://147.232.191.167:8000/high.mp3", "logo": "https://cdn.radia.sk/_radia/loga/coverflow/9.png"},
        {"nazov": "PARTY RADIO", "url": "https://mpc1.mediacp.eu/stream/partyradio", "logo": "http://files.exoweb.eu/13/40/13404079-0cdd-42be-88cd-e832e3e5542c.jpeg"},
        {"nazov": "Rádio Viva", "url": "http://stream.sepia.sk:8000/viva320.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-viva/play_250_250.webp"},
        {"nazov": "Fresh Rádio", "url": "https://icecast2.radionet.sk/freshradio.sk", "logo": "https://myonlineradio.sk/public/uploads/radio_img/fresh-radio/play_250_250.webp"},
        {"nazov": "Rádio Rock", "url": "https://stream.bauermedia.sk/rock-hi.mp3", "logo": "https://radiorock.sk/intro-v2.png"},
        {"nazov": "Rádio Maria Slovakia", "url": "https://dreamsiteradiocp5.com/proxy/radiomariaslomp3?mp=/stream.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-maria-slovensko/play_250_250.webp"},
        {"nazov": "Rádio Lumen", "url": "https://audio.lumen.sk/live128.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/lumen.png"},
        {"nazov": "Na vlne Novohradu", "url": "https://radioserver.online/proxy/navlnenovohradu/novohradHQ.mp3", "logo": "https://www.radia.sk/_radia/loga/app/navlnenovohradu.webp?v=1"},
        {"nazov": "Na vlne Liptova", "url": "http://radioserver.online:8009/hq.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/na-vlne-liptova.png"},
        {"nazov": "Mirjam Radio", "url": "https://dreamsiteradiocp5.com/proxy/rmslo?mp=/stream", "logo": "https://www.radia.sk/_radia/loga/app/mirjam.webp?v=1"},
        {"nazov": "METALSCENA netRADIO", "url": "https://listen.radioking.com/radio/263218/stream/308365", "logo": "https://www.radia.sk/_radia/loga/coverflow/metalscena.png"},
        {"nazov": "Mars Dance Rádio", "url": "https://stream.zenolive.com/683gf5xrxfeuv?1686916511841", "logo": "https://www.radia.sk/_radia/loga/app/mars-dance.webp?v=2"},
        {"nazov": "HITRÁDIO SLOVAKIA", "url": "https://hitradioslovakia.stream.laut.fm/hitradioslovakia", "logo": "https://myonlineradio.sk/public/uploads/radio_img/hitradio-slovakia/play_250_250.webp"},
        {"nazov": "BB FM", "url": "http://stream.bbfm.sk:8000/bbfm128.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/bb-fm-radio/play_250_250.webp"},
        {"nazov": "Rádio Regina - Západ", "url": "https://icecast.stv.livebox.sk/regina-ba_128.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/regina-zapad.png"},
        {"nazov": "Rádio Regina - Stred", "url": "https://icecast.stv.livebox.sk/regina-bb_128.mp3", "logo": "https://www.radia.sk/_radia/loga/app/regina-stred.webp?v=2"},
        {"nazov": "Rádio Regina - Východ", "url": "https://icecast.stv.livebox.sk/regina-ke_128.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/regina-vychod.png"},
        {"nazov": "Rádio Devín", "url": "https://icecast.stv.livebox.sk/devin_128.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/devin.png"},
        {"nazov": "Europa 2", "url": "https://stream.bauermedia.sk/europa2-hi.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/europa2.png"},
        {"nazov": "Dobré Rádio", "url": "https://stream.dobreradio.sk/dobreradio.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/dobre.png"},
        {"nazov": "Rádio InfoVojna", "url": "https://stream1.infovojna.com:8000/live", "logo": "https://topradio.sk/_next/image?url=%2Fimages%2Finfovojna.jpg&w=640&q=75"},
        {"nazov": "Rádio_FM", "url": "https://icecast.stv.livebox.sk/fm_128.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/fm.png"},
        {"nazov": "Rádio Dychovka", "url": "https://epanel.mediacp.eu:7661/stream", "logo": "https://www.radia.sk/_radia/loga/app/dychovka.webp?v=1"},
        {"nazov": "Rádio Košice", "url": "http://stream.ecce.sk:8000/radiokosice-128.mp3", "logo": "https://data.tvkosice.sk/images/cm/1000x0xresize/r/a/d/radiokosice/8e/fe/8efe9b31-bd08-4f5d-9168-fa656184fdd2.jpg"},
        {"nazov": "FIT Family RADIO", "url": "http://solid67.streamupsolutions.com:8052/;", "logo": "https://www.radia.sk/_radia/loga/app/fit-family.webp?v=1"},
        {"nazov": "Rádio WOW", "url": "https://radioserver.online:9816/radiowow.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/wow.png"},
        {"nazov": "Rádio Slovensko", "url": "https://icecast.stv.livebox.sk/slovensko_128.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-slovensko/play_250_250.webp"},
        {"nazov": "Detské Rádio", "url": "https://stream.21.sk/detskeradio-192.mp3", "logo": "https://data.tvkosice.sk/images/cm/1000x0xresize/r/a/d/radiokosice/08/80/0880daa2-a629-4ce0-9bf9-ab7765572c2f.jpg"},
        {"nazov": "Rádio Frontinus", "url": "http://stream.frontinus.sk:8000/frontinus128.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-frontinus/play_250_250.webp"},
        {"nazov": "Rádio Expres", "url": "https://stream.expres.sk/128.mp3", "logo": "https://www.radia.sk/_radia/loga/coverflow/expres.png"},
        {"nazov": "Rádio Melody", "url": "https://stream.bauermedia.sk/melody-hi.mp3", "logo": "https://www.radiomelody.sk/cover.png?f=raw"},
        {"nazov": "Rádio Beta", "url": "http://109.71.67.102:8000/beta_live_high.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-beta/play_250_250.webp"},
        {"nazov": "Fun Rádio", "url": "https://stream.funradio.sk:8000/fun128.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/fun-radio/play_250_250.webp"},
        {"nazov": "Rádio Vlna", "url": "http://stream.radiovlna.sk/vlna-hi.mp3", "logo": "https://myonlineradio.sk/public/uploads/radio_img/radio-vlna/play_250_250.webp"}
    ]

    radia_cz = [
        {"nazov": "Rádio Kiss", "url": "https://n25a-eu.rcs.revma.com/asn0cmvb938uv", "logo": "https://i1.sndcdn.com/artworks-000055555247-hukx9y-t500x500.jpg"},
        {"nazov": "Rádio Impuls", "url": "http://icecast5.play.cz/impuls128.mp3", "logo": "https://www.impuls.cz/img/logo-impuls.png"},
        {"nazov": "Evropa 2", "url": "https://ice.actve.net/fm-evropa2-128", "logo": "https://www.evropa2.cz/wp-content/themes/evropa2/assets/img/logo.png"}
    ]

    # --- 1. HLAVNÉ MENU ---
    if not params:
        menu_items = [
            ("🌍 [B]ŠTÁTY[/B]", {'action': 'list_states'}),
            ("🔍 [B]VYHĽADÁVANIE[/B]", {'action': 'search'}),
            ("🆕 [B]NAJNOVŠIE PRIDANÉ[/B]", {'action': 'latest'}),
            ("⭐ [B]OBLÚBENÉ[/B]", {'action': 'list_fav'}),
        ]
        for label, p in menu_items:
            li = xbmcgui.ListItem(label=label)
            xbmcplugin.addDirectoryItem(handle, build_url(p), li, True)
        xbmcplugin.endOfDirectory(handle)

    # --- 2. PODMENU: ŠTÁTY ---
    elif params.get('action') == 'list_states':
        states = [
            ("🇸🇰 [B]Slovenské Rádiá[/B]", {'country': 'sk'}, "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Slovakia.svg/1200px-Flag_of_Slovakia.svg.png"),
            ("🇨🇿 [B]České Rádiá[/B]", {'country': 'cz'}, "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_Czech_Republic.svg/1200px-Flag_of_the_Czech_Republic.svg.png"),
            ("🇭🇺 [B]Maďarské Rádiá[/B]", {'action': 'msg', 'text': 'Maďarské rádiá - Pripravujeme sa'}, "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Flag_of_Hungary.svg/1200px-Flag_of_Hungary.svg.png")
        ]
        for label, p, icon in states:
            li = xbmcgui.ListItem(label=label)
            li.setArt({'icon': icon, 'thumb': icon})
            xbmcplugin.addDirectoryItem(handle, build_url(p), li, True)
        xbmcplugin.endOfDirectory(handle)

    # --- 3. PODMENU: OBLÚBENÉ ---
    elif params.get('action') == 'list_fav':
        favs = [
            ("⭐ [B]TOP Slovensko 10[/B]", {'action': 'top10_sk'}),
            ("⭐ [B]TOP Česko 10[/B]", {'action': 'top10_cz'}),
        ]
        for label, p in favs:
            li = xbmcgui.ListItem(label=label)
            xbmcplugin.addDirectoryItem(handle, build_url(p), li, True)
        xbmcplugin.endOfDirectory(handle)

    # --- 4. FUNKCIA: VYHĽADÁVANIE ---
    elif params.get('action') == 'search':
        kb = xbmcgui.Dialog().input('Hľadať rádio', type=xbmcgui.INPUT_ALPHANUM)
        if kb:
            query = kb.lower()
            vsetky = radia_sk + radia_cz
            vysledky = [r for r in vsetky if query in r['nazov'].lower()]
            if vysledky:
                zobraz_radia(handle, vysledky)
            else:
                xbmcgui.Dialog().ok("Hľadanie", "Nenašli sa žiadne výsledky pre: " + kb)
        xbmcplugin.endOfDirectory(handle)

    # --- 5. ZOBRAZENIE RÁDIÍ ---
    elif params.get('country') == 'sk':
        zobraz_radia(handle, radia_sk)

    elif params.get('country') == 'cz':
        zobraz_radia(handle, radia_cz)

    elif params.get('action') == 'latest':
        zobraz_radia(handle, radia_sk[:5]) # Prvé v zozname (Tlis, Topoľčany...)

    elif params.get('action') == 'top10_sk':
        zobraz_radia(handle, radia_sk[-10:])

    elif params.get('action') == 'msg':
        xbmcgui.Dialog().ok("Informácia", params.get('text', 'Pripravujeme sa'))
        xbmcplugin.endOfDirectory(handle)

def zobraz_radia(handle, zoznam):
    for radio in zoznam:
        li = xbmcgui.ListItem(label=radio["nazov"])
        li.setArt({'thumb': radio["logo"], 'icon': radio["logo"]})
        li.setInfo('audio', {'title': radio["nazov"], 'mediatype': 'music'})
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(handle, radio["url"], li, False)
    xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    main()

