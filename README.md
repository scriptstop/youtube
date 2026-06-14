# youtube.py

Script Python para extrair URLs de streams do YouTube (ao vivo e vídeos) usando `yt-dlp`.

## Dependências

```bash
pip install -r requirements.txt
ou
python3 -m pip install yt-dlp
```

## Uso

```bash
# Canal ao vivo (live)
python youtube.py live=SBTNews
python youtube.py live=officialMasterChefGlobal
python youtube.py live=ClassicMrBean

# Vídeo por ID
python youtube.py id=dQw4w9WgXcQ
```

O script imprime o URL do stream diretamente no `stdout`, tornando-o compatível com sistemas de IPTV (como o MediaCP / EasyPHP) que invocam scripts externos.

## Canais confirmados online

| Canal | Parâmetro |
|-------|-----------|
| SBT NEWS HD | `live=SBTNews` |
| TV Jornal SBT Recife HD | `live=TVJornalSBTRecife` |
| SCC SBT HD | `live=sccsbt` |
| TV Jornal Interior HD | `live=TVJornalInterior` |
| Classic MrBean HD | `live=ClassicMrBean` |
| Warner Bros Classics HD | `live=warnerbrosclassics` |
| Official Master Chef Global HD | `live=officialMasterChefGlobal` |

## Notas

- Se o canal não for encontrado sem `@`, o script tenta automaticamente com `@` (ex: `@officialMasterChefGlobal`).
- Erros silenciosos na primeira tentativa — só mostra erro se o canal estiver realmente offline.
- Compatível com `youtube.cfg` para uso como script externo em sistemas de streaming.
# youtube
