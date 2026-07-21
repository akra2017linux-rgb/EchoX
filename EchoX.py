import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import customtkinter as ctk
from tkinter import filedialog
import pygame
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from PIL import Image
import io
import shutil
import random

# --- PALETA DE CORES PROFISSIONAL (ESTILO SPOTIFY / OPEN SOURCE) ---
COR_FUNDO = "#121212"
COR_CARD = "#181818"
COR_CARD_HOVER = "#242424"
COR_VERDE = "#1DB954"
COR_VERDE_HOVER = "#1ed760"
COR_TEXTO = "#FFFFFF"
COR_CINZA = "#B3B3B3"
COR_SELECIONADO = "#282828"

ctk.set_appearance_mode("dark")
DIRETORIO_PLAYLISTS = "EchoX_Playlists"

class EchoXPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("EchoX - Open Source Music Experience")
        self.root.geometry("950x670")
        self.root.resizable(False, False)
        self.root.configure(fg_color=COR_FUNDO)

        pygame.init()
        pygame.mixer.music.set_volume(0.5)

        self.EVENTO_FIM_MUSICA = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.EVENTO_FIM_MUSICA)

        # Estados e Fila
        self.playlists = {}
        self.playlist_atual = ""
        self.playlist_caminhos = []
        self.playlist_filtrada = []
        self.indice_atual = 0
        self.esta_tocando = False
        self.esta_pausado = False
        self.tempo_total = 0
        
        # Modos de Reprodução
        self.aleatorio_ativo = False
        self.repetir_ativo = False

        self.carregar_playlists()

        # Atalhos de Teclado
        self.root.bind("<F5>", lambda event: self.tocar_pausar())
        self.root.bind("<F6>", lambda event: self.parar_musica())
        self.root.bind("<F7>", lambda event: self.musica_anterior())
        self.root.bind("<F8>", lambda event: self.proxima_musica())

        self.criar_interfaces()
        
        if self.playlist_caminhos:
            self.atualizar_visor_playlist()
            self.extrair_metadados(self.playlist_caminhos[self.indice_atual])

        self.atualizar_progresso()

    def criar_interfaces(self):
        # --- ÁREA SUPERIOR (Conteúdo Principal) ---
        self.frame_conteudo = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame_conteudo.pack(fill="both", expand=True, padx=20, pady=(20, 10))

        # Esquerda: Capa e Detalhes da Música Atual
        self.frame_esq = ctk.CTkFrame(self.frame_conteudo, fg_color=COR_CARD, corner_radius=12, width=310)
        self.frame_esq.pack(side="left", fill="y", padx=(0, 15))
        self.frame_esq.pack_propagate(False)

        img_padrao = Image.new("RGB", (250, 250), (30, 30, 30))
        self.capa_img = ctk.CTkImage(light_image=img_padrao, dark_image=img_padrao, size=(250, 250))
        self.lbl_capa = ctk.CTkLabel(self.frame_esq, image=self.capa_img, text="", corner_radius=8)
        self.lbl_capa.pack(padx=30, pady=(25, 15))

        self.lbl_titulo = ctk.CTkLabel(self.frame_esq, text="Nenhuma música", font=("Arial", 16, "bold"), text_color=COR_TEXTO)
        self.lbl_titulo.pack(padx=20, anchor="w")

        self.lbl_artista = ctk.CTkLabel(self.frame_esq, text="Selecione ou importe uma pasta", font=("Arial", 13), text_color=COR_CINZA)
        self.lbl_artista.pack(padx=20, anchor="w", pady=(2, 20))

        # Direita: Gerenciador de Playlists, Pesquisa e Fila Interativa
        self.frame_dir = ctk.CTkFrame(self.frame_conteudo, fg_color=COR_CARD, corner_radius=12)
        self.frame_dir.pack(side="right", fill="both", expand=True)

        # Cabeçalho da Fila com Seletor de Playlist
        self.frame_topo_playlist = ctk.CTkFrame(self.frame_dir, fg_color="transparent")
        self.frame_topo_playlist.pack(fill="x", padx=20, pady=(15, 5))

        self.lbl_playlist_titulo = ctk.CTkLabel(self.frame_topo_playlist, text="Biblioteca (Pastas)", font=("Arial", 16, "bold"), text_color=COR_TEXTO)
        self.lbl_playlist_titulo.pack(side="left")

        nomes_playlists = list(self.playlists.keys()) if self.playlists else ["Favoritas"]
        self.menu_playlists = ctk.CTkOptionMenu(
            self.frame_topo_playlist,
            values=nomes_playlists,
            command=self.trocar_playlist,
            fg_color="#2A2A2A",
            button_color="#3A3A3A",
            button_hover_color=COR_VERDE,
            text_color=COR_TEXTO,
            width=150
        )
        self.menu_playlists.pack(side="right")
        if self.playlist_atual:
            self.menu_playlists.set(self.playlist_atual)

        # Barra de Pesquisa de Músicas
        self.entry_busca = ctk.CTkEntry(self.frame_dir, placeholder_text="🔍 Pesquisar música na pasta...", fg_color="#202020", text_color=COR_TEXTO, border_color="#333333", height=32)
        self.entry_busca.pack(fill="x", padx=20, pady=(5, 10))
        self.entry_busca.bind("<KeyRelease>", self.filtrar_musicas)

        # Scrollable Frame para a lista de músicas
        self.scroll_playlist = ctk.CTkScrollableFrame(self.frame_dir, fg_color="transparent", corner_radius=8)
        self.scroll_playlist.pack(fill="both", expand=True, padx=15, pady=0)

        # Botões de Gerenciamento de Pastas e Músicas
        self.frame_botoes_playlist = ctk.CTkFrame(self.frame_dir, fg_color="transparent")
        self.frame_botoes_playlist.pack(fill="x", padx=20, pady=12)

        self.frame_linha1 = ctk.CTkFrame(self.frame_botoes_playlist, fg_color="transparent")
        self.frame_linha1.pack(fill="x", pady=(0, 6))

        self.btn_nova_pl = ctk.CTkButton(self.frame_linha1, text="+ Nova Pasta", fg_color="#2A2A2A", hover_color="#3A3A3A", text_color=COR_TEXTO, font=("Arial", 12), height=32, command=self.criar_nova_playlist)
        self.btn_nova_pl.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self.btn_importar_pl = ctk.CTkButton(self.frame_linha1, text="📁 Importar Pasta (MP3)", fg_color="#2A2A2A", hover_color="#3A3A3A", text_color=COR_TEXTO, font=("Arial", 12), height=32, width=170, command=self.importar_playlist)
        self.btn_importar_pl.pack(side="right", padx=(4, 0))

        self.frame_linha2 = ctk.CTkFrame(self.frame_botoes_playlist, fg_color="transparent")
        self.frame_linha2.pack(fill="x")

        self.btn_add = ctk.CTkButton(self.frame_linha2, text="+ Adicionar Músicas", fg_color=COR_VERDE, hover_color=COR_VERDE_HOVER, text_color="#000000", font=("Arial", 12, "bold"), height=32, command=self.adicionar_a_playlist)
        self.btn_add.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self.btn_limpar = ctk.CTkButton(self.frame_linha2, text="Esvaziar", fg_color="#333333", hover_color="#444444", text_color=COR_TEXTO, font=("Arial", 12), height=32, width=80, command=self.limpar_playlist)
        self.btn_limpar.pack(side="right", padx=(4, 0))

        # --- BARRA INFERIOR (Player Bar Fixa) ---
        self.frame_inferior = ctk.CTkFrame(self.root, fg_color=COR_CARD, corner_radius=0, height=95)
        self.frame_inferior.pack(fill="x", side="bottom")
        self.frame_inferior.pack_propagate(False)

        self.frame_player_bar = ctk.CTkFrame(self.frame_inferior, fg_color="transparent")
        self.frame_player_bar.pack(fill="both", expand=True, padx=20, pady=12)

        self.frame_controles_centro = ctk.CTkFrame(self.frame_player_bar, fg_color="transparent")
        self.frame_controles_centro.pack(fill="x", expand=True)

        self.frame_botoes_acao = ctk.CTkFrame(self.frame_controles_centro, fg_color="transparent")
        self.frame_botoes_acao.pack(pady=(0, 6))

        # Botão Aleatório (Shuffle)
        self.btn_aleatorio = ctk.CTkButton(self.frame_botoes_acao, text="🔀", width=34, height=34, fg_color="transparent", hover_color=COR_CARD_HOVER, text_color=COR_CINZA, font=("Arial", 14), command=self.alternar_aleatorio)
        self.btn_aleatorio.pack(side="left", padx=4)

        self.btn_anterior = ctk.CTkButton(self.frame_botoes_acao, text="⏮", width=36, height=36, fg_color="transparent", hover_color=COR_CARD_HOVER, text_color=COR_TEXTO, font=("Arial", 16), command=self.musica_anterior)
        self.btn_anterior.pack(side="left", padx=4)

        self.btn_play_pause = ctk.CTkButton(self.frame_botoes_acao, text="▶", width=42, height=42, fg_color=COR_TEXTO, hover_color="#E0E0E0", text_color="#000000", font=("Arial", 18, "bold"), corner_radius=21, command=self.tocar_pausar)
        self.btn_play_pause.pack(side="left", padx=8)

        self.btn_parar = ctk.CTkButton(self.frame_botoes_acao, text="⏹", width=36, height=36, fg_color="transparent", hover_color=COR_CARD_HOVER, text_color=COR_TEXTO, font=("Arial", 14), command=self.parar_musica)
        self.btn_parar.pack(side="left", padx=4)

        self.btn_proxima = ctk.CTkButton(self.frame_botoes_acao, text="⏭", width=36, height=36, fg_color="transparent", hover_color=COR_CARD_HOVER, text_color=COR_TEXTO, font=("Arial", 16), command=self.proxima_musica)
        self.btn_proxima.pack(side="left", padx=4)

        # Botão Repetir (Repeat)
        self.btn_repetir = ctk.CTkButton(self.frame_botoes_acao, text="🔁", width=34, height=34, fg_color="transparent", hover_color=COR_CARD_HOVER, text_color=COR_CINZA, font=("Arial", 14), command=self.alternar_repetir)
        self.btn_repetir.pack(side="left", padx=4)

        # Timeline
        self.frame_timeline = ctk.CTkFrame(self.frame_controles_centro, fg_color="transparent")
        self.frame_timeline.pack(fill="x", padx=40)

        self.lbl_tempo_atual = ctk.CTkLabel(self.frame_timeline, text="00:00", font=("Arial", 11), text_color=COR_CINZA)
        self.lbl_tempo_atual.pack(side="left", padx=(0, 10))

        self.barra_progresso = ctk.CTkProgressBar(self.frame_timeline, height=5, progress_color=COR_VERDE, fg_color="#333333")
        self.barra_progresso.set(0)
        self.barra_progresso.pack(side="left", fill="x", expand=True, padx=5)

        self.lbl_tempo_total = ctk.CTkLabel(self.frame_timeline, text="00:00", font=("Arial", 11), text_color=COR_CINZA)
        self.lbl_tempo_total.pack(side="right", padx=(10, 0))

        # Volume
        self.frame_volume_box = ctk.CTkFrame(self.frame_player_bar, fg_color="transparent")
        self.frame_volume_box.place(relx=0.98, rely=0.5, anchor="e")

        self.lbl_icone_volume = ctk.CTkLabel(self.frame_volume_box, text="🔊", font=("Arial", 14), text_color=COR_CINZA)
        self.lbl_icone_volume.pack(side="left", padx=(0, 6))

        self.slider_volume = ctk.CTkSlider(self.frame_volume_box, from_=0.0, to=1.0, width=110, height=12, progress_color=COR_VERDE, button_color=COR_TEXTO, button_hover_color=COR_VERDE, command=self.mudar_volume)
        self.slider_volume.set(0.5)
        self.slider_volume.pack(side="left")

    def alternar_aleatorio(self):
        self.aleatorio_ativo = not self.aleatorio_ativo
        cor = COR_VERDE if self.aleatorio_ativo else COR_CINZA
        self.btn_aleatorio.configure(text_color=cor)

    def alternar_repetir(self):
        self.repetir_ativo = not self.repetir_ativo
        cor = COR_VERDE if self.repetir_ativo else COR_CINZA
        self.btn_repetir.configure(text_color=cor)

    def filtrar_musicas(self, event=None):
        termo = self.entry_busca.get().lower().strip()
        if not termo:
            self.playlist_filtrada = self.playlist_caminhos
        else:
            self.playlist_filtrada = [
                c for c in self.playlist_caminhos 
                if termo in os.path.basename(c).lower()
            ]
        self.atualizar_visor_playlist(filtrado=True)

    def carregar_playlists(self):
        if not os.path.exists(DIRETORIO_PLAYLISTS):
            os.makedirs(DIRETORIO_PLAYLISTS)

        self.playlists = {}
        try:
            for nome_pasta in os.listdir(DIRETORIO_PLAYLISTS):
                caminho_pasta = os.path.join(DIRETORIO_PLAYLISTS, nome_pasta)
                if os.path.isdir(caminho_pasta):
                    mp3s = []
                    for root, dirs, files in os.walk(caminho_pasta):
                        for f in files:
                            if f.lower().endswith(".mp3"):
                                mp3s.append(os.path.join(root, f))
                    self.playlists[nome_pasta] = sorted(mp3s)
        except Exception as e:
            print(f"Erro ao carregar pastas: {e}")

        if not self.playlists:
            pasta_padrao = os.path.join(DIRETORIO_PLAYLISTS, "Favoritas")
            os.makedirs(pasta_padrao, exist_ok=True)
            self.playlists["Favoritas"] = []

        if self.playlist_atual not in self.playlists:
            self.playlist_atual = list(self.playlists.keys())[0]
        
        self.playlist_caminhos = self.playlists.get(self.playlist_atual, [])
        self.playlist_filtrada = self.playlist_caminhos

    def atualizar_opcoes_playlists(self):
        nomes = list(self.playlists.keys())
        self.menu_playlists.configure(values=nomes)
        if self.playlist_atual in nomes:
            self.menu_playlists.set(self.playlist_atual)
        elif nomes:
            self.menu_playlists.set(nomes[0])

    def trocar_playlist(self, nova_playlist):
        self.parar_musica()
        self.playlist_atual = nova_playlist
        self.playlist_caminhos = self.playlists.get(nova_playlist, [])
        self.playlist_filtrada = self.playlist_caminhos
        self.entry_busca.delete(0, "end")
        self.indice_atual = 0
        self.atualizar_visor_playlist()
        
        if self.playlist_caminhos:
            self.extrair_metadados(self.playlist_caminhos[self.indice_atual])
        else:
            self.limpar_visor_musica_atual()

    def criar_nova_playlist(self):
        dialog = ctk.CTkInputDialog(text="Digite o nome da nova pasta/playlist:", title="Criar Pasta")
        nome = dialog.get_input()
        if nome:
            nome = nome.strip()
            if nome:
                caminho_nova_pasta = os.path.join(DIRETORIO_PLAYLISTS, nome)
                if not os.path.exists(caminho_nova_pasta):
                    try:
                        os.makedirs(caminho_nova_pasta, exist_ok=True)
                        self.carregar_playlists()
                        self.atualizar_opcoes_playlists()
                        self.menu_playlists.set(nome)
                        self.trocar_playlist(nome)
                    except Exception as e:
                        print(f"Erro ao criar pasta: {e}")

    def importar_playlist(self):
        pasta_origem = filedialog.askdirectory(title="Selecione uma pasta para buscar arquivos MP3")
        if pasta_origem:
            nome_pasta = os.path.basename(pasta_origem) or "Pasta Importada"
            caminho_destino = os.path.join(DIRETORIO_PLAYLISTS, nome_pasta)
            contador = 1
            nome_original = nome_pasta
            while os.path.exists(caminho_destino):
                nome_pasta = f"{nome_original} ({contador})"
                caminho_destino = os.path.join(DIRETORIO_PLAYLISTS, nome_pasta)
                contador += 1
            
            try:
                os.makedirs(caminho_destino, exist_ok=True)
                encontrados = 0
                for root, dirs, files in os.walk(pasta_origem):
                    for arquivo in files:
                        if arquivo.lower().endswith(".mp3"):
                            c_origem = os.path.join(root, arquivo)
                            c_destino = os.path.join(caminho_destino, arquivo)
                            sub = 1
                            base, ext = os.path.splitext(arquivo)
                            while os.path.exists(c_destino):
                                c_destino = os.path.join(caminho_destino, f"{base}_{sub}{ext}")
                                sub += 1
                            shutil.copy(c_origem, c_destino)
                            encontrados += 1
                
                if encontrados > 0:
                    self.carregar_playlists()
                    self.atualizar_opcoes_playlists()
                    self.menu_playlists.set(nome_pasta)
                    self.trocar_playlist(nome_pasta)
                else:
                    os.rmdir(caminho_destino)
            except Exception as e:
                print(f"Erro ao importar: {e}")

    def adicionar_a_playlist(self):
        arquivos = filedialog.askopenfilenames(filetypes=[("Músicas MP3", "*.mp3")])
        if arquivos:
            caminho_pasta_atual = os.path.join(DIRETORIO_PLAYLISTS, self.playlist_atual)
            os.makedirs(caminho_pasta_atual, exist_ok=True)
            for arquivo in arquivos:
                try:
                    nome = os.path.basename(arquivo)
                    destino = os.path.join(caminho_pasta_atual, nome)
                    sub = 1
                    base, ext = os.path.splitext(nome)
                    while os.path.exists(destino):
                        destino = os.path.join(caminho_pasta_atual, f"{base}_{sub}{ext}")
                        sub += 1
                    shutil.copy(arquivo, destino)
                except Exception as e:
                    print(f"Erro ao copiar: {e}")
            
            self.carregar_playlists()
            self.playlist_caminhos = self.playlists.get(self.playlist_atual, [])
            self.filtrar_musicas()
            
            if not self.esta_tocando and self.playlist_caminhos:
                self.indice_atual = 0
                self.extrair_metadados(self.playlist_caminhos[self.indice_atual])

    def limpar_playlist(self):
        self.parar_musica()
        caminho_pasta_atual = os.path.join(DIRETORIO_PLAYLISTS, self.playlist_atual)
        if os.path.exists(caminho_pasta_atual):
            for root, dirs, files in os.walk(caminho_pasta_atual):
                for f in files:
                    if f.lower().endswith(".mp3"):
                        try:
                            os.remove(os.path.join(root, f))
                        except:
                            pass
        self.playlists[self.playlist_atual] = []
        self.playlist_caminhos = []
        self.playlist_filtrada = []
        self.atualizar_visor_playlist()
        self.limpar_visor_musica_atual()

    def limpar_visor_musica_atual(self):
        self.lbl_titulo.configure(text="Nenhuma música")
        self.lbl_artista.configure(text="Pasta vazia")
        img_padrao = Image.new("RGB", (250, 250), (30, 30, 30))
        capa_padrao = ctk.CTkImage(light_image=img_padrao, dark_image=img_padrao, size=(250, 250))
        self.lbl_capa.configure(image=capa_padrao)
        self.lbl_tempo_atual.configure(text="00:00")
        self.lbl_tempo_total.configure(text="00:00")
        self.barra_progresso.set(0)

    def atualizar_visor_playlist(self, filtrado=False):
        for widget in self.scroll_playlist.winfo_children():
            widget.destroy()

        lista_exibicao = self.playlist_filtrada if filtrado else self.playlist_caminhos

        for caminho in lista_exibicao:
            try:
                i = self.playlist_caminhos.index(caminho)
            except ValueError:
                continue

            nome_arquivo = os.path.basename(caminho)
            nome_limpo = os.path.splitext(nome_arquivo)[0]

            eh_atual = (i == self.indice_atual)
            cor_bg = COR_SELECIONADO if eh_atual else "transparent"
            cor_txt = COR_VERDE if eh_atual else COR_TEXTO

            btn_musica = ctk.CTkButton(
                self.scroll_playlist,
                text=f"▶  {nome_limpo}" if eh_atual else f"     {nome_limpo}",
                anchor="w",
                fg_color=cor_bg,
                hover_color="#242424",
                text_color=cor_txt,
                font=("Arial", 13, "bold" if eh_atual else "normal"),
                height=38,
                corner_radius=6,
                command=lambda idx=i: self.selecionar_e_tocar(idx)
            )
            btn_musica.pack(fill="x", pady=2)

    def selecionar_e_tocar(self, indice):
        self.indice_atual = indice
        self.tocar_musica_atual()

    def tocar_musica_atual(self):
        if len(self.playlist_caminhos) > 0:
            caminho = self.playlist_caminhos[self.indice_atual]
            self.extrair_metadados(caminho)
            try:
                pygame.mixer.music.load(caminho)
                pygame.mixer.music.play()
                self.esta_tocando = True
                self.esta_pausado = False
                self.btn_play_pause.configure(text="⏸")
                self.atualizar_visor_playlist(filtrado=bool(self.entry_busca.get().strip()))
            except Exception as e:
                print(f"Erro ao reproduzir: {e}")

    def proxima_musica(self):
        if len(self.playlist_caminhos) > 0:
            if self.aleatorio_ativo:
                self.indice_atual = random.randint(0, len(self.playlist_caminhos) - 1)
            else:
                self.indice_atual += 1
                if self.indice_atual >= len(self.playlist_caminhos):
                    self.indice_atual = 0
            self.tocar_musica_atual()

    def musica_anterior(self):
        if len(self.playlist_caminhos) > 0:
            self.indice_atual -= 1
            if self.indice_atual < 0:
                self.indice_atual = len(self.playlist_caminhos) - 1
            self.tocar_musica_atual()

    def mudar_volume(self, valor):
        pygame.mixer.music.set_volume(valor)
        if valor == 0: self.lbl_icone_volume.configure(text="🔇")
        elif valor < 0.5: self.lbl_icone_volume.configure(text="🔉")
        else: self.lbl_icone_volume.configure(text="🔊")

    def formatar_tempo(self, segundos):
        minutos = int(segundos // 60)
        segundos_restantes = int(segundos % 60)
        return f"{minutos:02d}:{segundos_restantes:02d}"

    def atualizar_progresso(self):
        if self.esta_tocando and not self.esta_pausado and self.tempo_total > 0:
            tempo_atual = pygame.mixer.music.get_pos() / 1000
            if tempo_atual >= 0:
                self.lbl_tempo_atual.configure(text=self.formatar_tempo(tempo_atual))
                progresso = tempo_atual / self.tempo_total
                if progresso > 1.0: progresso = 1.0
                self.barra_progresso.set(progresso)

        for evento in pygame.event.get():
            if evento.type == self.EVENTO_FIM_MUSICA:
                if self.esta_tocando:
                    if self.repetir_ativo:
                        self.tocar_musica_atual()
                    else:
                        self.proxima_musica()

        self.root.after(1000, self.atualizar_progresso)

    def tocar_pausar(self):
        if not self.playlist_caminhos: return
        if not self.esta_tocando:
            self.tocar_musica_atual()
        elif self.esta_tocando and not self.esta_pausado:
            pygame.mixer.music.pause()
            self.esta_pausado = True
            self.btn_play_pause.configure(text="▶")
        elif self.esta_tocando and self.esta_pausado:
            pygame.mixer.music.unpause()
            self.esta_pausado = False
            self.btn_play_pause.configure(text="⏸")

    def parar_musica(self):
        self.esta_tocando = False  
        pygame.mixer.music.stop()
        self.esta_pausado = False
        self.btn_play_pause.configure(text="▶")
        self.barra_progresso.set(0)
        self.lbl_tempo_atual.configure(text="00:00")

    def extrair_metadados(self, caminho_arquivo):
        try:
            audio = MP3(caminho_arquivo, ID3=ID3)
            self.tempo_total = audio.info.length
            self.lbl_tempo_total.configure(text=self.formatar_tempo(self.tempo_total))
            
            titulo = os.path.basename(caminho_arquivo)
            artista = "Artista Desconhecido"
            
            if 'TIT2' in audio: titulo = str(audio['TIT2'])
            if 'TPE1' in audio: artista = str(audio['TPE1'])

            self.lbl_titulo.configure(text=titulo[:24] + "..." if len(titulo) > 24 else titulo)
            self.lbl_artista.configure(text=artista[:26] + "..." if len(artista) > 26 else artista)

            capa_encontrada = False
            if hasattr(audio, 'tags') and audio.tags:
                for tag in audio.tags.values():
                    if isinstance(tag, APIC):
                        imagem = Image.open(io.BytesIO(tag.data))
                        nova_capa = ctk.CTkImage(light_image=imagem, dark_image=imagem, size=(250, 250))
                        self.lbl_capa.configure(image=nova_capa)
                        capa_encontrada = True
                        break
            
            if not capa_encontrada:
                img_padrao = Image.new("RGB", (250, 250), (30, 30, 30))
                capa_padrao = ctk.CTkImage(light_image=img_padrao, dark_image=img_padrao, size=(250, 250))
                self.lbl_capa.configure(image=capa_padrao)
        except Exception as e:
            print(f"Erro metadados: {e}")

if __name__ == "__main__":
    app = ctk.CTk()
    player = EchoXPlayer(app)
    app.mainloop()