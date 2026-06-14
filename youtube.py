import sys
import yt_dlp

class QuietLogger:
    """Logger silencioso para suprimir mensagens de erro do yt_dlp"""
    def debug(self, msg): pass
    def info(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass

def _extrair_url(url_alvo, silencioso=False):
    """Tenta extrair a URL do stream para o URL dado"""
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
    }
    if silencioso:
        ydl_opts['logger'] = QuietLogger()

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url_alvo, download=False)
            return info['url']
    except Exception:
        return None

def obter_stream(ch=None, vid=None):
    """Extrai o link direto usando yt-dlp"""
    if ch:
        # 1ª tentativa: sem @ (silenciosa, para não poluir o output)
        url = _extrair_url(f"https://www.youtube.com/{ch}/live", silencioso=True)
        if url:
            return url
        # 2ª tentativa: com @ (caso o canal exija o @)
        if not ch.startswith('@'):
            url = _extrair_url(f"https://www.youtube.com/@{ch}/live", silencioso=False)
        return url
    elif vid:
        return _extrair_url(f"https://www.youtube.com/watch?v={vid}", silencioso=False)
    return None


def do_action():
    if len(sys.argv) < 2:
        print("Uso: python youtube.py live=canal")
        print("Uso: python youtube.py id=VIDEO_ID")
        return

    arg = sys.argv[1]

    if arg.startswith("live="):
        canal = arg.split("=", 1)[1]
        url_do_stream = obter_stream(ch=canal)
    elif arg.startswith("id="):
        video_id = arg.split("=", 1)[1]
        url_do_stream = obter_stream(vid=video_id)
    else:
        print("Uso: python youtube.py live=canal")
        print("Uso: python youtube.py id=VIDEO_ID")
        return

    if url_do_stream:
        print(url_do_stream)
    else:
        print("Não foi possível obter a URL do stream.")

# Executa se o script for chamado diretamente
if __name__ == "__main__":
    do_action()

#Uso: python youtube.py live=SBTNews
#Uso: python youtube.py live=officialMasterChefGlobal
#Uso: python youtube.py live=ClassicMrBean
#Uso: python youtube.py id=dQw4w9WgXcQ